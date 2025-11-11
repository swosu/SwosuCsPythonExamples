#!/usr/bin/env python3
"""
bubble_sort_analyze.py

Read bubble_sort_timing.csv, compute average time for each n,
fit a quadratic curve, and compare it to an ideal O(n^2) curve.

Outputs:
    figures/bubble_sort_timing_n2.png
"""

import csv
from collections import defaultdict
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


def load_timing_data(csv_path: Path):
    """
    Load timing data from CSV and group times by n_items.

    Returns:
        n_values (sorted list of ints)
        avg_times (list of floats, same order as n_values)
    """
    times_by_n = defaultdict(list)

    with csv_path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                n = int(row["n_items"])
                t = float(row["elapsed_seconds"])
            except (KeyError, ValueError):
                # Skip malformed rows
                continue
            times_by_n[n].append(t)

    n_values = sorted(times_by_n.keys())
    avg_times = [sum(times_by_n[n]) / len(times_by_n[n]) for n in n_values]

    return n_values, avg_times


def fit_quadratic(n_values, avg_times):
    """
    Fit a curve of the form T(n) ~= a*n^2 + b using least squares.

    Returns:
        a, b, fitted_values
    """
    n = np.array(n_values, dtype=float)
    t = np.array(avg_times, dtype=float)

    # We model t ~= a * n^2 + b
    x = n**2
    a, b = np.polyfit(x, t, 1)

    fitted = a * x + b
    return a, b, fitted


def ideal_n2_curve(n_values, avg_times):
    """
    Construct an "ideal" O(n^2) curve k * n^2, scaled so that it
    matches the average time at the smallest n.
    """
    n = np.array(n_values, dtype=float)
    t = np.array(avg_times, dtype=float)

    # Anchor k so that k * n0^2 = t0 at the smallest n.
    n0 = n[0]
    t0 = t[0]
    k = t0 / (n0**2)

    ideal = k * n**2
    return ideal


def plot_results(n_values, avg_times, fit_times, ideal_times, fig_path: Path):
    """
    Plot measured data, fitted quadratic, and ideal O(n^2) curve.
    """
    n = np.array(n_values, dtype=float)
    t = np.array(avg_times, dtype=float)

    fig_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure()
    # Measured data
    plt.plot(n, t, "o", label="Measured avg time")

    # Fitted quadratic
    plt.plot(n, fit_times, "-", label="Fitted a*n^2 + b")

    # Ideal O(n^2)
    plt.plot(n, ideal_times, "--", label="Ideal k*n^2")

    plt.xlabel("Number of items (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Bubble Sort: Timing vs. Input Size")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig(fig_path, dpi=300)
    plt.close()

    print(f"Saved figure to: {fig_path}")


def main():
    base_dir = Path(__file__).resolve().parent
    data_file = base_dir.parent / "data" / "bubble_sort_timing.csv"
    fig_file = base_dir.parent / "figures" / "bubble_sort_timing_n2.png"

    if not data_file.exists():
        raise FileNotFoundError(f"Could not find timing data at {data_file}")

    print(f"Loading timing data from: {data_file}")
    n_values, avg_times = load_timing_data(data_file)

    if not n_values:
        raise RuntimeError("No valid timing data found in CSV.")

    print("Fitting quadratic model T(n) ~= a*n^2 + b ...")
    a, b, fit_times = fit_quadratic(n_values, avg_times)
    ideal_times = ideal_n2_curve(n_values, avg_times)

    print(f"Fit parameters: a = {a:.6e}, b = {b:.6e}")
    print("Generating plot...")
    plot_results(n_values, avg_times, fit_times, ideal_times, fig_file)

    print("Done. This figure is ready to drop into Chapter 2.")


if __name__ == "__main__":
    main()

