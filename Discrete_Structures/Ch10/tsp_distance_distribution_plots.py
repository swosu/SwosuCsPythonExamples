import random
import itertools
from collections import Counter
import math
import matplotlib.pyplot as plt


def make_distance_matrix(n, low=1, high=6, seed=123):
    """Symmetric n x n integer distances in [low..high], 0 diagonal."""
    rng = random.Random(seed)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = rng.randint(low, high)
            dist[i][j] = d
            dist[j][i] = d
    return dist


def tour_length(tour, dist):
    """Cycle length (returns to start). tour is a list of city indices."""
    total = 0
    n = len(tour)
    for k in range(n):
        a = tour[k]
        b = tour[(k + 1) % n]
        total += dist[a][b]
    return total


def dist_distribution_exact(n, dist):
    """
    Exact distribution over all tours with start fixed at 0.
    Total tours = (n-1)!.
    Returns: Counter(length -> count), total_count
    """
    start = 0
    counts = Counter()
    total = 0
    for perm in itertools.permutations(range(1, n)):
        tour = [start] + list(perm)
        L = tour_length(tour, dist)
        counts[L] += 1
        total += 1
    return counts, total


def dist_distribution_sampled(n, dist, samples=300_000, seed=999):
    """
    Sampled (Monte Carlo) distribution over random tours with start fixed at 0.
    Returns: Counter(length -> count), total_samples
    """
    rng = random.Random(seed)
    start = 0
    counts = Counter()
    cities = list(range(1, n))

    for _ in range(samples):
        rng.shuffle(cities)
        tour = [start] + cities[:]
        L = tour_length(tour, dist)
        counts[L] += 1

    return counts, samples


def counter_to_percent_series(counts, total, n):
    """
    Convert Counter of lengths to a full percent series over all possible integer lengths.
    Min length = n*1, max length = n*6 for this distance setup.
    """
    min_len = n * 1
    max_len = n * 6
    xs = list(range(min_len, max_len + 1))
    ys = [(counts.get(x, 0) / total) * 100.0 for x in xs]
    return xs, ys


def summarize_shape(counts, total):
    """Return (min_len, mode_len, median_len, min_pct, mode_pct)."""
    # min
    min_len = min(counts.keys())
    min_pct = 100.0 * counts[min_len] / total

    # mode
    mode_len, mode_count = max(counts.items(), key=lambda kv: kv[1])
    mode_pct = 100.0 * mode_count / total

    # median (expand lengths; ok for <=5040 exact, but for sampled we compute via cumulative)
    items = sorted(counts.items())  # (len, count)
    half = total / 2
    cum = 0
    median_len = items[-1][0]
    for L, c in items:
        cum += c
        if cum >= half:
            median_len = L
            break

    return min_len, mode_len, median_len, min_pct, mode_pct


def main():
    # City sizes requested
    sizes = [6, 8, 12]

    # For n=12, exact (11)! is huge; use sampling
    samples_for_12 = 400_000  # bump this up for smoother curves

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(11, 12), sharex=False)

    for ax, n in zip(axes, sizes):
        dist = make_distance_matrix(n, low=1, high=6, seed=123 + n)  # different but reproducible per n

        total_tours = math.factorial(n - 1)
        if n <= 8:
            counts, total = dist_distribution_exact(n, dist)
            label = f"n={n} (exact, total tours={total:,})"
        else:
            counts, total = dist_distribution_sampled(n, dist, samples=samples_for_12, seed=2025)
            label = f"n={n} (sampled, {total:,} tours out of {total_tours:,} total)"

        xs, ys = counter_to_percent_series(counts, total, n)

        min_len, mode_len, median_len, min_pct, mode_pct = summarize_shape(counts, total)

        ax.bar(xs, ys)  # no explicit colors
        ax.set_title(label)
        ax.set_xlabel("Tour distance")
        ax.set_ylabel("Percent of tours (%)")

        # Annotate key facts (shortest, mode, median)
        ax.text(
            0.01, 0.95,
            f"shortest={min_len} ({min_pct:.2f}%)\n"
            f"mode={mode_len} ({mode_pct:.2f}%)\n"
            f"median={median_len}",
            transform=ax.transAxes,
            va="top"
        )

    fig.suptitle("Distribution of Tour Distances (Start Fixed) for n=6, 8 (Exact) and n=12 (Sampled)", y=0.99)
    plt.tight_layout()
    plt.show()

    # Optional: save image
    # fig.savefig("tour_distance_distributions.png", dpi=200)


if __name__ == "__main__":
    main()
