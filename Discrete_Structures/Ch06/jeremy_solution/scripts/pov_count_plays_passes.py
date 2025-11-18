#!/usr/bin/env python3
"""
pov_count_plays_passes.py

Count how many actions are 'play' vs 'pass',
and then break that down by strategy.

Run this from the jeremy_solution folder:

    python scripts/pov_count_plays_passes.py
"""

import csv
from collections import Counter, defaultdict
from pathlib import Path


def main() -> None:
    csv_path = Path("presidents_of_virtue_plays.csv")

    if not csv_path.exists():
        print(f"CSV not found at {csv_path}. Did you run simulate_game.py first?")
        return

    # Overall action counts (play vs pass)
    overall_actions = Counter()

    # Nested: strategy -> Counter({'play': x, 'pass': y, ...})
    strategy_actions = defaultdict(Counter)

    # Read the CSV
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            action = row["action"]          # e.g., "play" or "pass"
            strategy = row["strategy"]      # e.g., "Cautious"

            overall_actions[action] += 1
            strategy_actions[strategy][action] += 1

    # --- Overall summary ---
    print("=== Overall action counts ===")
    for action, count in overall_actions.items():
        print(f"{action:5s}: {count} actions")
    print()

    # --- Per-strategy breakdown ---
    print("=== Actions by strategy and type ===")
    # Sort strategies alphabetically for stable output
    for strategy in sorted(strategy_actions.keys()):
        counts = strategy_actions[strategy]
        plays = counts.get("play", 0)
        passes = counts.get("pass", 0)
        total = sum(counts.values())

        # Compute simple pass rate
        pass_rate = (passes / total) if total > 0 else 0.0

        print(
            f"{strategy:18s} -> "
            f"play: {plays:3d}, pass: {passes:3d}, "
            f"total: {total:3d}, pass_rate: {pass_rate:.2f}"
        )


if __name__ == "__main__":
    main()
