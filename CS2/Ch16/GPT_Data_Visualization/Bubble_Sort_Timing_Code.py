import random
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- Configuration ---
list_sizes = [10, 20, 40, 80, 160, 320, 640, 1280, 2560]
runs_per_size = 5
output_image = "bubble_sort_timing.png"

# --- Bubble Sort Function ---
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# --- Measure Wall Clock Time ---
results = []
for n in list_sizes:
    times = []
    for _ in range(runs_per_size):
        data = [random.randint(0, 1000000) for _ in range(n)]
        start = time.perf_counter()
        bubble_sort(data)
        end = time.perf_counter()
        times.append(end - start)
    avg_time = np.mean(times)
    results.append((n, avg_time))

# --- Create DataFrame ---
df = pd.DataFrame(results, columns=["n", "time"])

# --- Fit Curve T = a * n^b ---
def power_law(n, a, b):
    return a * (n ** b)

params, _ = curve_fit(power_law, df["n"], df["time"])
a, b = params

# --- Generate Fitted Data for Smooth Curve ---
n_fit = np.linspace(min(df["n"]), max(df["n"]), 200)
t_fit = power_law(n_fit, a, b)

# --- Visualization ---
sns.set_theme(style="whitegrid", context="talk")

plt.figure(figsize=(10, 6))
# Raw data as bars
sns.barplot(x="n", y="time", data=df, color="skyblue", alpha=0.7)

# Best-fit curve as a line
sns.lineplot(x=n_fit, y=t_fit, color="darkblue", linewidth=2.5, label=f"Fit: T = {a:.2e} * n^{b:.2f}")

plt.xscale("log")  # log axis for clarity
plt.yscale("linear")

plt.title("Bubble Sort Timing vs. List Size", fontsize=18, fontweight="bold")
plt.xlabel("List Size (n, log scale)")
plt.ylabel("Average Time (seconds)")
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig(output_image, dpi=300)
plt.show()

print(f"Plot saved as '{output_image}'")
print(df)
