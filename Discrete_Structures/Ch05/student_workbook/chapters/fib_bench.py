#!/usr/bin/env python3
# ASCII-only benchmark; produces CSV and a plot PDF.

import csv
import time
import matplotlib.pyplot as plt
from fib_variants import DataTracker, fib_recursive, fib_memo, fib_iter

def run_suite(max_n=35):
    rows = []
    trk = DataTracker()

    # Recursive
    for n in range(max_n + 1):
        trk.reset()
        t0 = time.time()
        val = fib_recursive(n, trk)
        t1 = time.time()
        rows.append(["recursive", n, val, t1 - t0, trk.calls, trk.adds, trk.assigns])

    # Memoized
    for n in range(max_n + 1):
        trk.reset()
        t0 = time.time()
        val = fib_memo(n, trk, memo={})
        t1 = time.time()
        rows.append(["memoized", n, val, t1 - t0, trk.calls, trk.adds, trk.assigns])

    # Iterative
    for n in range(max_n + 1):
        trk.reset()
        t0 = time.time()
        val = fib_iter(n, trk)
        t1 = time.time()
        rows.append(["iterative", n, val, t1 - t0, trk.calls, trk.adds, trk.assigns])

    with open("fib_results_ext.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["method","n","value","time_sec","calls","adds","assigns"])
        w.writerows(rows)

    return rows

def plot(csv_path="fib_results_ext.csv"):
    import pandas as pd
    df = pd.read_csv(csv_path)
    methods = ["recursive", "memoized", "iterative"]

    # Time plot
    fig = plt.figure(figsize=(8, 9))
    ax1 = plt.subplot(3,1,1)
    ax2 = plt.subplot(3,1,2)
    ax3 = plt.subplot(3,1,3)

    for m in methods:
        g = df[df["method"] == m]
        ax1.plot(g["n"], g["time_sec"], label=m)
        ax2.plot(g["n"], g["calls"], label=m)
        ax3.plot(g["n"], g["adds"], label=m)

    ax1.set_ylabel("Time (s)")
    ax2.set_ylabel("Function Calls")
    ax3.set_ylabel("Additions")
    ax3.set_xlabel("n")
    for ax in (ax1, ax2, ax3):
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.savefig("chapters/fib_bench_plot.pdf")

if __name__ == "__main__":
    run_suite(35)
    plot()
    print("[OK] Wrote fib_results_ext.csv and chapters/fib_bench_plot.pdf")

