#!/usr/bin/env python3
import csv
import time
import matplotlib.pyplot as plt

class DataTracker:
    def __init__(self):
        self.calls = 0
        self.adds = 0
        self.assigns = 0
        self.times = {}
    
    def track(self, n, value, t0, t1):
        self.times[n] = {
            "value": value,
            "time": t1 - t0,
            "calls": self.calls,
            "adds": self.adds,
            "assigns": self.assigns
        }

    def reset(self):
        self.calls = 0
        self.adds = 0
        self.assigns = 0

def fib_recursive(n, tracker):
    tracker.calls += 1
    if n <= 1:
        tracker.assigns += 1
        return n
    tracker.adds += 1
    return fib_recursive(n-1, tracker) + fib_recursive(n-2, tracker)

def fib_iterative(n, tracker):
    tracker.calls += 1
    a, b = 0, 1
    tracker.assigns += 2
    for _ in range(2, n+1):
        tracker.adds += 1
        a, b = b, a + b
        tracker.assigns += 2
    return b if n else a

def measure_fibonacci(max_n=30):
    tracker = DataTracker()
    results = []

    # Recursive measurement
    for n in range(0, max_n+1):
        tracker.reset()
        t0 = time.time()
        val = fib_recursive(n, tracker)
        t1 = time.time()
        tracker.track(n, val, t0, t1)
        results.append(["recursive", n, val, tracker.times[n]["time"], tracker.calls, tracker.adds, tracker.assigns])

    # Iterative measurement
    for n in range(0, max_n+1):
        tracker.reset()
        t0 = time.time()
        val = fib_iterative(n, tracker)
        t1 = time.time()
        tracker.track(n, val, t0, t1)
        results.append(["iterative", n, val, tracker.times[n]["time"], tracker.calls, tracker.adds, tracker.assigns])

    # Write results
    with open("fib_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["method", "n", "value", "time_sec", "calls", "adds", "assigns"])
        writer.writerows(results)

    return results

def plot_results(csv_file="fib_results.csv"):
    import pandas as pd
    df = pd.read_csv(csv_file)
    fig, axs = plt.subplots(3, 1, figsize=(8, 10))

    for method, group in df.groupby("method"):
        axs[0].plot(group["n"], group["time_sec"], label=method)
        axs[1].plot(group["n"], group["calls"], label=method)
        axs[2].plot(group["n"], group["adds"], label=method)

    axs[0].set_ylabel("Time (s)")
    axs[1].set_ylabel("Function Calls")
    axs[2].set_ylabel("Additions")
    axs[2].set_xlabel("n")
    for ax in axs:
        ax.legend()
        ax.grid(True)
    plt.tight_layout()
    plt.savefig("fib_results_plot.pdf")

if __name__ == "__main__":
    measure_fibonacci(30)
    plot_results()
    print("✅ Fibonacci analysis complete. Results saved to fib_results.csv and fib_results_plot.pdf")

