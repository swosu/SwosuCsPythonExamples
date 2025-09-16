#!/usr/bin/env python3
"""
Plot benchmarking results for searching and sorting algorithms.

Inputs
------
- CSV produced by your demo/benchmark script with columns:
  algorithm,size,best_time,worst_time,average_time,best_mem,worst_mem,average_mem

Outputs
-------
- figures/
    time_vs_n_sorting_linear.png
    time_vs_n_sorting_loglog.png
    theory_overlay_sorting.png
    time_vs_n_search_linear.png   (if search algos present)
    time_vs_n_search_loglog.png   (if search algos present)
    theory_overlay_search.png     (if search algos present)
    normalized_sorting.png        (time/(n log n) vs n for merge, time/n^2 vs n for bubble)

Notes
-----
- Uses matplotlib only (no seaborn, no specific colors set).
- Automatically detects which algorithms are present in the CSV.
- Scales theoretical curves k·f(n) by fitting k = median(time_i / f(n_i)).
"""

import argparse
import math
import os
from typing import Dict, List

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ------------------ Helpers ------------------ #

SORTING_COMPLEXITY = {
    "bubble_sort": "n2",
    "merge_sort": "nlogn",
    "heap_sort": "nlogn",
    "quick_sort": "nlogn",
    "timsort": "nlogn",
}

SEARCH_COMPLEXITY = {
    "linear_search": "n",
    "binary_search": "logn",
}


def f_of_n(n: np.ndarray, kind: str) -> np.ndarray:
    n = np.asarray(n, dtype=float)
    if kind == "n":
        return n
    if kind == "logn":
        return np.log2(np.maximum(n, 2))
    if kind == "nlogn":
        return n * np.log2(np.maximum(n, 2))
    if kind == "n2":
        return n ** 2
    raise ValueError(f"Unknown complexity kind: {kind}")


def fit_scale(y: np.ndarray, x_fn: np.ndarray) -> float:
    """Return k that best scales x_fn to y; use robust median ratio."""
    ratios = y / np.where(x_fn == 0, np.nan, x_fn)
    ratios = ratios[np.isfinite(ratios)]
    if ratios.size == 0:
        return 1.0
    return float(np.median(ratios))


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


# ------------------ Plotting ------------------ #

def plot_time_vs_n(df: pd.DataFrame, algos: List[str], title: str, outpath: str, loglog: bool = False) -> None:
    plt.figure()
    for algo in algos:
        sub = df[df["algorithm"] == algo].sort_values("size")
        if sub.empty:
            continue
        x = sub["size"].to_numpy()
        y = sub["average_time"].to_numpy()
        plt.plot(x, y, marker="o", linestyle="-", label=algo)
    plt.xlabel("n (array size)")
    plt.ylabel("Average time (s)")
    plt.title(title)
    plt.grid(True, which="both", linestyle=":")
    if loglog:
        plt.xscale("log")
        plt.yscale("log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()


def plot_theory_overlay(df: pd.DataFrame, algo_to_complexity: Dict[str, str], title: str, outpath: str) -> None:
    plt.figure()
    for algo, kind in algo_to_complexity.items():
        sub = df[df["algorithm"] == algo].sort_values("size")
        if sub.empty:
            continue
        x = sub["size"].to_numpy()
        y = sub["average_time"].to_numpy()
        # measured
        plt.plot(x, y, marker="o", linestyle="-", label=f"{algo} (measured)")
        # scaled theory
        theory = f_of_n(x, kind)
        k = fit_scale(y, theory)
        y_hat = k * theory
        plt.plot(x, y_hat, linestyle="--", label=f"{algo} ~ k·{kind}")
    plt.xlabel("n (array size)")
    plt.ylabel("Average time (s)")
    plt.title(title)
    plt.grid(True, which="both", linestyle=":")
    plt.xscale("log")
    plt.yscale("log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()


def plot_normalized_sorting(df: pd.DataFrame, outpath: str) -> None:
    """Flatten curves by dividing time by the theoretical growth term.
    - merge_sort: time / (n log n)
    - bubble_sort: time / n^2
    This highlights constant factors.
    """
    plt.figure()
    seen = False
    for algo in ["merge_sort", "bubble_sort"]:
        sub = df[df["algorithm"] == algo].sort_values("size")
        if sub.empty:
            continue
        seen = True
        x = sub["size"].to_numpy()
        y = sub["average_time"].to_numpy()
        kind = SORTING_COMPLEXITY.get(algo)
        denom = f_of_n(x, kind)
        plt.plot(x, y / denom, marker="o", linestyle="-", label=f"{algo} time/{kind}")
    if not seen:
        return
    plt.xlabel("n (array size)")
    plt.ylabel("Normalized time (s / growth)")
    plt.title("Normalized curves to reveal constant factors (sorting)")
    plt.grid(True, which="both", linestyle=":")
    plt.xscale("log")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath, dpi=150)
    plt.close()


# ------------------ Main ------------------ #

def main():
    ap = argparse.ArgumentParser(description="Plot algorithm benchmark results.")
    ap.add_argument("--csv", default="benchmark_results.csv", help="Path to results CSV")
    ap.add_argument("--out", default="figures", help="Directory to write figures")
    args = ap.parse_args()

    ensure_dir(args.out)

    df = pd.read_csv(args.csv)

    # Decide which families are present
    algos = sorted(df["algorithm"].unique())
    sorting_present = [a for a in algos if a in SORTING_COMPLEXITY]
    searching_present = [a for a in algos if a in SEARCH_COMPLEXITY]

    # Sorting: time vs n (linear & log-log)
    if sorting_present:
        plot_time_vs_n(
            df[df["algorithm"].isin(sorting_present)],
            sorting_present,
            title="Sorting: Time vs n (average over trials)",
            outpath=os.path.join(args.out, "time_vs_n_sorting_linear.png"),
            loglog=False,
        )
        plot_time_vs_n(
            df[df["algorithm"].isin(sorting_present)],
            sorting_present,
            title="Sorting: Time vs n (log-log)",
            outpath=os.path.join(args.out, "time_vs_n_sorting_loglog.png"),
            loglog=True,
        )
        plot_theory_overlay(
            df[df["algorithm"].isin(sorting_present)],
            {a: SORTING_COMPLEXITY[a] for a in sorting_present},
            title="Sorting: measured vs scaled theoretical curves",
            outpath=os.path.join(args.out, "theory_overlay_sorting.png"),
        )
        plot_normalized_sorting(
            df[df["algorithm"].isin(["merge_sort", "bubble_sort"])],
            outpath=os.path.join(args.out, "normalized_sorting.png"),
        )

    # Searching: time vs n (linear & log-log) + theory overlay
    if searching_present:
        plot_time_vs_n(
            df[df["algorithm"].isin(searching_present)],
            searching_present,
            title="Searching: Time vs n (average over trials)",
            outpath=os.path.join(args.out, "time_vs_n_search_linear.png"),
            loglog=False,
        )
        plot_time_vs_n(
            df[df["algorithm"].isin(searching_present)],
            searching_present,
            title="Searching: Time vs n (log-log)",
            outpath=os.path.join(args.out, "time_vs_n_search_loglog.png"),
            loglog=True,
        )
        plot_theory_overlay(
            df[df["algorithm"].isin(searching_present)],
            {a: SEARCH_COMPLEXITY[a] for a in searching_present},
            title="Searching: measured vs scaled theoretical curves",
            outpath=os.path.join(args.out, "theory_overlay_search.png"),
        )

    print(f"Wrote figures to: {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
