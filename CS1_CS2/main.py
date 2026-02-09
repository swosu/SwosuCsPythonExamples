# main.py
from __future__ import annotations

import random

from linear_search_lab import (
    RandomArrayFactory,
    LinearSearcher,
    BenchmarkRunner,
    ConsoleReporter,
)


def log_sizes(start: int = 10, decades: int = 5) -> list[int]:
    """
    Log-ish growth sizes: 10, 100, 1000, ...
    decades=5 -> [10, 100, 1000, 10000, 100000]
    """
    if start <= 0:
        raise ValueError("start must be > 0")
    if decades < 1:
        raise ValueError("decades must be >= 1")
    sizes = []
    value = start
    for _ in range(decades):
        sizes.append(value)
        value *= 10
    return sizes


def main() -> None:
    # Reproducible randomness so your timings are comparable run-to-run.
    rng = random.Random(42)

    factory = RandomArrayFactory(rng=rng)
    searcher = LinearSearcher()
    runner = BenchmarkRunner(factory=factory, searcher=searcher, runs_per_scenario=3)
    reporter = ConsoleReporter()

    sizes = log_sizes(start=10, decades=6)  # 10 .. 1,000,000

    all_summaries = []
    for size in sizes:
        summaries = runner.run_for_size(size)
        all_summaries.extend(summaries)

    reporter.print_report(all_summaries)


if __name__ == "__main__":
    main()
