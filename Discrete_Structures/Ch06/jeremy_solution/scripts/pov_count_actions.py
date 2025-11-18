#!/usr/bin/env python3
"""
pov_count_actions.py

Warm-up: count how many actions each strategy takes in
presidents_of_virtue_plays.csv.

Run this from the jeremy_solution folder:

    python scripts/pov_count_actions.py
"""

import csv
from collections import Counter
from pathlib import Path


def main() -> None:
    # Assume we run from jeremy_solution
    csv_path = Path("presidents_of_virtue_plays.csv")

    if not csv_path.exists():
        print(f"CSV not found at {csv_path}. Did you run simulate_game.py?")
        return

    counts = Counter()

    # utf-8-sig in case the file has a BOM
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            strategy = row["strategy"]
            counts[strategy] += 1

    print("Actions per strategy:")
    # Sort by strategy name for stable, readable output
    for strategy in sorted(counts):
        print(f"{strategy}: {counts[strategy]} actions")


if __name__ == "__main__":
    main()
