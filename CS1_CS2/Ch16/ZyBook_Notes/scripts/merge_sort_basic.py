#!/usr/bin/env python3
"""
merge_sort_basic.py

A recursive merge sort implementation with a simple trace:

- Uses recursion to split the list into halves and then merge them.
- Records the subarray at each recursive call and after each merge.
- Prints a step-by-step trace so you can see the recursion unfold.
- Appends a CSV row for each step, including a timestamp,
  so you can replay the recursion later or quote it in the book.
"""

import csv
from datetime import datetime
from pathlib import Path


def merge_sort_with_trace(data):
    """
    Perform merge sort and record a trace of the recursion.

    Returns:
        sorted_list: the sorted copy of the input list
        trace: a list of (step_number, depth, phase, subarray)

    Fields:
        - step_number: 1, 2, 3, ...
        - depth: recursion depth (0 for the outermost call)
        - phase: "call" when a subarray is first seen,
                 "merged" when that subarray has been fully merged
        - subarray: a snapshot copy of the current subarray at this step
    """
    trace = []
    step = 0

    def helper(arr, depth):
        nonlocal step

        # Record that we are "calling" merge sort on this subarray
        step += 1
        trace.append((step, depth, "call", arr[:]))

        if len(arr) <= 1:
            # Already sorted; nothing to merge
            return arr[:]

        mid = len(arr) // 2
        left = helper(arr[:mid], depth + 1)
        right = helper(arr[mid:], depth + 1)

        # Merge two sorted halves
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Append any leftovers
        merged.extend(left[i:])
        merged.extend(right[j:])

        # Record the merged result at this depth
        step += 1
        trace.append((step, depth, "merged", merged[:]))

        return merged

    sorted_list = helper(data, depth=0)
    return sorted_list, trace


def print_trace(trace):
    """
    Print a friendly view of the merge sort recursion.
    """
    print("Merge sort recursive trace:")
    for step_number, depth, phase, subarray in trace:
        print(
            f"step={step_number:2d}, depth={depth:2d}, "
            f"phase={phase:7s}, subarray={subarray}"
        )


def append_trace_to_csv(trace, csv_path: Path):
    """
    Append the merge sort trace to a CSV file.

    Columns:
        timestamp, step_number, depth, phase, subarray

    - timestamp: when this run was recorded
    - step_number: 1, 2, 3, ...
    - depth: recursion depth at this step
    - phase: "call" or "merged"
    - subarray: space-separated string version of the subarray
    """
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    file_exists = csv_path.exists()
    run_timestamp = datetime.now().isoformat(timespec="seconds")

    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)

        # Write header only if this is a new file
        if not file_exists:
            writer.writerow(
                ["timestamp", "step_number", "depth", "phase", "subarray"]
            )

        for step_number, depth, phase, subarray in trace:
            sub_str = " ".join(str(x) for x in subarray)
            writer.writerow(
                [run_timestamp, step_number, depth, phase, sub_str]
            )


if __name__ == "__main__":
    # Small data set so the trace is easy to follow.
    numbers = [9, 3, 7, 2, 10]

    print("Original list:", numbers)
    sorted_numbers, trace = merge_sort_with_trace(numbers)

    print()
    print_trace(trace)

    print()
    print("Sorted list:  ", sorted_numbers)

    # Write CSV file into ../data relative to this script
    base_dir = Path(__file__).resolve().parent
    csv_file = base_dir.parent / "data" / "merge_sort_basic_trace.csv"

    append_trace_to_csv(trace, csv_file)
    print(f"\nMerge sort trace appended to {csv_file}")

