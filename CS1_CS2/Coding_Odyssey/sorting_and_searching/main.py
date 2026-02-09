# main.py
from __future__ import annotations

import random

from array_factory import RandomArrayFactory
from linear_searcher import LinearSearcher
from benchmark_runner import BenchmarkRunner
from reporter_console import ConsoleReporter
from sizes import log_sizes


def main() -> None:
    # Seeded RNG for reproducible lists (stable comparisons)
    rng = random.Random(42)

    # add a quick example of what having a random seed set means
    print("Using seeded RNG for reproducible results.")
    example_list = RandomArrayFactory(rng=rng).build(size=5)
    print(f"Example list: {example_list}")

    factory = RandomArrayFactory(rng=rng)
    searcher = LinearSearcher()
    runner = BenchmarkRunner(factory=factory, searcher=searcher, runs_per_scenario=3)
    reporter = ConsoleReporter()

    sizes = log_sizes(start=10, decades=6)

    all_summaries = []
    for size in sizes:
        all_summaries.extend(runner.run_for_size(size))

    reporter.print_report(all_summaries)


if __name__ == "__main__":
    main()
