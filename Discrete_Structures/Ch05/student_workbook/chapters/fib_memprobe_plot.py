# chapters/fib_memprobe_plot.py
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv("fib_memtrace.csv")
plt.figure(figsize=(8,5))
plt.plot(df['n'], df['rss_mb'], label='Memory (MB)')
plt.plot(df['n'], df['cpu_percent'], label='CPU %')
plt.xlabel('n')
plt.ylabel('Usage')
plt.title('Fibonacci Resource Trace')
plt.legend()
plt.tight_layout()
plt.savefig("chapters/fib_memprobe_plot.pdf")
print("[OK] Wrote fib_memprobe_plot.pdf")

