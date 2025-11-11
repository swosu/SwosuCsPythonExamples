#!/usr/bin/env python3
"""
bubble_sort_timing.py

Measure wall-clock time for bubble sort on lists of increasing size
and append the results to a CSV file.

Each row in the CSV has:
    timestamp, n_items, elapsed_seconds
"""

import csv
import random
import time
from datetime import datetime
from pathlib import Path


def bubble_sort(arr):
    """
    In-place bubble sort with early exit if the list is already sorted.
    No tracing, just sorting as fast as this simple algorithm allows.
    """
    n = len(arr)
    for i in range(n):
        swapped = False

        # After each pass, the largest element among the unsorted part
        # "bubbles" to the end of the list.
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If we made no swaps, the list is already sorted.
        if not swapped:
            break


def time_bubble_sort(n, max_value=10**6):
    """
    Generate a random list of length n, sort it with bubble_sort,
    and return the elapsed wall-clock time in seconds.
    """
    data = [random.randint(0, max_value) for _ in range(n)]

    start = time.perf_counter()
    bubble_sort(data)
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
    csv_file = base_dir.parent / "data" / "bubble_sort_timing.csv"

    # List sizes to test. Feel free to tweak this for bigger/smaller runs.
    sizes = [100, 200, 400, 800, 1600, 3200, 6400, 10000, 20000, 30000, 40000]
    trials_per_size = 3  # Run multiple trials per size for smoother data.

    print("Bubble sort timing experiment")
    print(f"Results will be appended to: {csv_file}")
    print()

    for n in sizes:
        for trial in range(1, trials_per_size + 1):
            elapsed = time_bubble_sort(n)
            append_result(csv_file, n, elapsed)
            print(f"n = {n:5d}, trial = {trial}, time = {elapsed:.6f} seconds")

    print("\nDone. Data appended to CSV; ready for plotting in Chapter 2 and beyond.")


if __name__ == "__main__":
    main()
