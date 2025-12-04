# tsp_compare.py
# Simple Traveling Salesperson-ish demo on 6 cities.
#
# Key idea about certainty:
# - If you want COMPLETE certainty you found the shortest tour,
#   you must explore all possible tours.
# - Number of tours grows ~ factorial:
#     Directed tours (start fixed): (n-1)!
#     Undirected/symmetric tours (start fixed, reverse is same): (n-1)! / 2
#   This explodes fast: n=10 -> (9)! = 362,880 tours; n=15 -> (14)! ~ 87 billion.

import random
import itertools
import math
import matplotlib.pyplot as plt


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
    """Pretty-print the distance matrix."""
    w = 4
    header = " " * w + "".join(f"{name:>{w}}" for name in names)
    print(header)
    for i, row in enumerate(dist):
        line = f"{names[i]:>{w}}" + "".join(f"{val:>{w}}" for val in row)
        print(line)


def tour_length(tour, dist):
    """Total length of a cyclic tour (returns to start). tour is a list of city indices."""
    total = 0
    n = len(tour)
    for k in range(n):
        a = tour[k]
        b = tour[(k + 1) % n]
        total += dist[a][b]
    return total


def random_guess_and_check(dist, iters=2000, seed=1):
    """
    Guess & check:
    - each iteration guesses a full random tour
    - checks its length
    - keeps the best length seen so far
    """
    rng = random.Random(seed)
    n = len(dist)
    best_len = float("inf")
    best_tour = None
    best_so_far = []

    cities = list(range(n))
    for _ in range(iters):
        rng.shuffle(cities)
        t = cities[:]  # copy
        L = tour_length(t, dist)
        if L < best_len:
            best_len = L
            best_tour = t
        best_so_far.append(best_len)

    return best_tour, best_len, best_so_far


def greedy_tour(dist, start, rng):
    """
    Greedy nearest-neighbor tour:
    - start at 'start'
    - repeatedly go to the nearest unvisited city (ties broken randomly)
    """
    n = len(dist)
    unvisited = set(range(n))
    unvisited.remove(start)
    tour = [start]
    current = start

    while unvisited:
        # find min distance among unvisited
        best_d = min(dist[current][j] for j in unvisited)
        candidates = [j for j in unvisited if dist[current][j] == best_d]
        nxt = rng.choice(candidates)  # break ties randomly
        tour.append(nxt)
        unvisited.remove(nxt)
        current = nxt

    return tour


def greedy_search(dist, iters=2000, seed=2):
    """
    To compare fairly with guess&check:
    - run greedy repeatedly from random start cities
    - keep best greedy tour found so far
    """
    rng = random.Random(seed)
    n = len(dist)

    best_len = float("inf")
    best_tour = None
    best_so_far = []

    for _ in range(iters):
        start = rng.randrange(n)
        t = greedy_tour(dist, start, rng)
        L = tour_length(t, dist)
        if L < best_len:
            best_len = L
            best_tour = t
        best_so_far.append(best_len)

    return best_tour, best_len, best_so_far


def brute_force_optimal(dist):
    """
    Exact solution (for certainty) by brute force:
    Fix start city = 0, permute remaining cities.
    Complexity: (n-1)! tours (with start fixed) -> fine for n=6.
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


def tours_count_info(n):
    # Start fixed (remove rotations)
    directed = math.factorial(n - 1)
    # Symmetric/undirected (reverse path is the same tour)
    undirected = directed // 2
    return directed, undirected


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
    print("  (This grows factorial-fast; brute force becomes impossible quickly.)")

    # Exact optimal (certainty)
    opt_tour, opt_len = brute_force_optimal(dist)
    print(f"\nExact optimal tour length (brute force): {opt_len}")
    print("  Tour:", " -> ".join(city_names[i] for i in opt_tour) + f" -> {city_names[opt_tour[0]]}")

    # Heuristics
    iters = 3000
    rg_tour, rg_len, rg_best = random_guess_and_check(dist, iters=iters, seed=1)
    gr_tour, gr_len, gr_best = greedy_search(dist, iters=iters, seed=2)

    print(f"\nGuess & Check best length after {iters} guesses: {rg_len}")
    print("  Tour:", " -> ".join(city_names[i] for i in rg_tour) + f" -> {city_names[rg_tour[0]]}")

    print(f"\nGreedy (multi-start) best length after {iters} starts: {gr_len}")
    print("  Tour:", " -> ".join(city_names[i] for i in gr_tour) + f" -> {city_names[gr_tour[0]]}")

    # Plot: best-so-far curves
    xs = list(range(1, iters + 1))
    plt.figure()
    plt.plot(xs, rg_best, label="Guess & Check (random tours)")
    plt.plot(xs, gr_best, label="Greedy (nearest neighbor, random starts)")
    plt.axhline(opt_len, linestyle="--", label="Optimal (brute force)")
    plt.title("Best-so-far Tour Length vs Iterations")
    plt.xlabel("Iteration")
    plt.ylabel("Best tour length found so far (lower is better)")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
