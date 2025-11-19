# scripts/simulate_game.py
"""
Top-level simulation script for Presidents of Virtue.

Controls:
- number of rounds
- random seed
- which players to use (via pov_players)
- where to write CSV logs (via pov_logging)
"""

import random
from typing import List, Dict

from presidents_engine import (
    make_deck,
    deal_deck,
    PresidentsOfVirtueRound,
    Player,
)
from pov_players import create_oklahoma_players, create_oklahoma_with_human
from pov_logging import write_play_log_csv


def simulate_game(num_rounds: int = 3, seed: int = 0, vs_human: bool = False) -> None:
    random.seed(seed)

    if vs_human:
        players: List[Player] = create_oklahoma_with_human(
            human_name="Jeremy",
            human_position=0,   # 0–4: where you sit at the table
            use_smart_bot=True,
        )
    else:
        players: List[Player] = create_oklahoma_players()

    print("=== SpankTopia Table ===")
    for p in players:
        print(f"  {p.name:18s} -> {p.strategy.short_label():12s}")
    print()

    all_play_logs: List[Dict[str, object]] = []

    for r in range(1, num_rounds + 1):
        deck = make_deck()
        deal_deck(deck, players)
        round_game = PresidentsOfVirtueRound(players, round_index=r)
        round_game.run()

        # Fill in finish info for that round's logs
        finish_map = {
            p.name: (p.finish_position, p.ended_on_bomb)
            for p in players
        }

        for entry in round_game.play_log:
            name = entry["player_name"]
            fp, bomb = finish_map.get(name, (None, None))
            entry["finish_position"] = fp
            entry["ended_on_bomb"] = bomb
            all_play_logs.append(entry)

        print("\nRound", r, "results:")
        for p in sorted(players, key=lambda pl: pl.finish_position or 99):
            bomb_note = " (ended on bomb)" if p.ended_on_bomb else ""
            print(f"  {p.finish_position}: {p.name:18s} "
                  f"[{p.strategy.short_label():12s}]{bomb_note}")
        print("-" * 60)

    csv_name = "presidents_of_virtue_plays.csv"
    write_play_log_csv(all_play_logs, csv_name)
    print(f"\nWrote detailed play log to {csv_name}")

    # Optional: overall summary across all rounds
    print("\n=== Overall finish-position summary ===")
    summary: Dict[str, List[int]] = {}
    for p in players:
        summary[p.name] = []

    for row in all_play_logs:
        name = row["player_name"]
        pos = row["finish_position"]
        if pos is not None:
            summary[name].append(pos)

    for p in players:
        positions = summary[p.name]
        if positions:
            avg = sum(positions) / len(positions)
            print(f"{p.name:18s} [{p.strategy.short_label():12s}] "
                  f"average finish ≈ {avg:.2f} over {num_rounds} round(s)")
        else:
            print(f"{p.name:18s} [{p.strategy.short_label():12s}] "
                  f"(no positions recorded?)")


if __name__ == "__main__":
    # AI vs AI:
    # simulate_game(num_rounds=3, seed=42, vs_human=False)

    # Human vs bots (you control one seat at the table):
    simulate_game(num_rounds=3, seed=42, vs_human=True)

