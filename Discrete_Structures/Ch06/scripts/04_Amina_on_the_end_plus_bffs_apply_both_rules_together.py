#!/usr/bin/env python3
"""
seating_permutations_with_tests.py

Explore permutations of friends in a row of chairs.

Rules:

Step 1:
- Count all seatings (n! total).

Step 2 (Amina Drama):
- Amina must sit on an END (front or back).
- Middle Amina seatings are "not allowed".

Step 3 (Lin–Zahra BFF rule):
- Lin and Zahra must sit in adjacent seats.
- We now care about the intersection:
    Amina on an end AND Lin & Zahra adjacent.
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
    Expected count of seatings where a distinguished person is in an END seat.

    For n >= 2:
        total = 2 * (n-1)!   (front OR back)

    For n = 1: 1 seating.
    For n = 0: 0 seatings.
    """
    n = len(items)
    if n == 0:
        return 0
    if n == 1:
        return 1
    return 2 * math.factorial(n - 1)


# ---------- "two friends sit together" helpers (Lin & Zahra) ----------

def are_adjacent(seating, a, b):
    """
    Return True if a and b sit in adjacent chairs (either order).
    """
    try:
        i = seating.index(a)
        j = seating.index(b)
    except ValueError:
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
    return len(permutations_with_pair_adjacent(items, a, b))


def expected_pair_adjacent_count(items):
    """
    Expected count where two distinguished friends sit together.

    Treat them as one "block":
        - Number of blocks: (n - 1)
        - Arrange blocks: (n - 1)!
        - Inside the block, 2! orders.

    Total = 2 * (n-1)! for n >= 2.
    """
    n = len(items)
    if n < 2:
        return 0
    return 2 * math.factorial(n - 1)


# ---------- NEW: intersection of rules ----------

def permutations_with_ends_and_pair_adjacent(items, person, a, b):
    """
    Return permutations where:
      - `person` is in the first OR last chair
      - and `a` and `b` are adjacent.
    """
    return [
        p for p in generate_permutations(items)
        if (p[0] == person or p[-1] == person) and are_adjacent(p, a, b)
    ]


def count_with_ends_and_pair_adjacent(items, person, a, b):
    return len(permutations_with_ends_and_pair_adjacent(items, person, a, b))


def expected_ends_and_pair_adjacent_count(items):
    """
    Math rule for intersection:

    We want:
        - Amina on an end (front OR back)
        - Lin & Zahra adjacent

    Case Amina fixed on the LEFT:
        There are (n - 1) remaining people.
        Among those, the number of seatings with Lin & Zahra adjacent is:
            2 * ( (n-1) - 1 )! = 2 * (n - 2)!

    Case Amina fixed on the RIGHT:
        Same count again.

    Total = 2 * [ 2 * (n - 2)! ] = 4 * (n - 2)!  for n >= 3.

    For n < 3, we don't have enough distinct people for this pattern.
    """
    n = len(items)
    if n < 3:
        return 0
    return 4 * math.factorial(n - 2)


# ---------- Demo / main program ----------

def main():
    friends = ["Amina", "Lin", "Zahra", "Jake"]
    vip = "Amina"
    pair_a, pair_b = "Lin", "Zahra"

    n = len(friends)
    all_perms = generate_permutations(friends)

    print("Friends:", friends)
    print("\n=== All permutations ===")
    for p in all_perms:
        print("  ", p)
    print(f"Total seatings: {len(all_perms)} (4! = 4*3*2*1 = {math.factorial(n)})")

    # Step 2: Amina ends vs middle
    front_perms = permutations_with_person_first(friends, vip)
    back_perms = permutations_with_person_last(friends, vip)
    drama_perms = permutations_with_person_not_at_ends(friends, vip)

    print(f"\n=== Amina on the ENDS (Step 2) ===")
    for p in front_perms:
        print("  FRONT:", p)
    for p in back_perms:
        print("  BACK: ", p)
    print(f"Count with Amina on an end: {len(front_perms) + len(back_perms)} "
          f"(2 * 3! = 2 * 6 = 12)")
    print(f"Seatings we THROW OUT now (Amina in the middle): {len(drama_perms)}")

    # Step 3: Lin & Zahra together (global)
    adjacent_perms = permutations_with_pair_adjacent(friends, pair_a, pair_b)
    non_adjacent_perms = permutations_without_pair_adjacent(friends, pair_a, pair_b)

    print(f"\n=== Lin & Zahra TOGETHER (Step 3, ignoring Amina for the moment) ===")
    for p in adjacent_perms:
        print("  LZ ✅", p)
    print(f"Count with Lin & Zahra adjacent: {len(adjacent_perms)} "
          f"(2 * 3! = 12)")

    print(f"\nSeatings where Lin & Zahra are NOT adjacent (they fall away if we enforce BFF rule):")
    for p in non_adjacent_perms:
        print("  LZ ❌", p)
    print(f"Count not adjacent: {len(non_adjacent_perms)}")

    # Intersection: Amina at an end AND Lin & Zahra together
    both_rules_perms = permutations_with_ends_and_pair_adjacent(
        friends, vip, pair_a, pair_b
    )

    # Among the LZ-adjacent seatings, separate those that fail because of Amina
    bad_due_to_amina = [
        p for p in adjacent_perms if not (p[0] == vip or p[-1] == vip)
    ]

    print(f"\n=== BOTH RULES: Amina on an end AND Lin & Zahra together ===")
    print("These are the seatings that SURVIVE all the drama:")
    for p in both_rules_perms:
        print("  ✅ FULL OK:", p)
    print(f"Count that meet BOTH rules: {len(both_rules_perms)} "
          f"(math says 4 * (4-2)! = 4 * 2! = 8)")

    print("\nThese seatings had Lin & Zahra together,")
    print("but are REJECTED because Amina is stuck in the middle:")
    for p in bad_due_to_amina:
        print("  ❌ FAILS Amina rule:", p)
    print(f"Count rejected only because of Amina-at-the-end rule: {len(bad_due_to_amina)}")

    print("\n--- Summary of the math filters ---")
    print("Start:          4!  = 24 total seatings")
    print("LZ together:    2 * 3! = 12 seatings with Lin & Zahra adjacent")
    print("Amina on ends:  2 * 3! = 12 seatings with Amina on an end")
    print("Both rules:     4 * 2! = 8 seatings with Amina on an end AND LZ adjacent")


# ---------- Unit tests ----------

class TestPermutationsBasic(unittest.TestCase):
    def test_total_count_matches_factorial(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        self.assertEqual(
            count_permutations(friends),
            expected_permutation_count(friends),
        )


class TestEndsAndAdjacency(unittest.TestCase):
    def test_pair_adjacent_count_for_4(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        self.assertEqual(
            count_with_pair_adjacent(friends, "Lin", "Zahra"),
            expected_pair_adjacent_count(friends),
        )
        self.assertEqual(expected_pair_adjacent_count(friends), 12)

    def test_ends_and_pair_adjacent_count_for_4(self):
        """
        Rule: For 4 friends, Amina on an end AND Lin & Zahra adjacent
        should give 4 * (4-2)! = 4 * 2! = 8 seatings.
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        count = count_with_ends_and_pair_adjacent(friends, "Amina", "Lin", "Zahra")
        expected = expected_ends_and_pair_adjacent_count(friends)
        self.assertEqual(count, expected)
        self.assertEqual(expected, 8)

    def test_intersection_matches_manual_filter(self):
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        vip = "Amina"
        pair_a, pair_b = "Lin", "Zahra"

        all_perms = generate_permutations(friends)
        # Manual definition of both rules:
        manual_both = {
            p for p in all_perms
            if (p[0] == vip or p[-1] == vip) and are_adjacent(p, pair_a, pair_b)
        }
        func_both = set(permutations_with_ends_and_pair_adjacent(
            friends, vip, pair_a, pair_b
        ))

        self.assertEqual(manual_both, func_both)


if __name__ == "__main__":
    main()
    print("\nRunning unit tests...\n")
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
