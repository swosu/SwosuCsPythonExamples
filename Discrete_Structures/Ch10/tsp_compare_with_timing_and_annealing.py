# tsp_compare_with_timing.py
# Traveling Salesperson-style demo for 6 cities.
#
# Includes (9 total outputs):
#  1) Random Guess & Check (adaptive stopping)
#  2) Greedy nearest-neighbor (runs from EACH city; adaptive rounds)
#  3) Brute force (exact optimal; certainty)
#  4) Guess & Check + Simulated Annealing (2-opt neighbor)
#  5) Greedy + Simulated Annealing (2-opt neighbor)
#  6) Brute force result + Simulated Annealing (2-opt neighbor)  [sanity check]
#  7) Guess & Check + Simulated Annealing (3-city swap/permutation neighbor)
#  8) Greedy + Simulated Annealing (3-city swap/permutation neighbor)
#  9) Brute force result + Simulated Annealing (3-city neighbor) [sanity check]
#
# Brute force also prints:
#  - Sorted table of all 120 tours by distance
#  - Summary table: distance -> count, percent
#  - Shortest-path frequency and "longer vs shorter" comparison
#
# Certainty vs number of cities:
#  - With start fixed (removes rotations): (n-1)! tours (directed).
#  - If symmetric and reverse considered same: (n-1)! / 2 tours
#  - Factorial growth is brutal.

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


def greedy_adaptive_rounds(dist, min_rounds=1, max_rounds=2000, patience_rounds=100, seed=2):
    """
    A "round" = run greedy from EACH start city (so at least 6 tours per round).
    Keep best-so-far across rounds; stop when best doesn't improve for patience_rounds.
    """
    rng = random.Random(seed)
    n = len(dist)

    best_len = float("inf")
    best_tour = None
    best_per_round = []
    rounds = 0

    for _ in range(max_rounds):
        rounds += 1
        for s in range(n):
            t = greedy_tour(dist, s, rng)
            L = tour_length(t, dist)
            if L < best_len:
                best_len = L
                best_tour = t

        best_per_round.append(best_len)

        if rounds >= min_rounds and stop_when_stable(best_per_round, min_iters=min_rounds, patience=patience_rounds):
            break

    return best_tour, best_len, best_per_round


# ----------------------------
# 3) Brute force (exact) + distribution tables
# ----------------------------

def brute_force_optimal(dist):
    """
    Exact optimal (certainty) by brute force.
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


def brute_force_all_tours_sorted(dist):
    """
    Return all tours (start fixed at 0) as a list sorted by length:
      [(length, tour), ...]
    Total = (n-1)! tours.
    """
    n = len(dist)
    start = 0
    tours = []
    for perm in itertools.permutations(range(1, n)):
        t = [start] + list(perm)
        L = tour_length(t, dist)
        tours.append((L, t))
    tours.sort(key=lambda x: x[0])
    return tours


def print_bruteforce_tables(sorted_tours, names):
    """
    Prints:
    1) Full sorted list of tours by distance
    2) Summary distribution: distance -> count and percent
    3) Answers:
       - How many shortest tours?
       - What % are shortest?
       - Are longer paths more common than shorter?
    """
    total = len(sorted_tours)
    best_len = sorted_tours[0][0]

    # Count length frequencies
    counts = {}
    for L, _ in sorted_tours:
        counts[L] = counts.get(L, 0) + 1

    # Sorted by length
    unique_lengths = sorted(counts.keys())

    print("\nBrute force: all tours sorted by distance (start fixed at A)")
    print(f"  Total tours: {total}")
    print("  Rank | Distance | Tour")
    print("  ---- | -------- | ----")
    for idx, (L, t) in enumerate(sorted_tours, start=1):
        print(f"  {idx:>4} | {L:>8} | {format_tour(t, names)}")

    print("\nSummary: distance distribution across all tours")
    print("  Distance | Count | Percent")
    print("  -------- | ----- | -------")
    for L in unique_lengths:
        c = counts[L]
        pct = 100.0 * c / total
        print(f"  {L:>8} | {c:>5} | {pct:>6.2f}%")

    shortest_count = counts[best_len]
    shortest_pct = 100.0 * shortest_count / total

    # Compare "short" vs "long" in a concrete way:
    # We'll define "shorter" as <= median length and "longer" as > median length.
    lengths_expanded = []
    for L in unique_lengths:
        lengths_expanded.extend([L] * counts[L])
    lengths_expanded.sort()
    median_len = lengths_expanded[len(lengths_expanded) // 2]

    shorter_or_equal = sum(c for L, c in counts.items() if L <= median_len)
    longer = total - shorter_or_equal

    # Also: what's the single most common length?
    mode_len = max(counts.items(), key=lambda kv: kv[1])[0]
    mode_count = counts[mode_len]
    mode_pct = 100.0 * mode_count / total

    print("\nAnswers from this exact distribution:")
    print(f"  Shortest tour distance: {best_len}")
    print(f"  Number of shortest tours: {shortest_count} out of {total}")
    print(f"  Percent of tours that are shortest: {shortest_pct:.2f}%")
    print(f"  Most common distance (mode): {mode_len}  ({mode_count} tours = {mode_pct:.2f}%)")
    print(f"  Median distance: {median_len}")
    if longer > shorter_or_equal:
        print(f"  Longer-than-median tours are more common: {longer} vs {shorter_or_equal}")
    elif longer < shorter_or_equal:
        print(f"  Shorter-or-equal-to-median tours are more common: {shorter_or_equal} vs {longer}")
    else:
        print(f"  Perfect tie: longer {longer} == shorter/equal {shorter_or_equal}")


# ----------------------------
# Simulated Annealing (SA)
#   We'll support multiple neighbor "move sizes":
#     - 2-opt style segment reversal (uses two cut points)
#     - 3-city permutation (switch three cities at a time)
# ----------------------------

def neighbor_two_opt(tour, rng):
    """
    2-opt-ish neighbor:
    reverse a subsequence between two indices.
    """
    n = len(tour)
    i, j = sorted(rng.sample(range(n), 2))
    if i == j:
        return tour[:]
    # Avoid reversing the entire cycle as a no-op-ish move
    if i == 0 and j == n - 1:
        i, j = 1, n - 2
    new_t = tour[:]
    new_t[i:j+1] = reversed(new_t[i:j+1])
    return new_t


def neighbor_three_city_permute(tour, rng):
    """
    "3-city switch" neighbor:
    pick 3 positions and permute the cities in those positions.
    This changes three cities at once (instead of a 2-city swap).
    """
    n = len(tour)
    a, b, c = sorted(rng.sample(range(n), 3))
    new_t = tour[:]

    # Grab the three cities
    x, y, z = new_t[a], new_t[b], new_t[c]

    # Choose one of the 5 non-identity permutations
    perms = [
        (x, z, y),
        (y, x, z),
        (y, z, x),
        (z, x, y),
        (z, y, x),
    ]
    px, py, pz = rng.choice(perms)

    new_t[a], new_t[b], new_t[c] = px, py, pz
    return new_t


def simulated_annealing(dist, start_tour, seed=99,
                        max_steps=20000,
                        neighbor_fn=neighbor_two_opt,
                        initial_temp=None, alpha=0.995, min_temp=1e-4,
                        patience=3000):
    """
    Simulated annealing:
    - Start from start_tour
    - Propose neighbor tours using neighbor_fn
    - Accept if better; sometimes accept worse with probability exp(-delta/T)
    - Cool temperature each step
    - Stop when temperature tiny OR best hasn't improved for patience steps.
    """
    rng = random.Random(seed)
    n = len(dist)

    # Default temperature based on typical edge weights
    if initial_temp is None:
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
        neighbor = neighbor_fn(current, rng)
        neigh_len = tour_length(neighbor, dist)
        delta = neigh_len - current_len

        if delta <= 0:
            accept = True
        else:
            accept = (rng.random() < (math.exp(-delta / T) if T > 0 else 0.0))

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

def timed(fn, *args, **kwargs):
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    t1 = time.perf_counter()
    return out, (t1 - t0)


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

    # ---- Brute force (exact) + full sorted tour table + summary distribution ----
    (opt_tour, opt_len), t_bf = timed(brute_force_optimal, dist)
    print(f"\nExact optimal tour length (brute force): {opt_len}")
    print("  Tour:", format_tour(opt_tour, city_names))
    print(f"  Time: {t_bf*1000:.3f} ms")

    (sorted_tours), t_list = timed(brute_force_all_tours_sorted, dist)
    print(f"\nBrute force enumeration time (building + sorting all tours): {t_list*1000:.3f} ms")
    print_bruteforce_tables(sorted_tours, city_names)

    # ---- Random Guess & Check (adaptive) ----
    (rg_tour, rg_len, rg_curve), t_rg = timed(
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
    (gr_tour, gr_len, gr_round_curve), t_gr = timed(
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

    # ---- Annealing refinements: 2-opt neighbor ----
    (rg_sa2_tour, rg_sa2_len, rg_sa2_curve), t_rg_sa2 = timed(
        simulated_annealing,
        dist, rg_tour,
        101,     # seed
        20000,   # max_steps
        neighbor_two_opt,
        None, 0.995, 1e-4, 3000
    )

    (gr_sa2_tour, gr_sa2_len, gr_sa2_curve), t_gr_sa2 = timed(
        simulated_annealing,
        dist, gr_tour,
        202,
        20000,
        neighbor_two_opt,
        None, 0.995, 1e-4, 3000
    )

    (bf_sa2_tour, bf_sa2_len, bf_sa2_curve), t_bf_sa2 = timed(
        simulated_annealing,
        dist, opt_tour,
        303,
        20000,
        neighbor_two_opt,
        None, 0.995, 1e-4, 3000
    )

    print(f"\nGuess&Check + SA(2-opt) best length: {rg_sa2_len} (steps={len(rg_sa2_curve)})")
    print("  Tour:", format_tour(rg_sa2_tour, city_names))
    print(f"  Time: {t_rg_sa2*1000:.3f} ms")

    print(f"\nGreedy + SA(2-opt) best length: {gr_sa2_len} (steps={len(gr_sa2_curve)})")
    print("  Tour:", format_tour(gr_sa2_tour, city_names))
    print(f"  Time: {t_gr_sa2*1000:.3f} ms")

    print(f"\nBrute force + SA(2-opt) best length: {bf_sa2_len} (steps={len(bf_sa2_curve)})")
    print("  Tour:", format_tour(bf_sa2_tour, city_names))
    print(f"  Time: {t_bf_sa2*1000:.3f} ms")

    # ---- Annealing refinements: 3-city neighbor (your new request) ----
    (rg_sa3_tour, rg_sa3_len, rg_sa3_curve), t_rg_sa3 = timed(
        simulated_annealing,
        dist, rg_tour,
        111,     # seed
        20000,
        neighbor_three_city_permute,
        None, 0.995, 1e-4, 3000
    )

    (gr_sa3_tour, gr_sa3_len, gr_sa3_curve), t_gr_sa3 = timed(
        simulated_annealing,
        dist, gr_tour,
        222,
        20000,
        neighbor_three_city_permute,
        None, 0.995, 1e-4, 3000
    )

    (bf_sa3_tour, bf_sa3_len, bf_sa3_curve), t_bf_sa3 = timed(
        simulated_annealing,
        dist, opt_tour,
        333,
        20000,
        neighbor_three_city_permute,
        None, 0.995, 1e-4, 3000
    )

    print(f"\nGuess&Check + SA(3-city) best length: {rg_sa3_len} (steps={len(rg_sa3_curve)})")
    print("  Tour:", format_tour(rg_sa3_tour, city_names))
    print(f"  Time: {t_rg_sa3*1000:.3f} ms")

    print(f"\nGreedy + SA(3-city) best length: {gr_sa3_len} (steps={len(gr_sa3_curve)})")
    print("  Tour:", format_tour(gr_sa3_tour, city_names))
    print(f"  Time: {t_gr_sa3*1000:.3f} ms")

    print(f"\nBrute force + SA(3-city) best length: {bf_sa3_len} (steps={len(bf_sa3_curve)})")
    print("  Tour:", format_tour(bf_sa3_tour, city_names))
    print(f"  Time: {t_bf_sa3*1000:.3f} ms")

    # ---- Timing summary ----
    print("\nTiming summary:")
    rows = [
        ("Brute force (exact)", t_bf),
        ("Brute force enumerate+sort (all tours)", t_list),
        ("Guess & Check (adaptive)", t_rg),
        ("Greedy (all starts, adaptive rounds)", t_gr),
        ("Guess&Check + SA(2-opt)", t_rg_sa2),
        ("Greedy + SA(2-opt)", t_gr_sa2),
        ("Brute force + SA(2-opt)", t_bf_sa2),
        ("Guess&Check + SA(3-city)", t_rg_sa3),
        ("Greedy + SA(3-city)", t_gr_sa3),
        ("Brute force + SA(3-city)", t_bf_sa3),
    ]
    for name, sec in rows:
        print(f"  {name:<40} {sec*1000:>10.3f} ms")

    # ---- Graphs ----
    # Figure 1: Base methods vs optimal
    plt.figure()
    plt.plot(range(1, len(rg_curve) + 1), rg_curve, label="Guess & Check (best-so-far)")
    plt.plot(range(1, len(gr_round_curve) + 1), gr_round_curve, label="Greedy (best per round)")
    plt.axhline(opt_len, linestyle="--", label="Optimal (brute force)")
    plt.title("Base Methods: Tour Quality vs Effort")
    plt.xlabel("Iteration / Round")
    plt.ylabel("Best tour length found so far (lower is better)")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Figure 2: Annealing move comparison (2-opt vs 3-city)
    plt.figure()
    plt.plot(range(1, len(rg_sa2_curve) + 1), rg_sa2_curve, label="G&C + SA (2-opt)")
    plt.plot(range(1, len(rg_sa3_curve) + 1), rg_sa3_curve, label="G&C + SA (3-city)")
    plt.plot(range(1, len(gr_sa2_curve) + 1), gr_sa2_curve, label="Greedy + SA (2-opt)")
    plt.plot(range(1, len(gr_sa3_curve) + 1), gr_sa3_curve, label="Greedy + SA (3-city)")
    plt.axhline(opt_len, linestyle="--", label="Optimal (brute force)")
    plt.title("Annealing: 2-opt vs 3-city Moves")
    plt.xlabel("SA Step")
    plt.ylabel("Best tour length found so far (lower is better)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
