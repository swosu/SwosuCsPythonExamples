#!/usr/bin/env python3
"""
merge_sort_timing.py

Measure wall-clock time for merge sort on lists of increasing size
and append the results to a CSV file.

Each row in the CSV has:
    timestamp, n_items, elapsed_seconds
"""

import csv
import random
import time
from datetime import datetime
from pathlib import Path


def merge_sort(arr):
    """
    Recursive merge sort that returns a new sorted list.

    This version does no tracing; it is written to be as
    straightforward and efficient as possible for timing.
    """
    n = len(arr)
    if n <= 1:
        return arr

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merged = []
    i = j = 0

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append leftovers from either half
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def time_merge_sort(n, max_value=10**6):
    """
    Generate a random list of length n, sort it with merge_sort,
    and return the elapsed wall-clock time in seconds.
    """
    data = [random.randint(0, max_value) for _ in range(n)]

    start = time.perf_counter()
    _ = merge_sort(data)
    end = time.perf_counter()

    return end - start


def append_result(csv_path: Path, n: int, elapsed: float):
    """
    Append a single timing result to the CSV file.

    Columns:
        timestamp, n_items, elapsed_seconds
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    file_exists = csv_path.exists()
    timestamp = datetime.now().isoformat(timespec="seconds")

    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)

        # Write a header row only if the file is new.
        if not file_exists:
            writer.writerow(["timestamp", "n_items", "elapsed_seconds"])

        writer.writerow([timestamp, n, f"{elapsed:.6f}"])


def main():
    # Figure out where we are and where the data directory lives.
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir.parent / "data" / "merge_sort_timing.csv"

    # Match your bubble_sort_timing sizes so we can compare later.
    sizes = [100, 200, 400, 800, 1600, 3200, 6400, 10000, 20000, 30000, 40000]
    trials_per_size = 3  # Run multiple trials per size for smoother data.

    print("Merge sort timing experiment")
    print(f"Results will be appended to: {csv_file}")
    print()

    for n in sizes:
        for trial in range(1, trials_per_size + 1):
            elapsed = time_merge_sort(n)
            append_result(csv_file, n, elapsed)
            print(f"n = {n:5d}, trial = {trial}, time = {elapsed:.6f} seconds")

    print("\nDone. Data appended to CSV; ready for plotting alongside bubble sort.")


if __name__ == "__main__":
    main()

