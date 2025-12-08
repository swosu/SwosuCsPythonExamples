"""
monty_hall.py

Monty Hall simulator with:
 - Game, Player, DataHandler classes
 - Plotter class (matplotlib)
 - Automatic simulate-until-precision behavior integrated into simulate flow
"""

import random
import csv
import json
import math
from typing import Optional, Dict, Any, List
from pathlib import Path

import matplotlib.pyplot as plt  # plotting (required for graphs)


# -----------------------
# Core game / data classes
# -----------------------
class Game:
    """Handles a single round of Monty Hall (3 doors: 0,1,2)."""

    def __init__(self, doors: int = 3):
        if doors != 3:
            raise ValueError("This implementation expects exactly 3 doors.")
        self.doors = list(range(doors))
        self.prize_door: Optional[int] = None
        self.revealed_door: Optional[int] = None

    def setup(self):
        self.prize_door = random.choice(self.doors)
        self.revealed_door = None

    def host_reveal(self, player_choice: int) -> int:
        if self.prize_door is None:
            raise RuntimeError("Game not set up. Call setup() first.")
        possible = [d for d in self.doors if d != player_choice and d != self.prize_door]
        if not possible:
            raise RuntimeError("No valid door to reveal (logic error).")
        self.revealed_door = random.choice(possible)
        return self.revealed_door

    def get_switch_target(self, player_choice: int) -> int:
        if self.revealed_door is None:
            raise RuntimeError("Host hasn't revealed a door yet.")
        remaining = [d for d in self.doors if d != player_choice and d != self.revealed_door]
        if len(remaining) != 1:
            raise RuntimeError("Switch target ambiguous.")
        return remaining[0]

    def evaluate(self, final_choice: int) -> bool:
        if self.prize_door is None:
            raise RuntimeError("Game not set up.")
        return final_choice == self.prize_door

    def play_round(self, player_first_choice: int, stay: bool) -> Dict[str, Any]:
        self.setup()
        revealed = self.host_reveal(player_first_choice)
        if stay:
            final_choice = player_first_choice
        else:
            final_choice = self.get_switch_target(player_first_choice)
        won = self.evaluate(final_choice)
        return {
            "prize_door": self.prize_door,
            "player_first_choice": player_first_choice,
            "revealed_door": revealed,
            "player_final_choice": final_choice,
            "stayed": stay,
            "won": won
        }


class DataHandler:
    """Collects and saves round results."""

    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def append(self, record: Dict[str, Any], strategy_label: Optional[str] = None):
        rec = dict(record)
        if strategy_label is not None:
            rec["strategy"] = strategy_label
        self.records.append(rec)

    def summary(self) -> Dict[str, Any]:
        total = len(self.records)
        stays = [r for r in self.records if r.get("stayed")]
        switches = [r for r in self.records if r.get("stayed") is False]
        def rate(lst):
            if not lst:
                return None
            return sum(1 for r in lst if r.get("won")) / len(lst)
        return {
            "total_rounds": total,
            "stay_count": len(stays),
            "switch_count": len(switches),
            "stay_win_rate": rate(stays),
            "switch_win_rate": rate(switches)
        }

    def save_csv(self, filename: str):
        if not self.records:
            raise RuntimeError("No records to save.")
        fieldnames = list({k for r in self.records for k in r.keys()})
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in self.records:
                writer.writerow(r)

    def save_json(self, filename: str):
        with open(filename, "w") as f:
            json.dump(self.records, f, indent=2)


# -----------------------
# Plotter
# -----------------------
class Plotter:
    """
    Plotter for Monty Hall simulation results stored in DataHandler.records.
    """

    def __init__(self, figsize=(10, 6)):
        self.figsize = figsize

    def _split_records(self, records: List[Dict[str, Any]]):
        if not records:
            return [], []
        has_strategy = any("strategy" in r for r in records)
        if has_strategy:
            stay_recs = [r for r in records if str(r.get("strategy", "")).lower() == "stay"]
            switch_recs = [r for r in records if str(r.get("strategy", "")).lower() == "switch"]
            if stay_recs or switch_recs:
                return stay_recs, switch_recs
        stay_recs = [r for r in records if r.get("stayed") is True]
        switch_recs = [r for r in records if r.get("stayed") is False]
        return stay_recs, switch_recs

    def _cumulative_win_rate(self, recs: List[Dict[str, Any]]):
        trials = []
        cum_rates = []
        wins = 0
        for i, r in enumerate(recs, start=1):
            if r.get("won"):
                wins += 1
            trials.append(i)
            cum_rates.append(wins / i)
        return trials, cum_rates

    def plot_from_data(self,
                       data_handler,
                       save_path: str = "monty_hall_plot.png",
                       show: bool = True,
                       include_theoretical: bool = True) -> Path:
        records = getattr(data_handler, "records", None)
        if records is None:
            if isinstance(data_handler, list):
                records = data_handler
            else:
                raise RuntimeError("data_handler must have a .records attribute or be a list of records.")
        stay_recs, switch_recs = self._split_records(records)
        stay_x, stay_rates = self._cumulative_win_rate(stay_recs) if stay_recs else ([], [])
        switch_x, switch_rates = self._cumulative_win_rate(switch_recs) if switch_recs else ([], [])
        fig, ax = plt.subplots(figsize=self.figsize)
        if stay_x:
            ax.plot(stay_x, stay_rates, label="Stay (empirical)")
        if switch_x:
            ax.plot(switch_x, switch_rates, label="Switch (empirical)")
        max_x = 0
        if stay_x:
            max_x = max(max_x, stay_x[-1])
        if switch_x:
            max_x = max(max_x, switch_x[-1])
        if max_x == 0:
            max_x = 1
        if include_theoretical:
            ax.hlines(1/3, xmin=1, xmax=max_x, linestyles="dashed", label="Stay (theoretical = 1/3)")
            ax.hlines(2/3, xmin=1, xmax=max_x, linestyles="dashed", label="Switch (theoretical = 2/3)")
        ax.set_xlabel("Number of trials (per strategy)")
        ax.set_ylabel("Cumulative win rate")
        ax.set_title("Monty Hall: Stay vs Switch — Cumulative Win Rate")
        ax.set_ylim(0, 1)
        ax.grid(True, linewidth=0.4)
        ax.legend()
        fig.tight_layout()
        p = Path(save_path)
        fig.savefig(p)
        if show:
            plt.show()
        plt.close(fig)
        return p


# -----------------------
# Utility functions for automatic stopping
# -----------------------
_Z_FOR_COMMON_CONFIDENCE = {
    0.90: 1.6448536269514722,
    0.95: 1.959963984540054,
    0.99: 2.5758293035489004
}


def _get_z_for_confidence(confidence: float) -> float:
    if confidence in _Z_FOR_COMMON_CONFIDENCE:
        return _Z_FOR_COMMON_CONFIDENCE[confidence]
    # fallback to 99% if unknown
    return _Z_FOR_COMMON_CONFIDENCE[0.99]


def _ci_half_width(p_hat: float, n: int, confidence: float) -> float:
    if n <= 0:
        return float("inf")
    z = _get_z_for_confidence(confidence)
    se = math.sqrt(max(p_hat * (1.0 - p_hat), 0.0) / n)
    return z * se


def _estimate_proportion(records: List[Dict[str, Any]]):
    if not records:
        return 0.0, 0
    wins = sum(1 for r in records if r.get("won"))
    n = len(records)
    return wins / n, n


# -----------------------
# Simulation: automatic until precision reached
# -----------------------
def simulate_until_precision(
    margin: float = 0.02,
    confidence: float = 0.99,
    batch_per_strategy: int = 1000,
    strategy: str = "both",
    save_prefix: Optional[str] = None,
    max_rounds_per_strategy: Optional[int] = 2_000_000
):
    """
    Simulate Monty Hall repeatedly until CI half-width <= margin for each requested strategy.
    - margin: desired half-width (e.g. 0.02 for ±2%).
    - confidence: 0.90, 0.95, or 0.99 (others default to 0.99).
    - batch_per_strategy: run this many trials per strategy each loop iteration.
    - strategy: 'both', 'stay', or 'switch'.
    - save_prefix: optional filename prefix to save CSV/JSON and plot.
    - max_rounds_per_strategy: safety cap.
    """
    if strategy not in ("both", "stay", "switch"):
        raise ValueError("strategy must be 'both', 'stay', or 'switch'")

    game = Game()
    data = DataHandler()

    def run_batch(n_batch: int, stay_flag: bool, label: str):
        for _ in range(n_batch):
            first = random.choice([0, 1, 2])
            rec = game.play_round(first, stay_flag)
            data.append(rec, strategy_label=label)

    rounds_run = {"stay": 0, "switch": 0}
    simulate_stay = (strategy in ("both", "stay"))
    simulate_switch = (strategy in ("both", "switch"))
    target_reached = False

    print(f"Starting auto-simulation: strategy={strategy}, target margin={margin}, confidence={confidence}")
    while True:
        # Run one batch for each requested strategy (if not already past max)
        if simulate_stay and (max_rounds_per_strategy is None or rounds_run["stay"] < max_rounds_per_strategy):
            to_run = batch_per_strategy
            # Avoid overshoot beyond max_rounds_per_strategy
            if max_rounds_per_strategy:
                remaining = max_rounds_per_strategy - rounds_run["stay"]
                if remaining <= 0:
                    to_run = 0
                else:
                    to_run = min(to_run, remaining)
            if to_run > 0:
                run_batch(to_run, True, "stay")
                rounds_run["stay"] += to_run

        if simulate_switch and (max_rounds_per_strategy is None or rounds_run["switch"] < max_rounds_per_strategy):
            to_run = batch_per_strategy
            if max_rounds_per_strategy:
                remaining = max_rounds_per_strategy - rounds_run["switch"]
                if remaining <= 0:
                    to_run = 0
                else:
                    to_run = min(to_run, remaining)
            if to_run > 0:
                run_batch(to_run, False, "switch")
                rounds_run["switch"] += to_run

        # compute estimates and half-widths
        stay_recs = [r for r in data.records if str(r.get("strategy", "")).lower() == "stay"]
        switch_recs = [r for r in data.records if str(r.get("strategy", "")).lower() == "switch"]
        stay_p, stay_n = _estimate_proportion(stay_recs)
        switch_p, switch_n = _estimate_proportion(switch_recs)
        stay_half = _ci_half_width(stay_p, stay_n, confidence) if stay_n > 0 else float("nan")
        switch_half = _ci_half_width(switch_p, switch_n, confidence) if switch_n > 0 else float("nan")

        print("Progress: stay n =", stay_n, "p_hat=", round(stay_p, 4), "half-width=", None if math.isnan(stay_half) else round(stay_half, 5),
              "| switch n =", switch_n, "p_hat=", round(switch_p, 4), "half-width=", None if math.isnan(switch_half) else round(switch_half, 5))

        ok_stay = (not simulate_stay) or (stay_n > 0 and stay_half <= margin)
        ok_switch = (not simulate_switch) or (switch_n > 0 and switch_half <= margin)

        if ok_stay and ok_switch:
            print("Desired precision reached for requested strategies.")
            target_reached = True
            break

        # stop if both have hit max rounds
        if max_rounds_per_strategy is not None:
            stay_at_max = (not simulate_stay) or (rounds_run["stay"] >= max_rounds_per_strategy)
            switch_at_max = (not simulate_switch) or (rounds_run["switch"] >= max_rounds_per_strategy)
            if stay_at_max and switch_at_max:
                print("Max rounds reached for all requested strategies. Stopping.")
                break

    # Summary & optional save/plot
    summary = data.summary()
    print("Final summary:", summary)

    if save_prefix:
        csv_name = f"{save_prefix}.csv"
        json_name = f"{save_prefix}.json"
        data.save_csv(csv_name)
        data.save_json(json_name)
        print("Saved results to", csv_name, "and", json_name)

    plotter = Plotter()
    save_plot_name = f"{save_prefix}_precision_plot.png" if save_prefix else "monty_hall_precision_plot.png"
    try:
        plotter.plot_from_data(data, save_path=save_plot_name, show=True)
        print("Saved/Displayed plot as", save_plot_name)
    except Exception as e:
        print("Plotting failed (matplotlib missing or headless?):", e)

    return data, target_reached


# -----------------------
# Interactive mode (unchanged)
# -----------------------
class Player:
    """Interactive-only player (kept for completeness)."""

    def __init__(self, interactive: bool = True):
        self.interactive = interactive

    def choose_first_door(self) -> int:
        if self.interactive:
            while True:
                try:
                    raw = input("Pick a door (0, 1, or 2): ").strip()
                    c = int(raw)
                    if c in (0, 1, 2):
                        return c
                    print("Please enter 0, 1, or 2.")
                except ValueError:
                    print("Please enter a number (0, 1, or 2).")
        else:
            return random.choice([0, 1, 2])

    def choose_stay_or_switch(self) -> bool:
        if self.interactive:
            while True:
                raw = input("Do you want to stay or switch? (stay/switch): ").strip().lower()
                if raw in ("stay", "s"):
                    return True
                if raw in ("switch", "sw", "w"):
                    return False
                print("Type 'stay' or 'switch'.")
        else:
            raise RuntimeError("Automated player needs strategy externally.")


def interactive_mode():
    print("Monty Hall - Interactive mode")
    game = Game()
    player = Player(interactive=True)
    data = DataHandler()

    while True:
        print("\nStarting a new round.")
        first = player.choose_first_door()
        game.setup()
        revealed = game.host_reveal(first)
        print(f"The host reveals door {revealed} — it's a ZONK!")
        stay = player.choose_stay_or_switch()
        if not stay:
            final_choice = game.get_switch_target(first)
            print(f"You switched to door {final_choice}.")
        else:
            final_choice = first
            print(f"You stayed with door {final_choice}.")
        won = game.evaluate(final_choice)
        if won:
            print("CONGRATULATIONS — you won the prize!")
        else:
            print(f"Sorry — the prize was behind door {game.prize_door}.")
        record = {
            "prize_door": game.prize_door,
            "player_first_choice": first,
            "revealed_door": revealed,
            "player_final_choice": final_choice,
            "stayed": stay,
            "won": won
        }
        data.append(record, strategy_label="interactive")
        cont = input("Play again? (y/n): ").strip().lower()
        if cont not in ("y", "yes"):
            print("\nSession summary:", data.summary())
            save = input("Save session to files? (csv/json/none): ").strip().lower()
            if save in ("csv", "both"):
                csv_name = input("CSV filename (default 'monty_results.csv'): ").strip() or "monty_results.csv"
                data.save_csv(csv_name)
                print("Saved CSV to", csv_name)
            if save in ("json", "both"):
                json_name = input("JSON filename (default 'monty_results.json'): ").strip() or "monty_results.json"
                data.save_json(json_name)
                print("Saved JSON to", json_name)
            print("Goodbye!")
            break


# -----------------------
# Program entry & menu
# -----------------------
def main():
    print("Monty Hall Simulator (auto-stop simulate)")
    while True:
        mode = input("Choose mode: (interactive/simulate/quit): ").strip().lower()
        if mode in ("quit", "q", "exit"):
            print("Bye.")
            break
        elif mode in ("interactive", "i"):
            interactive_mode()
            break
        elif mode in ("simulate", "s"):
            # Ask user which strategy(s) to evaluate
            strat = input("Strategy to run: 'stay', 'switch', or 'both' [both]: ").strip().lower() or "both"
            if strat not in ("stay", "switch", "both"):
                print("Invalid strategy. Try again.")
                continue

            # Ask for desired margin (half-width)
            try:
                margin_raw = input("Desired half-width margin (e.g. 0.02 for ±2%) [0.02]: ").strip() or "0.02"
                margin = float(margin_raw)
                if margin <= 0 or margin >= 1:
                    print("Margin should be a small positive number (e.g. 0.02).")
                    continue
            except ValueError:
                print("Please enter a decimal number like 0.02.")
                continue

            # Ask for confidence level
            try:
                conf_raw = input("Confidence level (0.90, 0.95, or 0.99) [0.99]: ").strip() or "0.99"
                confidence = float(conf_raw)
                if confidence not in (0.90, 0.95, 0.99):
                    print("Supported confidence levels: 0.90, 0.95, 0.99. Using 0.99.")
                    confidence = 0.99
            except ValueError:
                print("Using default 0.99.")
                confidence = 0.99

            # Optional save prefix
            save = input("Save results? (filename prefix or none) [none]: ").strip()
            save_prefix = save if save and save.lower() != "none" else None

            # Optional batch size (fast enough default)
            try:
                batch_raw = input("Batch size per loop iteration (trials per strategy per batch) [1000]: ").strip() or "1000"
                batch_per_strategy = int(batch_raw)
                if batch_per_strategy <= 0:
                    batch_per_strategy = 1000
            except ValueError:
                batch_per_strategy = 1000

            # Run the auto-stopping simulation
            simulate_until_precision(
                margin=margin,
                confidence=confidence,
                batch_per_strategy=batch_per_strategy,
                strategy=strat,
                save_prefix=save_prefix
            )
            break
        else:
            print("Unknown option. Type 'interactive' or 'simulate' or 'quit'.")


if __name__ == "__main__":
    main()
