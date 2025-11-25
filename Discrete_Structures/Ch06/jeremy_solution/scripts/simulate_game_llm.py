# scripts/simulate_game_llm.py

from __future__ import annotations

import os
import random
from typing import Dict, List, Optional

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

from pov_strategies import (
    CautiousStrategy,
    GreedyStrategy,
    ChaosRevolutionaryStrategy,
    PairLoverStrategy,
    RandomStrategy,
)

# ---------------------------------------------------------------------------
# Model loading / caching
# ---------------------------------------------------------------------------

# Default env var + fallback model file name
DEFAULT_MODEL_ENV = "POV_LLM_MODEL_1"
DEFAULT_MODEL_FILE = "orca-mini-3b-gguf2-q4_0.gguf"

_model_cache: Dict[str, GPT4All] = {}


def resolve_model_path(model_path: Optional[str] = None) -> str:
    """
    Decide which GGUF file to use.

    Priority:
      1. Explicit model_path argument
      2. POV_LLM_MODEL_1 environment variable
      3. DEFAULT_MODEL_FILE in current directory / GPT4All default path
    """
    if model_path is not None:
        return model_path

    env_path = os.environ.get(DEFAULT_MODEL_ENV)
    if env_path:
        return env_path

    return DEFAULT_MODEL_FILE


def get_llm_model(model_path: Optional[str] = None) -> GPT4All:
    """
    Load (or reuse) a GPT4All model for the given model_path.

    If `model_path` (or the resolved value) is a real file on disk, we treat it
    as a full path: directory + filename.

    Otherwise, we assume it's a model *name* that GPT4All knows how to download.
    """
    path = resolve_model_path(model_path)

    if path not in _model_cache:
        print(f"[LLM] Loading model from: {path}")

        # Case 1: user gave us a full path like /mnt/raid60/models/foo.gguf
        if os.path.isfile(path):
            model_dir, model_name = os.path.split(path)
            _model_cache[path] = GPT4All(
                model_name,
                model_path=model_dir,
                allow_download=False,  # don't try to download, use local file
            )
        else:
            # Case 2: treat `path` as a model name that GPT4All can download
            _model_cache[path] = GPT4All(path)

    return _model_cache[path]


# ---------------------------------------------------------------------------
# LLM-backed Strategy
# ---------------------------------------------------------------------------

class LLMStrategy(Strategy):
    """
    A very baby strategy: we show the model the legal options,
    ask it to pick an index, and parse its answer.

    If anything goes weird, we fall back to a random legal play.
    """

    def __init__(self, model_path: Optional[str] = None, label: str = "LLMBaby") -> None:
        self.model_path = model_path
        self._label = label

    def description(self) -> str:
        return "Tiny local LLM that picks a play from a menu of options."

    def short_label(self) -> str:
        return self._label

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

        # Grab / cache the model for this strategy's configured path.
        model = get_llm_model(self.model_path)

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


# ---------------------------------------------------------------------------
# Simple table: 1 LLM + 3 bots
# ---------------------------------------------------------------------------

def build_players_with_llm(
    model_path: Optional[str] = None,
    llm_label: str = "LLM_Baby",
) -> List[Player]:
    """
    Build a standard table with one LLM player and three classic bots.
    """
    return [
        Player(llm_label, LLMStrategy(model_path=model_path, label="LLMBaby")),
        Player("CautiousBot", CautiousStrategy()),
        Player("GreedyBot", GreedyStrategy()),
        Player("ChaosBot", ChaosRevolutionaryStrategy()),
    ]


def run_single_llm_match_for_duel(label: str, model_path: str) -> int:
    """
    Adapter used by simulate_game_llm_duel.py (or any other tournament harness).

    - Create the LLM strategy using `model_path`.
    - Build the table (LLM player + 3 bots).
    - Run ONE match.
    - Return the LLM player's finishing position (1..4).
    """
    players = [
        Player(label, LLMStrategy(model_path=model_path, label="LLMBaby")),
        Player("CautiousBot", CautiousStrategy()),
        Player("GreedyBot", GreedyStrategy()),
        Player("ChaosBot", ChaosRevolutionaryStrategy()),
    ]

    deck = make_deck()
    deal_deck(deck, players)

    round_engine = PresidentsOfVirtueRound(players, round_index=1)
    round_engine.run()

    # Find the LLM player in the finish order
    llm_player = next(
        p for p in round_engine.finish_order if p.name == label
    )
    return llm_player.finish_position


def main() -> None:
    """
    Demo: run a single game with one LLM (env POV_LLM_MODEL_1 or default)
    plus three bot strategies.
    """
    model_path = resolve_model_path(None)
    print(f"[LLM] Using model for demo: {model_path}")

    players = build_players_with_llm(model_path=model_path, llm_label="LLM_Baby")

    deck = make_deck()
    deal_deck(deck, players)

    round_engine = PresidentsOfVirtueRound(players, round_index=1)
    round_engine.run()

    print("\n=== Finishing order ===")
    for p in round_engine.finish_order:
        print(f"{p.finish_position}: {p.name} ({p.strategy.short_label()})")


if __name__ == "__main__":
    main()

