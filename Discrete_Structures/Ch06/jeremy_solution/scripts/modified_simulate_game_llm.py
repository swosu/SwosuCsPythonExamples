# scripts/simulate_game_llm.py

from __future__ import annotations

import random
import sys
from typing import List, Optional, Dict
from collections import defaultdict

from gpt4all import GPT4All

from presidents_engine import (
    Card,
    Player,
    Strategy,
    PresidentsOfVirtueRound,
    make_deck,
    deal_deck,
    hand_to_str,
    RANKS_NORMAL,
)

# Optional: pull in your existing bots so we can compare
from pov_strategies import (
    CautiousStrategy,
    GreedyStrategy,
    ChaosRevolutionaryStrategy,
    PairLoverStrategy,
    RandomStrategy,
)

# ---------------- LLM setup (global, so we only load once) ---------------- #

_llm_model: Optional[GPT4All] = None


def get_llm_model() -> GPT4All:
    """
    Lazily load a single GPT4All model and reuse it across all rounds.
    """
    global _llm_model
    if _llm_model is None:
        # First time you call this, it will download the model if needed.
        # You can swap this model file for any other GPT4All .gguf you like.
        _llm_model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    return _llm_model


# ---------------- LLM-backed Strategy ---------------- #


class LLMStrategy(Strategy):
    """
    A very baby strategy: we show the model the legal options,
    ask it to pick an index, and parse its answer.

    If anything goes weird, we fall back to a random legal play.
    """

    def description(self) -> str:
        return "Tiny local LLM that picks a play from a menu of options."

    def short_label(self) -> str:
        return "LLMBaby"

    def choose_play(
        self,
        player: Player,
        legal_plays: List[List[Card]],
        can_lead: bool,
        rank_order: List[str],
        revolution: bool,
    ) -> Optional[List[Card]]:

        # No legal plays? Must pass.
        if not legal_plays:
            return None

        # Get (or create) the shared GPT4All instance
        model = get_llm_model()

        # Build a compact description of the game state
        hand_str = hand_to_str(player.hand, rank_order)

        options_lines = []
        for idx, play in enumerate(legal_plays, start=1):
            opt_str = " ".join(str(c) for c in play)
            options_lines.append(f"{idx}: {opt_str}")

        options_block = "\n".join(options_lines)

        lead_text = (
            "You are LEADING a new trick."
            if can_lead
            else "You are RESPONDING to an existing play."
        )
        revolution_text = (
            "Rank order is currently REVERSED."
            if revolution
            else "Rank order is normal (3 low, 2 high)."
        )

        prompt = f"""
You are playing a shedding card game. Your goal is to get rid of all your cards.

Game rules (simplified):
- You may only play one of the LEGAL OPTIONS listed.
- Do NOT invent new cards.
- Pick exactly ONE option index.

State:
- Your name: {player.name}
- Your hand (sorted by strength): {hand_str}
- {lead_text}
- {revolution_text}
- Legal options (each line is an option index and the cards you would play):

{options_block}

IMPORTANT:
Reply with ONLY a single integer: the option number you choose.
Do not explain your reasoning.
""".strip()

        # Ask the baby model
        raw = model.generate(prompt, max_tokens=8)

        # Try to parse the first integer we see
        choice_idx: Optional[int] = None
        for token in raw.split():
            if token.strip().isdigit():
                choice_idx = int(token.strip())
                break

        # Basic sanity check; fall back to random on nonsense
        if choice_idx is None or choice_idx < 1 or choice_idx > len(legal_plays):
            choice_idx = random.randint(1, len(legal_plays))

        return legal_plays[choice_idx - 1]


# ---------------- Player table construction ---------------- #


def build_players_with_llm(llm_name: str = "LLM_Baby") -> list[Player]:
    """
    Build a table with one LLM-driven player and three bot baselines.
    """
    return [
        Player(llm_name, LLMStrategy()),
        Player("CautiousBot", CautiousStrategy()),
        Player("GreedyBot", GreedyStrategy()),
        Player("ChaosBot", ChaosRevolutionaryStrategy()),
        # You could also swap in PairLoverStrategy or RandomStrategy if desired.
    ]


# ---------------- Single-round helper ---------------- #


def run_single_round(
    round_index: int = 1, llm_name: str = "LLM_Baby"
) -> PresidentsOfVirtueRound:
    """
    Set up a fresh deck + players, run a single round,
    and return the round engine so the caller can inspect finish_order.
    """
    players = build_players_with_llm(llm_name=llm_name)

    deck = make_deck()
    random.shuffle(deck)  # extra shuffle, just in case make_deck() is deterministic

    deal_deck(deck, players)

    round_engine = PresidentsOfVirtueRound(players, round_index=round_index)
    round_engine.run()
    return round_engine


# ---------------- Tournament / stats logic ---------------- #


def run_tournament(num_rounds: int = 10, llm_name: str = "LLM_Baby") -> None:
    """
    Run multiple rounds and summarize:
    - how many times each player wins (finish_position == 1)
    - win rate
    - average finishing position
    """
    # stats[name] = {"wins": int, "total_finish": int, "rounds": int}
    stats: Dict[str, Dict[str, float]] = defaultdict(
        lambda: {"wins": 0, "total_finish": 0, "rounds": 0}
    )

    # We’ll use this to print in a nice consistent order at the end.
    player_order = [llm_name, "CautiousBot", "GreedyBot", "ChaosBot"]

    for r in range(1, num_rounds + 1):
        print(f"\n================ Round {r} ================")
        round_engine = run_single_round(round_index=r, llm_name=llm_name)

        # Record stats from this round
        for p in round_engine.finish_order:
            name = p.name
            stats[name]["rounds"] += 1
            stats[name]["total_finish"] += p.finish_position
            if p.finish_position == 1:
                stats[name]["wins"] += 1

        # Quick per-round recap
        print("\nFinishing order for this round:")
        for p in round_engine.finish_order:
            print(f"  {p.finish_position}: {p.name} ({p.strategy.short_label()})")

    # -------------- Final summary --------------
    print(f"\n\n=== Summary over {num_rounds} round(s) ===")
    for name in player_order:
        if stats[name]["rounds"] == 0:
            continue
        wins = int(stats[name]["wins"])
        rounds_played = int(stats[name]["rounds"])
        avg_finish = stats[name]["total_finish"] / rounds_played
        win_rate = (wins / rounds_played) * 100.0
        print(
            f"{name:15s}: "
            f"wins = {wins:3d}  "
            f"win rate = {win_rate:5.1f}%  "
            f"avg finish = {avg_finish:.2f}"
        )


# ---------------- Duel adapter for simulate_game_llm_duel.py ---------------- #


def run_single_llm_match_for_duel(label: str, model_path: str) -> int:
    """
    Adapter used by simulate_game_llm_duel.py.

    - `label` is the name we want to give the LLM player at this table.
    - `model_path` is the GPT4All model filename. For now we ignore it and
      just use the default in get_llm_model(), but you can easily extend
      get_llm_model() to switch models based on this.

    Returns:
        The finishing position (1..4) of the LLM player with name == label.
    """
    # Ensure the model is at least initialized once (even though LLMStrategy
    # calls get_llm_model() itself, this makes it obvious we're using GPT4All).
    _ = get_llm_model()

    players = [
        Player(label, LLMStrategy()),
        Player("CautiousBot", CautiousStrategy()),
        Player("GreedyBot", GreedyStrategy()),
        Player("ChaosBot", ChaosRevolutionaryStrategy()),
    ]

    deck = make_deck()
    random.shuffle(deck)
    deal_deck(deck, players)

    round_engine = PresidentsOfVirtueRound(players, round_index=1)
    round_engine.run()

    # Find and return the LLM player's finish position
    for p in round_engine.finish_order:
        if p.name == label:
            return p.finish_position

    # Fallback: if, for some reason, finish_order didn't contain the LLM player
    for p in players:
        if p.name == label:
            return p.finish_position

    raise RuntimeError(f"LLM player with name '{label}' not found in results.")


# ---------------- Main entrypoint ---------------- #


def main() -> None:
    """
    If you run this file directly, we play multiple rounds and print stats.

    Usage:
        python simulate_game_llm.py          # default 10 rounds
        python simulate_game_llm.py 30       # run 30 rounds
    """
    num_rounds = 10
    if len(sys.argv) >= 2:
        try:
            num_rounds = int(sys.argv[1])
        except ValueError:
            pass  # ignore bad CLI input, keep default

    run_tournament(num_rounds=num_rounds, llm_name="LLM_Baby")


if __name__ == "__main__":
    main()
