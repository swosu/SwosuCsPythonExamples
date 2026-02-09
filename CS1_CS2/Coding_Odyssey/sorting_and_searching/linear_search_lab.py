# linear_search_lab.py
from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev
from time import perf_counter_ns
from typing import List, Sequence, Optional
import random


class RandomArrayFactory:
    """Generates random integer arrays with a guaranteed 'not-found' value available (0)."""

    def __init__(self, rng: Optional[random.Random] = None) -> None:
        self._rng = rng or random.Random()

    def build(self, size: int, low: int = 1, high_multiplier: int = 10) -> List[int]:
        """
        Build a random list of integers of length `size`.

        We generate values in [low, size*high_multiplier] (inclusive).
        That guarantees 0 is NOT in the list, so 0 is a safe 'not found' target.
        """
        if size <= 0:
            raise ValueError("size must be > 0")
        high = max(low, size * high_multiplier)
        
        random_values = []
        for _ in range(size):
            random_value = self._rng.randint(low, high)
            random_values.append(random_value)
        
        return random_values


class LinearSearcher:
    """Classic linear search, returns the index of target or -1 if not found."""

    def search(self, data: Sequence[int], target: int) -> int:
        for i, value in enumerate(data):
            if value == target:
                return i
        return -1


@dataclass(frozen=True)
class RunMeasurement:
    """One timed run of a search."""
    size: int
    target: int
    found: bool
    index: int
    elapsed_ns: int


@dataclass(frozen=True)
class ScenarioSummary:
    """Aggregated results for a scenario at a given size."""
    size: int
    scenario_name: str
    target: int
    found_expected: bool
    runs: List[RunMeasurement]

    @property
    def elapsed_ns_list(self) -> List[int]:
        return [r.elapsed_ns for r in self.runs]

    @property
    def mean_ns(self) -> float:
        return mean(self.elapsed_ns_list)

    @property
    def stdev_ns(self) -> float:
        # population stdev is fine for small run counts (we're just describing the sample we ran)
        return pstdev(self.elapsed_ns_list) if len(self.runs) >= 2 else 0.0

    def mean_us(self) -> float:
        return self.mean_ns / 1_000.0

    def stdev_us(self) -> float:
        return self.stdev_ns / 1_000.0


class BenchmarkRunner:
    """
    Orchestrates:
    - generate array
    - run linear search 3x with target present
    - run linear search 3x with target absent
    - time each run
    """

    def __init__(
        self,
        factory: RandomArrayFactory,
        searcher: LinearSearcher,
        runs_per_scenario: int = 3,
    ) -> None:
        if runs_per_scenario < 1:
            raise ValueError("runs_per_scenario must be >= 1")
        self._factory = factory
        self._searcher = searcher
        self._runs = runs_per_scenario

    def _time_search(self, data: Sequence[int], target: int) -> RunMeasurement:
        start = perf_counter_ns()
        index = self._searcher.search(data, target)
        end = perf_counter_ns()

        found = index != -1
        return RunMeasurement(
            size=len(data),
            target=target,
            found=found,
            index=index,
            elapsed_ns=end - start,
        )

    def run_for_size(self, size: int) -> List[ScenarioSummary]:
        data = self._factory.build(size)

        # "Found" target: pick last element to nudge toward worst-case for a successful search.
        found_target = data[-1]

        # "Not found" target: 0 is guaranteed NOT in the list by our generator.
        not_found_target = 0

        found_runs: List[RunMeasurement] = []
        for _ in range(self._runs):
            found_runs.append(self._time_search(data, found_target))

        not_found_runs: List[RunMeasurement] = []
        for _ in range(self._runs):
            not_found_runs.append(self._time_search(data, not_found_target))

        # Sanity checks: if these fail, something is off with the assumptions.
        if any(r.index == -1 for r in found_runs):
            raise RuntimeError("Expected to find the target, but at least one run did not.")
        if any(r.index != -1 for r in not_found_runs):
            raise RuntimeError("Expected NOT to find the target, but at least one run did.")

        return [
            ScenarioSummary(
                size=size,
                scenario_name="target_in_list",
                target=found_target,
                found_expected=True,
                runs=found_runs,
            ),
            ScenarioSummary(
                size=size,
                scenario_name="target_not_in_list",
                target=not_found_target,
                found_expected=False,
                runs=not_found_runs,
            ),
        ]


class ConsoleReporter:
    """Pretty-ish console output without extra dependencies."""

    def print_report(self, all_summaries: List[ScenarioSummary]) -> None:
        # Grouped printing in the order received.
        header = (
            f"{'size':>10}  {'scenario':<18}  {'mean (µs)':>12}  {'stdev (µs)':>12}  "
            f"{'runs (µs)':<}"
        )
        print(header)
        print("-" * len(header))

        for s in all_summaries:
            runs_us = [f"{r.elapsed_ns / 1_000.0:.2f}" for r in s.runs]
            print(
                f"{s.size:>10}  {s.scenario_name:<18}  "
                f"{s.mean_us():>12.2f}  {s.stdev_us():>12.2f}  "
                f"{', '.join(runs_us)}"
            )

        print("\nNotes:")
        print("- Linear search is O(n): time tends to rise roughly in proportion to list size.")
        print("- 'target_in_list' uses the LAST element to encourage a near-worst-case successful search.")
        print("- 'target_not_in_list' is always worst-case: it scans the whole list.")
