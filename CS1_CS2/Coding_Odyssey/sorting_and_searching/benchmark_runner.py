# benchmark_runner.py
from __future__ import annotations

from time import perf_counter_ns
from typing import List, Sequence

from array_factory import RandomArrayFactory
from linear_searcher import LinearSearcher
from models import RunMeasurement, ScenarioSummary


class BenchmarkRunner:
    """
    For each size:
      - generate one random list
      - run 3 searches where the target IS in the list
      - run 3 searches where the target is NOT in the list
      - time each search
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

        # Found case: choose last element (near worst-case successful search)
        found_target = data[-1]

        # Not found case: 0 is guaranteed absent (generator uses low=1)
        not_found_target = 0

        found_runs = [self._time_search(data, found_target) for _ in range(self._runs)]
        not_found_runs = [self._time_search(data, not_found_target) for _ in range(self._runs)]

        # Sanity checks
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
