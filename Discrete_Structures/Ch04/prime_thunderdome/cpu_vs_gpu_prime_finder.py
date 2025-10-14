#!/usr/bin/env python3
import numpy as np
import cupy as cp
import time, csv, argparse, sys
import matplotlib.pyplot as plt

# --- PRIME FINDERS ---
def cpu_sieve(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = False
    return np.count_nonzero(sieve)

def gpu_sieve(n):
    sieve = cp.ones(n + 1, dtype=cp.bool_)
    sieve[:2] = False
    for i in range(2, int(cp.sqrt(n).get()) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = False
    return cp.count_nonzero(sieve)

# --- RUNNER ---
def run_benchmark(sizes, runs):
    results = []
    print("\n🏁 Entering the Prime Thunderdome...\n")

    for n in sizes:
        print(f"⚙️  Testing up to {int(n):,} ...")
        for r in range(1, runs + 1):
            # CPU
            t0 = time.time()
            cpu_count = cpu_sieve(int(n))
            cpu_time = time.time() - t0

            # GPU
            t0 = time.time()
            gpu_count = gpu_sieve(int(n))
            cp.cuda.Device().synchronize()
            gpu_time = time.time() - t0

            results.append({
                "range": int(n),
                "run": r,
                "cpu_primes": int(cpu_count),
                "cpu_time": round(cpu_time, 4),
                "gpu_primes": int(gpu_count.get() if hasattr(gpu_count, 'get') else gpu_count),
                "gpu_time": round(gpu_time, 4),
            })
            print(f"  Run {r}: CPU {cpu_time:.2f}s | GPU {gpu_time:.2f}s")

    return results

# --- CSV LOGGER ---
def save_results(results):
    filename = f"prime_race_results_{int(time.time())}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print(f"\n📄 Results saved to {filename}")
    return filename

# --- GRAPH MAKER ---
def plot_results(results, outfile="prime_race_plot.png"):
    sizes = sorted(set(r["range"] for r in results))
    cpu_avg = [np.mean([r["cpu_time"] for r in results if r["range"] == s]) for s in sizes]
    gpu_avg = [np.mean([r["gpu_time"] for r in results if r["range"] == s]) for s in sizes]

    plt.figure(figsize=(8,6))
    plt.plot(sizes, cpu_avg, marker='o', label="CPU", linewidth=2)
    plt.plot(sizes, gpu_avg, marker='o', label="GPU", linewidth=2)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Range (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Prime Finder: CPU vs GPU Showdown")
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig(outfile)
    print(f"📊 Plot saved to {outfile}")

# --- MAIN ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CPU vs GPU Prime Benchmark")
    parser.add_argument("--runs", type=int, default=3, help="Number of runs per size")
    parser.add_argument("--sizes", nargs="+", type=float, default=[1e6, 10e6, 50e6, 100e6],
                        help="List of max ranges to test")
    args = parser.parse_args()

    try:
        results = run_benchmark(args.sizes, args.runs)
        csv_file = save_results(results)
        plot_results(results)
        print("\n🏆 Benchmark complete! Check your CSV and plot for results.\n")
    except cp.cuda.runtime.CUDARuntimeError as e:
        print(f"❌ CUDA error: {e}")
        sys.exit(1)

