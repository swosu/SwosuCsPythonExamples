# scripts/pov_logging.py
"""
CSV logging utilities for Presidents of Virtue simulations.

Provides:
- write_play_log_csv(play_logs, filename)
"""

import csv
from typing import List, Dict


def write_play_log_csv(play_logs: List[Dict[str, object]], filename: str) -> None:
    if not play_logs:
        return

    fieldnames = [
        "round", "trick", "step",
        "player_name", "strategy",
        "action", "cards_played",
        "hand_size_before", "hand_size_after",
        "current_size_before", "current_rank_before",
        "is_lead", "is_justice_burst", "is_revolution_trigger",
        "revolution_state_after",
        "finish_position", "ended_on_bomb",
    ]

    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in play_logs:
            writer.writerow(row)

