#!/usr/bin/env python3
"""
pov_peek.py

Quick, data-science-style peek at presidents_of_virtue_plays.csv.

Run this from the jeremy_solution folder:

    python scripts/pov_peek.py
"""

import csv
from collections import Counter, defaultdict
from pathlib import Path


def main() -> None:
    # 1. Locate the CSV
    csv_path = Path("presidents_of_virtue_plays.csv")

    if not csv_path.exists():
        print(f"CSV not found at {csv_path}. Did you run simulate_game.py first?")
        return

    # 2. Load all rows
    # utf-8-sig handles the BOM that may be at the start of the file
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} actions from {csv_path}.\n")

    # 3. Show the first few actions
    print("First 5 actions:")
    for row in rows[:5]:
        print(
            f"round {row['round']}, trick {row['trick']}, step {row['step']}: "
            f"{row['player_name']} ({row['strategy']}) "
            f"{row['action']} {row['cards_played']}"
        )
    print()

    # 4. Actions per strategy (how busy each style is)
    actions_per_strategy = Counter()
    for row in rows:
        actions_per_strategy[row["strategy"]] += 1

    print("=== Actions per strategy ===")
    for strategy, count in actions_per_strategy.most_common():
        print(f"{strategy:18s}: {count:6d} actions")
    print()

    # 5. Finish-position summary per strategy
    finishes_per_strategy = defaultdict(list)

    for row in rows:
        pos_text = row["finish_position"]
        if pos_text:  # skip empty / None
            try:
                pos = int(pos_text)
            except ValueError:
                continue
            finishes_per_strategy[row["strategy"]].append(pos)

    print("=== Finish-position summary by strategy ===")
    for strategy, positions in finishes_per_strategy.items():
        n = len(positions)
        if n == 0:
            print(f"{strategy:18s}: no finish data")
            continue

        avg_pos = sum(positions) / n
        wins = sum(1 for p in positions if p == 1)
        top2 = sum(1 for p in positions if p <= 2)

        print(
            f"{strategy:18s}: "
            f"avg_finish = {avg_pos:4.2f} over {n:5d} actions "
            f"(wins={wins}, top2={top2})"
        )
    print()

    # 6. Justice Burst usage per strategy
    justice_bursts = Counter()
    for row in rows:
        if row.get("is_justice_burst") == "True":
            justice_bursts[row["strategy"]] += 1

    print("=== Justice Burst (2s) usage by strategy ===")
    total_bursts = sum(justice_bursts.values())
    if total_bursts == 0:
        print("No Justice Bursts recorded.")
    else:
        for strategy, count in justice_bursts.most_common():
            fraction = count / total_bursts
            print(
                f"{strategy:18s}: {count:4d} bursts "
                f"({fraction:.1%} of all Justice Bursts)"
            )


if __name__ == "__main__":
    main()
