#!/usr/bin/env python3
"""
simulate_game_llm_duel.py

Run Presidents of Virtue games where two different LLM configurations
take turns playing against the same bot table so we can compare how
they perform.

This script is intentionally separate from simulate_game_llm.py so
you can keep the original “LLM_Baby vs bots” run intact.
"""

import os
import statistics
from dataclasses import dataclass
from typing import Dict, List, Tuple

# You will adapt these imports to match your actual engine entrypoints.
# The idea is: whatever you currently use in simulate_game_llm.py to
# run ONE game with ONE LLM player, we re-use here.
#
# Example / placeholder:
# from presidents_engine import run_presidents_match_with_llm
# from pov_logging import make_logger
#
# For now, I’ll write this assuming you have a helper function you can
# create in simulate_game_llm.py called `run_single_llm_match` that:
#   - takes a model label and a model path
#   - runs ONE game
#   - returns the finishing position of the LLM player (1 = best, 4/5 = worst)
#
# You can add that function to simulate_game_llm.py, or just inline
# whatever logic you already have.

# ---------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------


@dataclass
class LlmProfile:
    label: str          # "LLM_Baby", "LLM_Toddler"
    env_var: str        # environment variable that points to GGUF
    default_path: str   # fallback path if env var is unset


# Model 1 and Model 2 configs.
# Adjust the default paths to wherever you stash your GGUF files on DTN.
LLM_PROFILES: Dict[str, LlmProfile] = {
    "model1": LlmProfile(
        label="LLM_Baby",
        env_var="POV_LLM_MODEL_1",
        default_path="/mnt/raid60/models/llm_baby.gguf",
    ),
    "model2": LlmProfile(
        label="LLM_Toddler",
        env_var="POV_LLM_MODEL_2",
        default_path="/mnt/raid60/models/llm_toddler.gguf",
    ),
}


# ---------------------------------------------------------------------
# Hooks you will wire into your existing simulate_game_llm code
# ---------------------------------------------------------------------

def resolve_model_path(profile: LlmProfile) -> str:
    """Get the model path from env var or fallback default."""
    path = os.environ.get(profile.env_var, profile.default_path)
    return path


def run_single_llm_match(profile: LlmProfile) -> int:
    """
    *** YOU MUST ADAPT THIS FUNCTION ***

    This should:
      1. Use `profile.label` and `resolve_model_path(profile)` to
         configure the LLM player.
      2. Run ONE full game of Presidents of Virtue with that LLM
         plus your existing bot strategies (Cautious, Greedy, Chaos, etc.).
      3. Return the finishing position of the LLM player:
         1 = President, 2 = Vice President, ..., N = last.

    For now this function is just a placeholder that raises if you forget
    to implement it.
    """
    raise NotImplementedError(
        "Implement run_single_llm_match(profile) using your existing "
        "simulate_game_llm engine."
    )


# ---------------------------------------------------------------------
# Tournament runner
# ---------------------------------------------------------------------


def run_tournament(
    n_games: int = 20,
    models: Tuple[str, str] = ("model1", "model2"),
) -> None:
    """
    Alternate between the two LLM profiles, running n_games for each,
    and summarize their average finishing positions.
    """
    profile_a = LLM_PROFILES[models[0]]
    profile_b = LLM_PROFILES[models[1]]

    results: Dict[str, List[int]] = {
        profile_a.label: [],
        profile_b.label: [],
    }

    print("=== LLM Duel Tournament ===")
    print(f"  Model A: {profile_a.label} (env {profile_a.env_var})")
    print(f"  Model B: {profile_b.label} (env {profile_b.env_var})")
    print(f"  Games per model: {n_games}")
    print("------------------------------------------------------------")

    for i in range(1, n_games + 1):
        print(f"\n>>> Game {i} with {profile_a.label}")
        pos_a = run_single_llm_match(profile_a)
        results[profile_a.label].append(pos_a)
        print(f"Result: {profile_a.label} finished position {pos_a}")

        print(f"\n>>> Game {i} with {profile_b.label}")
        pos_b = run_single_llm_match(profile_b)
        results[profile_b.label].append(pos_b)
        print(f"Result: {profile_b.label} finished position {pos_b}")

    print("\n=== Tournament Summary ===")
    for label, finishes in results.items():
        avg = statistics.fmean(finishes)
        counts = {}
        for p in finishes:
            counts[p] = counts.get(p, 0) + 1
        histogram = "  ".join(f"{pos}: {cnt}" for pos, cnt in sorted(counts.items()))
        print(f"{label}:")
        print(f"  Games: {len(finishes)}")
        print(f"  Avg finish: {avg:.2f}")
        print(f"  Histogram: {histogram}")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Compare two LLM configs on the Presidents of Virtue table."
    )
    parser.add_argument(
        "--games",
        type=int,
        default=10,
        help="Number of games per model (default: 10)",
    )
    parser.add_argument(
        "--models",
        nargs=2,
        default=("model1", "model2"),
        metavar=("MODEL_A", "MODEL_B"),
        help="Which profiles from LLM_PROFILES to use (default: model1 model2)",
    )

    args = parser.parse_args()
    run_tournament(n_games=args.games, models=tuple(args.models))


if __name__ == "__main__":
    main()

