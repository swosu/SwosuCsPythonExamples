#!/usr/bin/env python3
"""
seating_permutations_with_tests.py

Explore permutations of friends in a row of chairs.

Rules so far:

Step 1:
- Count all seatings (n! total).

Step 2 (Amina Drama):
- Seatings with Amina at the front.
- Seatings with Amina at the back.
- Seatings where Amina is stuck in the middle (not allowed now).

Step 3 (Lin–Zahra together):
- Choose two friends (Lin and Zahra) and count only the seatings
  where they sit in adjacent seats.
- Also list which seatings *do not* have them together.
"""

import itertools
import math
import unittest


# ---------- Core permutation helpers ----------

def generate_permutations(items):
    """
    Return a list of all permutations (orderings) of the given items.
    """
    return list(itertools.permutations(items))


def count_permutations(items):
    """
    Return the number of permutations of the given list of items.
    """
    return len(generate_permutations(items))


def expected_permutation_count(items):
    """
    Return n! where n = len(items).
    """
    return math.factorial(len(items))


# ---------- "fixed person at ends" helpers (Amina Drama) ----------

def permutations_with_person_first(items, person):
    """
    Return all permutations where `person` is in the FIRST position.
    """
    return [p for p in generate_permutations(items) if p[0] == person]


def permutations_with_person_last(items, person):
    """
    Return all permutations where `person` is in the LAST position.
    """
    return [p for p in generate_permutations(items) if p[-1] == person]


def permutations_with_person_not_at_ends(items, person):
    """
    Return all permutations where `person` is NOT in the first or last position.

    This is the "Amina Drama" set: seatings that no longer work
    because the VIP refuses to sit in the middle.
    """
    return [
        p for p in generate_permutations(items)
        if person in p and p[0] != person and p[-1] != person
    ]


def count_with_person_first(items, person):
    return len(permutations_with_person_first(items, person))


def count_with_person_last(items, person):
    return len(permutations_with_person_last(items, person))


def count_with_person_first_or_last(items, person):
    perms = generate_permutations(items)
    return sum(1 for p in perms if p[0] == person or p[-1] == person)


def expected_person_fixed_first_or_last(items):
    """
    Expected count of seatings where some distinguished person
    is in the first OR last seat.

    For n >= 2:
        - First seat fixed: (n-1)! ways
        - Last seat fixed:  (n-1)! ways
        => Total = 2 * (n-1)!.

    For n = 1: exactly 1 seating.
    For n = 0: 0 seatings.
    """
    n = len(items)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * math.factorial(n - 1)


# ---------- NEW: "two friends sit together" helpers (Lin & Zahra) ----------

def are_adjacent(seating, a, b):
    """
    Return True if a and b sit in adjacent chairs (either order) in this seating.
    """
    try:
        i = seating.index(a)
        j = seating.index(b)
    except ValueError:
        # One or both not present
        return False
    return abs(i - j) == 1


def permutations_with_pair_adjacent(items, a, b):
    """
    Return all permutations where `a` and `b` sit in adjacent seats.
    """
    return [
        p for p in generate_permutations(items)
        if are_adjacent(p, a, b)
    ]


def permutations_without_pair_adjacent(items, a, b):
    """
    Return all permutations where `a` and `b` are NOT adjacent.
    """
    return [
        p for p in generate_permutations(items)
        if not are_adjacent(p, a, b)
    ]


def count_with_pair_adjacent(items, a, b):
    """
    Number of permutations where `a` and `b` are adjacent.
    """
    return len(permutations_with_pair_adjacent(items, a, b))


def expected_pair_adjacent_count(items):
    """
    Expected count of permutations where two distinguished friends
    (say, Lin and Zahra) sit together in a row of chairs.

    Math rule:
        Treat the two friends as a single "block". Now there are (n-1)
        objects to arrange (the block + the other n-2 people).
        => (n-1)! ways to arrange the blocks

        Inside the block, the two friends can be in 2! orders.
        => multiply by 2.

        Total = 2 * (n-1)! for n >= 2.

    For n < 2, there aren't two distinct friends to be adjacent.
    """
    n = len(items)
    if n < 2:
        return 0
    return 2 * math.factorial(n - 1)


# ---------- Demo / main program ----------

def main():
    """
    Demo showing:
    - All seatings.
    - Amina-at-ends breakdown.
    - Lin–Zahra adjacency breakdown, with printouts showing
      which permutations "still work" and which "fall away".
    """
    friends = ["Amina", "Lin", "Zahra", "Jake"]
    vip = "Amina"
    pair_a, pair_b = "Lin", "Zahra"

    n = len(friends)
    all_perms = generate_permutations(friends)

    print("Friends:", friends)
    print("\n=== All permutations ===")
    for p in all_perms:
        print("  ", p)
    print(f"Total seatings: {len(all_perms)} (should be {math.factorial(n)} = {n}!)")

    # ---------- Amina Drama (Step 2) ----------
    front_perms = permutations_with_person_first(friends, vip)
    back_perms = permutations_with_person_last(friends, vip)
    drama_perms = permutations_with_person_not_at_ends(friends, vip)

    print(f"\n=== Seatings with {vip} at the FRONT ===")
    for p in front_perms:
        print("  ", p)
    print(f"Count: {len(front_perms)} (formula (n-1)! = {math.factorial(n - 1)})")

    print(f"\n=== Seatings with {vip} at the BACK ===")
    for p in back_perms:
        print("  ", p)
    print(f"Count: {len(back_perms)} (formula (n-1)! = {math.factorial(n - 1)})")

    print(f"\n=== Amina Drama: seatings that NO LONGER WORK (Amina in the middle) ===")
    for p in drama_perms:
        print("  ", p)
    print(f"Count: {len(drama_perms)}")

    # ---------- Lin & Zahra together (Step 3) ----------
    adjacent_perms = permutations_with_pair_adjacent(friends, pair_a, pair_b)
    non_adjacent_perms = permutations_without_pair_adjacent(friends, pair_a, pair_b)

    print(f"\n=== Step 3: Seatings where {pair_a} and {pair_b} sit TOGETHER (adjacent) ===")
    for p in adjacent_perms:
        print("  ✅", p)
    print(
        f"Count: {len(adjacent_perms)} "
        f"(math says 2 * (n-1)! = 2 * {math.factorial(n - 1)} = {expected_pair_adjacent_count(friends)})"
    )

    print(f"\n=== Seatings that FALL AWAY now ( {pair_a} and {pair_b} are NOT adjacent ) ===")
    for p in non_adjacent_perms:
        print("  ❌", p)
    print(f"Count: {len(non_adjacent_perms)}")

    print("\n--- Sanity check for adjacency partition ---")
    print(f"Adjacent + non-adjacent = {len(adjacent_perms)} + {len(non_adjacent_perms)} "
          f"= {len(adjacent_perms) + len(non_adjacent_perms)} (should equal total 24)")


# ---------- Unit tests: rules embodied as tests ----------

class TestPermutationsBasic(unittest.TestCase):
    """
    Tests for the original 'count all permutations' rule.
    """

    def test_total_count_matches_factorial(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        self.assertEqual(
            count_permutations(friends),
            expected_permutation_count(friends)
        )

    def test_empty_list_has_one_permutation(self):
        items = []
        self.assertEqual(count_permutations(items), 1)
        self.assertEqual(expected_permutation_count(items), 1)


class TestFixedPersonSeating(unittest.TestCase):
    """
    Tests that embody our 'Amina at the ends / Amina Drama' rules.
    """

    def test_front_count_matches_factorial_n_minus_1(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        n = len(friends)
        self.assertEqual(
            count_with_person_first(friends, "Amina"),
            math.factorial(n - 1)
        )

    def test_back_count_matches_factorial_n_minus_1(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        n = len(friends)
        self.assertEqual(
            count_with_person_last(friends, "Amina"),
            math.factorial(n - 1)
        )

    def test_first_or_last_matches_2_factorial_n_minus_1_for_n_ge_2(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        count = count_with_person_first_or_last(friends, "Amina")
        expected = expected_person_fixed_first_or_last(friends)
        self.assertEqual(count, expected)

    def test_drama_middle_only(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        drama = permutations_with_person_not_at_ends(friends, "Amina")
        for p in drama:
            self.assertIn("Amina", p)
            self.assertNotEqual(p[0], "Amina")
            self.assertNotEqual(p[-1], "Amina")


class TestAdjacentPair(unittest.TestCase):
    """
    Tests for the 'two friends sit together' rule.
    """

    def test_adjacent_count_matches_2_factorial_n_minus_1_for_4(self):
        """
        Rule: For 4 friends, Lin and Zahra together should give
        2 * (4-1)! = 2 * 6 = 12 seatings.
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        count = count_with_pair_adjacent(friends, "Lin", "Zahra")
        expected = expected_pair_adjacent_count(friends)
        self.assertEqual(count, expected)
        self.assertEqual(expected, 12)

    def test_adjacent_and_nonadjacent_partition_all_permutations(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        all_perms = set(generate_permutations(friends))

        adj = set(permutations_with_pair_adjacent(friends, "Lin", "Zahra"))
        non_adj = set(permutations_without_pair_adjacent(friends, "Lin", "Zahra"))

        # Sets are disjoint
        self.assertTrue(adj.isdisjoint(non_adj))

        # Together they cover all permutations
        self.assertEqual(all_perms, adj | non_adj)

    def test_every_adjacent_seating_has_pair_adjacent(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        adj = permutations_with_pair_adjacent(friends, "Lin", "Zahra")
        for p in adj:
            self.assertTrue(are_adjacent(p, "Lin", "Zahra"))

    def test_every_nonadjacent_seating_has_pair_not_adjacent(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        non_adj = permutations_without_pair_adjacent(friends, "Lin", "Zahra")
        for p in non_adj:
            self.assertFalse(are_adjacent(p, "Lin", "Zahra"))


if __name__ == "__main__":
    # 1) Run the demo so we can SEE what's going on
    main()

    print("\nRunning unit tests...\n")

    # 2) Run unit tests
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
