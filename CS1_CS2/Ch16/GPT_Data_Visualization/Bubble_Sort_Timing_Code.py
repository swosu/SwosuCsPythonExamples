import random
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- Configuration ---
list_sizes = [10, 20, 40, 80, 160, 320, 640, 1280, 2560]
runs_per_size = 20
output_image = "bubble_sort_timing_r2.png"

# --- Bubble Sort Function ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# --- Measure Wall Clock Time ---
records = []
for n in list_sizes:
    times = []
    for _ in range(runs_per_size):
        data = [random.randint(0, 1_000_000) for _ in range(n)]
        start = time.perf_counter()
        bubble_sort(data)
        end = time.perf_counter()
        times.append(end - start)
    avg = np.mean(times)
    std = np.std(times)
    records.append((n, avg, std))

# --- DataFrame ---
df = pd.DataFrame(records, columns=["n", "time", "std"])

# --- Fit Power-Law Curve T = a * n^b ---
def power_law(n, a, b):
    return a * (n ** b)

params, _ = curve_fit(power_law, df["n"], df["time"])
a, b = params

# --- Compute R² for goodness of fit ---
predicted = power_law(df["n"], a, b)
ss_res = np.sum((df["time"] - predicted) ** 2)
ss_tot = np.sum((df["time"] - np.mean(df["time"])) ** 2)
r2 = 1 - (ss_res / ss_tot)

# --- Generate Smooth Curve for Plot ---
n_fit = np.linspace(min(df["n"]), max(df["n"]), 300)
t_fit = power_law(n_fit, a, b)

# --- Visualization ---
sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(9, 6))

# Scatter plot with error bars
sns.scatterplot(
    x="n", y="time", data=df, color="dodgerblue", s=100,
    label="Measured (mean ± std)"
)
plt.errorbar(df["n"], df["time"], yerr=df["std"], fmt='none',
             ecolor='lightblue', elinewidth=1, capsize=3, alpha=0.6)

# Fitted curve
sns.lineplot(
    x=n_fit, y=t_fit, color="darkblue", linewidth=2.5,
    label=f"Fit: T = {a:.2e} × n^{b:.2f}  (R² = {r2:.4f})"
)

plt.title("Bubble Sort Runtime vs. List Size", fontsize=18, fontweight="bold")
plt.xlabel("List Size (n)")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.tight_layout()
plt.savefig(output_image, dpi=300)
plt.show()

# --- Console Report ---
print(f"\nSaved plot as '{output_image}'")
print(f"Fitted equation:  T = {a:.2e} × n^{b:.2f}")
print(f"Goodness of fit (R²): {r2:.4f}\n")
print(df)
