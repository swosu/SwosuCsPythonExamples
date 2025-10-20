import random
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor
from scipy.optimize import curve_fit

# --- Configuration ---
list_sizes = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240]
runs_per_size = 10
output_image = "sort_comparison.png"

# --- Sorting Algorithms ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    # parallel merge sort using ThreadPoolExecutor
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    if len(arr) > 512:  # spawn threads for large arrays only
        with ThreadPoolExecutor(max_workers=2) as executor:
            left_future = executor.submit(merge_sort, left)
            right_future = executor.submit(merge_sort, right)
            left = left_future.result()
            right = right_future.result()
    else:
        left = merge_sort(left)
        right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# --- Timing Helper ---
def measure_time(sort_func, n):
    times = []
    for _ in range(runs_per_size):
        data = [random.randint(0, 1_000_000) for _ in range(n)]
        start = time.perf_counter()
        sort_func(data)
        end = time.perf_counter()
        times.append(end - start)
    return np.mean(times), np.std(times)

# --- Measure All Algorithms ---
records = []
for n in list_sizes:
    for name, func in [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort (Parallel)", merge_sort),
        ("Python sorted()", sorted),
    ]:
        avg, std = measure_time(func, n)
        records.append((name, n, avg, std))

df = pd.DataFrame(records, columns=["Algorithm", "n", "time", "std"])

# --- Fit Power Law ---
def power_law(n, a, b):
    return a * (n ** b)

fit_results = {}
for name in df["Algorithm"].unique():
    subset = df[df["Algorithm"] == name]
    params, _ = curve_fit(power_law, subset["n"], subset["time"])
    a, b = params
    predicted = power_law(subset["n"], a, b)
    ss_res = np.sum((subset["time"] - predicted) ** 2)
    ss_tot = np.sum((subset["time"] - np.mean(subset["time"])) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    fit_results[name] = (a, b, r2)

# --- Visualization ---
sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(10, 6))

palette = {
    "Bubble Sort": "dodgerblue",
    "Merge Sort (Parallel)": "orange",
    "Python sorted()": "green",
}

# scatter points with error bars
sns.scatterplot(data=df, x="n", y="time", hue="Algorithm",
                palette=palette, s=80, alpha=0.8)
for algo, color in palette.items():
    subset = df[df["Algorithm"] == algo]
    plt.errorbar(subset["n"], subset["time"], yerr=subset["std"],
                 fmt='none', ecolor=color, alpha=0.3, capsize=2)

# fitted curves
n_fit = np.linspace(min(df["n"]), max(df["n"]), 300)
for algo, (a, b, r2) in fit_results.items():
    plt.plot(n_fit, power_law(n_fit, a, b), label=f"{algo} Fit: n^{b:.2f} (R²={r2:.3f})",
             color=palette[algo], linewidth=2.2, linestyle="--")

plt.xscale("log")
plt.yscale("log")
plt.title("Sorting Algorithm Performance Comparison", fontsize=18, fontweight="bold")
plt.xlabel("List Size (n, log scale)")
plt.ylabel("Average Time (seconds, log scale)")
plt.legend()
plt.tight_layout()
plt.savefig(output_image, dpi=300)
plt.show()

print(f"\nPlot saved as '{output_image}'")
for algo, (a, b, r2) in fit_results.items():
    print(f"{algo:25s} → T = {a:.2e} × n^{b:.2f},  R² = {r2:.4f}")
