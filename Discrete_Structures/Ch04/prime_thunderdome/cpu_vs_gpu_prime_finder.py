#!/usr/bin/env python3
import numpy as np
import cupy as cp
import time, csv, argparse, os, sys
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
        print(f"⚙️ Testing up to {int(n):,} ...")
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
    with open(filename, "w"

