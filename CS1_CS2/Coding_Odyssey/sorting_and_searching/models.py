# models.py
from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev
from typing import List


@dataclass(frozen=True)
class RunMeasurement:
    size: int
    target: int
    found: bool
    index: int
    elapsed_ns: int


@dataclass(frozen=True)
class ScenarioSummary:
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
        return pstdev(self.elapsed_ns_list) if len(self.runs) >= 2 else 0.0

    def mean_us(self) -> float:
        return self.mean_ns / 1_000.0

    def stdev_us(self) -> float:
        return self.stdev_ns / 1_000.0
