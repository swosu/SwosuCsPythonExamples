# scripts/simulate_game_llm.py

from __future__ import annotations

import random
from typing import List, Optional

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
    global _llm_model
    if _llm_model is None:
        # First time you call this, it will download the model
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

        # For a first test, don't let the LLM choose to pass.
        # Later we can give it a '0 = pass' option.
        model = get_llm_model()

        # Build a compact description of the game state
        hand_str = hand_to_str(player.hand, rank_order)
        options_lines = []
        for idx, play in enumerate(legal_plays, start=1):
            opt_str = " ".join(str(c) for c in play)
            options_lines.append(f"{idx}: {opt_str}")

        options_block = "\n".join(options_lines)

        lead_text = "You are LEADING a new trick." if can_lead else "You are RESPONDING to an existing play."
        revolution_text = "Rank order is currently REVERSED." if revolution else "Rank order is normal (3 low, 2 high)."

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
        choice_idx = None
        for token in raw.split():
            if token.strip().isdigit():
                choice_idx = int(token.strip())
                break

        # Basic sanity check; fall back to random on nonsense
        if choice_idx is None or choice_idx < 1 or choice_idx > len(legal_plays):
            choice_idx = random.randint(1, len(legal_plays))

        return legal_plays[choice_idx - 1]


# ---------------- Simple "table" with 1 LLM + 3 bots ---------------- #

def build_players_with_llm() -> list[Player]:
    return [
        Player("LLM_Baby", LLMStrategy()),
        Player("CautiousBot", CautiousStrategy()),
        Player("GreedyBot", GreedyStrategy()),
        Player("ChaosBot", ChaosRevolutionaryStrategy()),
        # You can swap these around as you like
    ]


def main() -> None:
    players = build_players_with_llm()

    # Fresh deck + deal (reusing your existing helpers)
    deck = make_deck()
    deal_deck(deck, players)

    # Run a single round with lots of printouts
    round_engine = PresidentsOfVirtueRound(players, round_index=1)
    round_engine.run()

    print("\n=== Finishing order ===")
    for p in round_engine.finish_order:
        print(f"{p.finish_position}: {p.name} ({p.strategy.short_label()})")


if __name__ == "__main__":
    main()

