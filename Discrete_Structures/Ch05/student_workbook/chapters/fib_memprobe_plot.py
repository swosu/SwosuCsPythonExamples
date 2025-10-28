# chapters/fib_memprobe_plot.py
"""
Smart plotter for fib_memtrace.csv
Detects available columns and generates resource-usage plots.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

fname = "fib_memtrace.csv"

try:
    df = pd.read_csv(fname)
except FileNotFoundError:
    sys.exit(f"[ERROR] {fname} not found. Run fib_memprobe.py first.")

print("[OK] Loaded columns:", list(df.columns))

# try to detect likely column names
possible_n = [c for c in df.columns if c.lower() in ("n", "depth", "step", "call_depth")]
possible_mem = [c for c in df.columns if "mem" in c.lower()]
possible_cpu = [c for c in df.columns if "cpu" in c.lower()]

xcol = possible_n[0] if possible_n else df.columns[0]
memcol = possible_mem[0] if possible_mem else None
cpucol = possible_cpu[0] if possible_cpu else None

plt.figure(figsize=(8,5))

if memcol:
    plt.plot(df[xcol], df[memcol], label=f"Memory ({memcol})", linewidth=2)
if cpucol:
    plt.plot(df[xcol], df[cpucol], label=f"CPU ({cpucol})", linewidth=2, linestyle="--")

plt.xlabel(xcol)
plt.ylabel("Usage")
plt.title("Fibonacci Resource Trace")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("chapters/fib_memprobe_plot.pdf")
print("[OK] Wrote chapters/fib_memprobe_plot.pdf")

