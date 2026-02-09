# reporter_console.py
from __future__ import annotations

from typing import List
from models import ScenarioSummary


class ConsoleReporter:
    def print_report(self, summaries: List[ScenarioSummary]) -> None:
        header = (
            f"{'size':>10}  {'scenario':<18}  {'mean (µs)':>12}  {'stdev (µs)':>12}  runs (µs)"
        )
        print(header)
        print("-" * len(header))

        for s in summaries:
            runs_us = [f"{r.elapsed_ns / 1_000.0:.2f}" for r in s.runs]
            print(
                f"{s.size:>10}  {s.scenario_name:<18}  "
                f"{s.mean_us():>12.2f}  {s.stdev_us():>12.2f}  "
                f"{', '.join(runs_us)}"
            )

        print("\nNotes:")
        print("- Linear search is O(n): it tends to grow roughly with list size.")
        print("- 'target_in_list' uses the LAST element to push toward a hard successful case.")
        print("- 'target_not_in_list' forces worst-case scanning every time.")
