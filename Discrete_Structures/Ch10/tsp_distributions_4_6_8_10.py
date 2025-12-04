import itertools
import math
import time
from collections import Counter

import matplotlib.pyplot as plt


def make_distance_matrix(n, low=1, high=6, seed=123):
    """Symmetric n x n matrix with integer distances in [low..high], diagonal 0."""
    import random
    rng = random.Random(seed)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = rng.randint(low, high)
            dist[i][j] = d
            dist[j][i] = d
    return dist


def brute_force_distribution(dist):
    """
    Exact distribution over ALL tours with start fixed at 0.
    Total tours = (n-1)!.
    Returns:
      counts: Counter(length -> count)
      best_len: shortest length found
      best_count: how many tours have that shortest length
      total: number of tours enumerated
      elapsed_sec: timing
    """
    n = len(dist)
    start = 0
    D = dist  # local for speed

    t0 = time.perf_counter()

    counts = Counter()
    best_len = float("inf")

    # perm is a tuple of cities [1..n-1] in some order
    for perm in itertools.permutations(range(1, n)):
        # Fast length compute without building a full tour list:
        # length = D[0][perm0] + sum D[perm[i]][perm[i+1]] + D[perm_last][0]
        L = D[start][perm[0]]
        for i in range(n - 2):
            L += D[perm[i]][perm[i + 1]]
        L += D[perm[-1]][start]

        counts[L] += 1
        if L < best_len:
            best_len = L

    elapsed = time.perf_counter() - t0
    total = math.factorial(n - 1)
    best_count = counts[best_len]
    return counts, best_len, best_count, total, elapsed


def distribution_table(counts, total, n):
    """Build a full (distance -> count, percent) table for distances n..6n."""
    min_len = n * 1
    max_len = n * 6
    rows = []
    for L in range(min_len, max_len + 1):
        c = counts.get(L, 0)
        pct = (c / total) * 100.0
        rows.append((L, c, pct))
    return rows


def print_distribution_table(rows, n, best_len, best_count, total):
    print(f"\nSummary table for n={n} (start fixed; total tours={(total):,}):")
    print("  Distance | Count | Percent")
    print("  -------- | ----- | -------")
    for L, c, pct in rows:
        if c != 0:
            star = "  <-- shortest" if L == best_len else ""
            print(f"  {L:>8} | {c:>5} | {pct:>6.2f}%{star}")

    best_pct = (best_count / total) * 100.0
    print(f"\n  Shortest distance = {best_len}")
    print(f"  # shortest tours   = {best_count} / {total:,}  ({best_pct:.2f}%)")


def plot_distribution(ax, rows, n, title_suffix=""):
    xs = [L for (L, _, _) in rows]
    ys = [pct for (_, _, pct) in rows]
    ax.bar(xs, ys)
    ax.set_title(f"n={n} distance distribution {title_suffix}".strip())
    ax.set_xlabel("Tour distance")
    ax.set_ylabel("Percent of tours (%)")


def main():
    sizes = [4, 6, 8, 10]

    results = {}   # n -> dict with counts, tables, timing, etc.
    timing_rows = []

    for n in sizes:
        dist = make_distance_matrix(n, low=1, high=6, seed=123 + n)
        counts, best_len, best_count, total, elapsed = brute_force_distribution(dist)
        rows = distribution_table(counts, total, n)

        results[n] = {
            "counts": counts,
            "best_len": best_len,
            "best_count": best_count,
            "total": total,
            "elapsed": elapsed,
            "rows": rows,
        }

        timing_rows.append((n, total, elapsed, (elapsed / total) * 1e6))

        # Print per-n table (so you can talk about exact numbers)
        print_distribution_table(rows, n, best_len, best_count, total)
        print(f"  Brute force time   = {elapsed:.3f} sec")
        print(f"  Time per tour      = {(elapsed / total) * 1e6:.2f} µs")

    # Timing overview table
    print("\n\nTiming overview (exact brute force):")
    print("  n | tours (start fixed) | total time (sec) | µs per tour")
    print("  - | ------------------- | --------------- | ----------")
    for n, total, elapsed, us_per in timing_rows:
        print(f"  {n:>1} | {total:>19,} | {elapsed:>15.3f} | {us_per:>10.2f}")

    # -------- Plots --------
    # Figure 1: stacked 3 graphs for n=4,6,8 (as requested)
    fig1, axes = plt.subplots(nrows=3, ncols=1, figsize=(11, 12))
    for ax, n in zip(axes, [4, 6, 8]):
        plot_distribution(ax, results[n]["rows"], n)
    fig1.suptitle("Tour Distance Distributions (Exact brute force) — n=4,6,8", y=0.99)
    plt.tight_layout()
    plt.show()

    # Figure 2: n=10 by itself (still exact, but bigger)
    fig2, ax2 = plt.subplots(nrows=1, ncols=1, figsize=(11, 4))
    plot_distribution(ax2, results[10]["rows"], 10, title_suffix="(exact)")
    fig2.suptitle("Tour Distance Distribution — n=10 (Exact brute force)", y=0.98)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
