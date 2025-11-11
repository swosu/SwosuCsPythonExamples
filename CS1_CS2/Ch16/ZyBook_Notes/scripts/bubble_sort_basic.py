#!/usr/bin/env python3
"""
bubble_sort_basic.py

Bubble sort with a simple trace:

- Prints the list after each full bubble pass so you can
  see the numbers "bubbling" toward the end.
- Appends a CSV row for each pass, including a timestamp,
  so you can track when the data was generated.
"""

import csv
from pathlib import Path
from datetime import datetime


def bubble_sort_with_trace(data):
    """
    Perform bubble sort and record the list state after each pass.

    Returns:
        sorted_list: the sorted copy of the input list
        trace: a list of (pass_number, state_list) snapshots

    pass_number = 0 is the initial state before any passes.
    """
    arr = data[:]  # copy so we don't mutate the original list
    n = len(arr)
    trace = []

    # Record the initial (unsorted) state
    trace.append((0, arr[:]))

    for i in range(n):
        swapped = False

        # One "bubble pass"
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap out-of-order neighbors
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Record the state of the list *after* this pass
        trace.append((i + 1, arr[:]))

        # If no swaps were made, the list is already sorted
        if not swapped:
            break

    return arr, trace


def print_trace(trace):
    """
    Print a friendly view of how the list changes after each pass.
    """
    print("Bubble sort trace (state after each full pass):")
    for pass_number, state in trace:
        if pass_number == 0:
            label = "Start"
        else:
            label = f"Pass {pass_number}"
        print(f"{label:>6}: {state}")


def append_trace_to_csv(trace, csv_path: Path):
    """
    Append the bubble sort trace to a CSV file.

    Columns:
        timestamp, pass_number, state_list

    - timestamp: when this run was recorded
    - pass_number: 0 for initial state, 1, 2, ... for later passes
    - state_list: space-separated string version of the list
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    file_exists = csv_path.exists()
    run_timestamp = datetime.now().isoformat(timespec="seconds")

    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)

        # Write header only if this is a new file
        if not file_exists:
            writer.writerow(["timestamp", "pass_number", "state_list"])

        for pass_number, state in trace:
            state_str = " ".join(str(x) for x in state)
            writer.writerow([run_timestamp, pass_number, state_str])


if __name__ == "__main__":
    # Example data; later chapters can experiment with other lists.
    numbers = [9, 3, 7, 2, 10]

    print("Original list:", numbers)
    sorted_numbers, trace = bubble_sort_with_trace(numbers)

    print()
    print_trace(trace)

    print()
    print("Sorted list:  ", sorted_numbers)

    # Write CSV file into ../data relative to this script
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir.parent / "data" / "bubble_sort_basic_trace.csv"

    append_trace_to_csv(trace, csv_file)
    print(f"\nTrace appended to {csv_file}")
