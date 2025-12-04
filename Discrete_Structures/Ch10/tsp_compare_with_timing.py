# tsp_compare.py
# Traveling Salesperson-style demo for 6 cities.
#
# Includes:
#  1) Random Guess & Check (adaptive stopping)
#  2) Greedy nearest-neighbor (runs from EACH city; adaptive rounds)
#  3) Brute force (exact optimal; certainty)
#  4) Guess & Check + Simulated Annealing refinement
#  5) Greedy + Simulated Annealing refinement
#  6) Brute force result + Simulated Annealing (should not improve; sanity check)
#
# Note on "certainty" vs number of cities:
#  - If you want COMPLETE certainty you found the shortest tour by brute force,
#    you must evaluate all tours.
#  - With start fixed (removes rotations): (n-1)! tours (directed).
#  - If distances are symmetric and you treat reverse tours as identical:
#       (n-1)! / 2 tours
#  - Factorial growth is brutal. n=15 => (14)! ~ 8.7e10 tours (nope).

import random
import itertools
import math
import time
import matplotlib.pyplot as plt


# ----------------------------
# Distance table utilities
# ----------------------------

def make_distance_matrix(n=6, low=1, high=6, seed=123):
    """Create an n x n symmetric distance matrix with integer distances in [low..high]."""
    rng = random.Random(seed)
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            d = rng.randint(low, high)
            dist[i][j] = d
            dist[j][i] = d
    return dist


def print_distance_table(dist, names):
    w = 4
    header = " " * w + "".join(f"{name:>{w}}" for name in names)
    print(header)
    for i, row in enumerate(dist):
        line = f"{names[i]:>{w}}" + "".join(f"{val:>{w}}" for val in row)
        print(line)


def tour_length(tour, dist):
    """Total length of a cyclic tour (returns to start)."""
    total = 0
    n = len(tour)
    for k in range(n):
        a = tour[k]
        b = tour[(k + 1) % n]
        total += dist[a][b]
    return total


def format_tour(tour, names):
    return " -> ".join(names[i] for i in tour) + f" -> {names[tour[0]]}"


def tours_count_info(n):
    directed = math.factorial(n - 1)
    undirected = directed // 2
    return directed, undirected


# ----------------------------
# Adaptive stopping helper
# ----------------------------

def stop_when_stable(best_so_far, min_iters, patience):
    """
    Stop rule: after min_iters, stop if no improvement in the last `patience` steps.
    """
    if len(best_so_far) < min_iters:
        return False
    if patience <= 0:
        return False
    recent = best_so_far[-patience:]
    return min(recent) == recent[0]  # best hasn't improved during that window


# ----------------------------
# 1) Random Guess & Check (adaptive)
# ----------------------------

def random_guess_and_check_adaptive(dist, min_iters=200, max_iters=20000, patience=1500, seed=1):
    """
    Each iteration guesses a random full tour, keeps best-so-far.
    Stops when best hasn't improved for `patience` iterations (after min_iters),
    or max_iters reached.
    """
    rng = random.Random(seed)
    n = len(dist)

    best_len = float("inf")
    best_tour = None
    best_so_far = []

    base = list(range(n))
    for _ in range(max_iters):
        rng.shuffle(base)
        t = base[:]
        L = tour_length(t, dist)
        if L < best_len:
            best_len = L
            best_tour = t
        best_so_far.append(best_len)

        if stop_when_stable(best_so_far, min_iters=min_iters, patience=patience):
            break

    return best_tour, best_len, best_so_far


# ----------------------------
# 2) Greedy nearest neighbor (run from EACH city)
# ----------------------------

def greedy_tour(dist, start, rng):
    """
    Greedy nearest-neighbor tour:
    repeatedly go to nearest unvisited (ties broken randomly).
    """
    n = len(dist)
    unvisited = set(range(n))
    unvisited.remove(start)

    tour = [start]
    current = start

    while unvisited:
        best_d = min(dist[current][j] for j in unvisited)
        candidates = [j for j in unvisited if dist[current][j] == best_d]
        nxt = rng.choice(candidates)  # randomness only used for ties
        tour.append(nxt)
        unvisited.remove(nxt)
        current = nxt

    return tour


def greedy_all_starts_once(dist, seed=2):
    """
    Runs greedy from each start city exactly once.
    Returns the best tour among those n runs, and a per-run list of results.
    """
    rng = random.Random(seed)
    n = len(dist)

    best_len = float("inf")
    best_tour = None
    per_start = []

    for s in range(n):
        t = greedy_tour(dist, s, rng)
        L = tour_length(t, dist)
        per_start.append((s, t, L))
        if L < best_len:
            best_len = L
            best_tour = t

    return best_tour, best_len, per_start


def greedy_adaptive_rounds(dist, min_rounds=1, max_rounds=2000, patience_rounds=100, seed=2):
    """
    A "round" = run greedy from EACH start city (so at least 6 tours per round).
    We keep best-so-far across rounds and stop when best doesn't improve for a while.
    """
    rng = random.Random(seed)
    n = len(dist)

    best_len = float("inf")
    best_tour = None
    best_so_far = []
    rounds = 0

    for _ in range(max_rounds):
        rounds += 1
        # Run all starts this round (tie randomness can produce different tours)
        for s in range(n):
            t = greedy_tour(dist, s, rng)
            L = tour_length(t, dist)
            if L < best_len:
                best_len = L
                best_tour = t

        best_so_far.append(best_len)

        # Adaptive stopping checks improvement across rounds
        if rounds >= min_rounds and stop_when_stable(best_so_far, min_iters=min_rounds, patience=patience_rounds):
            break

    # Expand the "round best-so-far" into a per-evaluation-ish curve (optional).
    # For plotting, we'll keep the round curve; it's cleaner.
    return best_tour, best_len, best_so_far


# ----------------------------
# 3) Brute force (exact)
# ----------------------------

def brute_force_optimal(dist):
    """
    Exact optimal solution (certainty) by brute force.
    Fix start city = 0, permute remaining cities -> (n-1)! tours.
    """
    n = len(dist)
    start = 0
    best_len = float("inf")
    best_tour = None

    for perm in itertools.permutations(range(1, n)):
        t = [start] + list(perm)
        L = tour_length(t, dist)
        if L < best_len:
            best_len = L
            best_tour = t

    return best_tour, best_len


# ----------------------------
# Simulated Annealing (SA)
# ----------------------------

def two_opt_neighbor(tour, rng):
    """
    Make a neighbor tour by reversing a segment (2-opt style move).
    Keeps it a valid permutation.
    """
    n = len(tour)
    i, j = sorted(rng.sample(range(n), 2))
    if i == 0 and j == n - 1:
        # reversing whole tour is basically the same cycle; pick another move
        i, j = 1, n - 2
    new_t = tour[:]
    new_t[i:j+1] = reversed(new_t[i:j+1])
    return new_t


def simulated_annealing(dist, start_tour, seed=99,
                        max_steps=20000,
                        initial_temp=None, alpha=0.995, min_temp=1e-4,
                        patience=3000):
    """
    Simulated annealing:
    - Start from start_tour
    - Propose neighbor tours via 2-opt-like segment reversal
    - Accept if better; sometimes accept worse with probability exp(-delta/T)
    - Cool temperature each step

    Stops when temperature is tiny OR best hasn't improved for `patience` steps.
    Returns best tour found and best-so-far curve (per step).
    """
    rng = random.Random(seed)
    n = len(dist)

    # Set a reasonable default temperature based on typical edge weights.
    if initial_temp is None:
        # mean of off-diagonal distances * n is a decent "scale"
        vals = [dist[i][j] for i in range(n) for j in range(n) if i != j]
        mean_d = sum(vals) / len(vals)
        initial_temp = mean_d * n

    current = start_tour[:]
    current_len = tour_length(current, dist)

    best = current[:]
    best_len = current_len

    T = float(initial_temp)
    best_so_far = []
    steps_since_improve = 0

    for _ in range(max_steps):
        neighbor = two_opt_neighbor(current, rng)
        neigh_len = tour_length(neighbor, dist)
        delta = neigh_len - current_len  # positive means worse

        accept = False
        if delta <= 0:
            accept = True
        else:
            # accept worse sometimes
            p = math.exp(-delta / T) if T > 0 else 0.0
            if rng.random() < p:
                accept = True

        if accept:
            current = neighbor
            current_len = neigh_len

        if current_len < best_len:
            best = current[:]
            best_len = current_len
            steps_since_improve = 0
        else:
            steps_since_improve += 1

        best_so_far.append(best_len)

        T *= alpha
        if T < min_temp:
            break
        if steps_since_improve >= patience:
            break

    return best, best_len, best_so_far


# ----------------------------
# Timing wrapper
# ----------------------------

def timed(label, fn, *args, **kwargs):
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return out, (t1 - t0), label


# ----------------------------
# Main
# ----------------------------

def main():
    n = 6
    city_names = ["A", "B", "C", "D", "E", "F"]
    dist = make_distance_matrix(n=n, low=1, high=6, seed=123)

    print("\nDistance table (integers 1..6, symmetric):")
    print_distance_table(dist, city_names)

    directed, undirected = tours_count_info(n)
    print("\nHow number of cities impacts certainty (tours to fully check):")
    print(f"  n={n}")
    print(f"  Directed tours w/ fixed start: (n-1)! = {directed}")
    print(f"  Symmetric tours w/ fixed start: (n-1)!/2 = {undirected}")
    print("  Factorial growth example (directed, start fixed):")
    for k in [6, 8, 10, 12, 15]:
        print(f"    n={k:>2} -> (n-1)! = {math.factorial(k-1):,}")

    # ---- Brute force (exact) ----
    (opt_tour, opt_len), t_bf, _ = timed("Brute force (exact)", brute_force_optimal, dist)
    print(f"\nExact optimal tour length (brute force): {opt_len}")
    print("  Tour:", format_tour(opt_tour, city_names))
    print(f"  Time: {t_bf*1000:.3f} ms")

    # ---- Random Guess & Check (adaptive) ----
    (rg_tour, rg_len, rg_curve), t_rg, _ = timed(
        "Guess & Check (adaptive)",
        random_guess_and_check_adaptive,
        dist,
        200,      # min_iters
        20000,    # max_iters
        1500,     # patience
        1         # seed
    )
    print(f"\nGuess & Check best length: {rg_len}  (iters={len(rg_curve)})")
    print("  Tour:", format_tour(rg_tour, city_names))
    print(f"  Time: {t_rg*1000:.3f} ms")

    # ---- Greedy from EACH city (adaptive rounds) ----
    # This guarantees at least 6 greedy runs per round.
    (gr_tour, gr_len, gr_round_curve), t_gr, _ = timed(
        "Greedy (all starts, adaptive rounds)",
        greedy_adaptive_rounds,
        dist,
        1,     # min_rounds
        2000,  # max_rounds
        100,   # patience_rounds
        2      # seed
    )
    print(f"\nGreedy best length: {gr_len}  (rounds={len(gr_round_curve)}; greedy-runs={len(gr_round_curve)*n})")
    print("  Tour:", format_tour(gr_tour, city_names))
    print(f"  Time: {t_gr*1000:.3f} ms")

    # ---- Annealing refinements (Simulated Annealing) ----
    # NOTE: Simulated annealing is NOT substring search; it’s a probabilistic optimization technique.

    (rg_sa_tour, rg_sa_len, rg_sa_curve), t_rg_sa, _ = timed(
        "Guess&Check + SA",
        simulated_annealing,
        dist,
        rg_tour,
        101,      # seed
        20000,    # max_steps
        None,     # initial_temp auto
        0.995,    # alpha
        1e-4,     # min_temp
        3000      # patience
    )
    print(f"\nGuess&Check + SA best length: {rg_sa_len} (steps={len(rg_sa_curve)})")
    print("  Tour:", format_tour(rg_sa_tour, city_names))
    print(f"  Time: {t_rg_sa*1000:.3f} ms")

    (gr_sa_tour, gr_sa_len, gr_sa_curve), t_gr_sa, _ = timed(
        "Greedy + SA",
        simulated_annealing,
        dist,
        gr_tour,
        202,      # seed
        20000,
        None,
        0.995,
        1e-4,
        3000
    )
    print(f"\nGreedy + SA best length: {gr_sa_len} (steps={len(gr_sa_curve)})")
    print("  Tour:", format_tour(gr_sa_tour, city_names))
    print(f"  Time: {t_gr_sa*1000:.3f} ms")

    # Brute force is already optimal; SA from optimal is a "can it get better?" sanity test.
    (bf_sa_tour, bf_sa_len, bf_sa_curve), t_bf_sa, _ = timed(
        "Brute force + SA (sanity check)",
        simulated_annealing,
        dist,
        opt_tour,
        303,
        20000,
        None,
        0.995,
        1e-4,
        3000
    )
    print(f"\nBrute force + SA best length: {bf_sa_len} (steps={len(bf_sa_curve)})")
    print("  Tour:", format_tour(bf_sa_tour, city_names))
    print(f"  Time: {t_bf_sa*1000:.3f} ms")

    # ---- Summary timing table ----
    print("\nTiming summary:")
    rows = [
        ("Brute force (exact)", t_bf),
        ("Guess & Check (adaptive)", t_rg),
        ("Greedy (all starts, adaptive rounds)", t_gr),
        ("Guess&Check + SA", t_rg_sa),
        ("Greedy + SA", t_gr_sa),
        ("Brute force + SA (sanity check)", t_bf_sa),
    ]
    for name, sec in rows:
        print(f"  {name:<38} {sec*1000:>10.3f} ms")

    # ---- Plot comparisons ----
    plt.figure()

    # Two “base” curves
    plt.plot(range(1, len(rg_curve) + 1), rg_curve, label="Guess & Check (best-so-far)")
    plt.plot(range(1, len(gr_round_curve) + 1), gr_round_curve, label="Greedy (best per round)")

    # Annealing curves
    plt.plot(range(1, len(rg_sa_curve) + 1), rg_sa_curve, label="Guess&Check + SA (best-so-far)")
    plt.plot(range(1, len(gr_sa_curve) + 1), gr_sa_curve, label="Greedy + SA (best-so-far)")

    # Optimal line
    plt.axhline(opt_len, linestyle="--", label="Optimal (brute force)")

    plt.title("Tour Quality vs Effort (Adaptive Methods + Annealing)")
    plt.xlabel("Iteration / Round / SA step")
    plt.ylabel("Best tour length found so far (lower is better)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
