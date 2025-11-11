#!/usr/bin/env python3
"""
seating_permutations_with_tests.py

Explore permutations of friends in a row of chairs.

Current rules:
- Count all seatings.
- Count only seatings where Amina is in the first chair.
- Count only seatings where Amina is in the last chair.
- Count only seatings where Amina is in the first OR last chair.
- List:
    * all seatings with Amina at the front,
    * all seatings with Amina at the back,
    * all seatings that are now "not allowed" (Amina in the middle).

Each rule is backed by unit tests.
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


# ---------- "fixed person" counting rules ----------

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


# ---------- Demo / main program ----------

def main():
    """
    Demo showing how the counts line up with the formulas,
    and printing out the three categories:

    - Amina at the front
    - Amina at the back
    - Amina Drama: seatings that no longer work
    """
    friends = ["Amina", "Lin", "Zahra", "Jake"]
    vip = "Amina"
    n = len(friends)

    all_perms = generate_permutations(friends)
    front_perms = permutations_with_person_first(friends, vip)
    back_perms = permutations_with_person_last(friends, vip)
    drama_perms = permutations_with_person_not_at_ends(friends, vip)

    print("Friends:", friends)
    print(f"\nTotal seatings: {len(all_perms)} (should be {math.factorial(n)} = {n}!)")

    # 1) Amina at the front
    print(f"\n=== Seatings with {vip} at the FRONT ===")
    for p in front_perms:
        print("  ", p)
    print(f"Count: {len(front_perms)} (formula (n-1)! = {math.factorial(n - 1)})")

    # 2) Amina at the back
    print(f"\n=== Seatings with {vip} at the BACK ===")
    for p in back_perms:
        print("  ", p)
    print(f"Count: {len(back_perms)} (formula (n-1)! = {math.factorial(n - 1)})")

    # 3) Amina Drama – seatings that no longer work
    print(f"\n=== Amina Drama: seatings that NO LONGER WORK (Amina in the middle) ===")
    for p in drama_perms:
        print("  ", p)
    print(f"Count: {len(drama_perms)}")

    # Sanity check: partitioning for n >= 2
    # All permutations with Amina present should split into:
    #   front ∪ back ∪ drama   (disjoint union)
    print("\n--- Partition check ---")
    drama_union_size = len(set(front_perms) | set(back_perms) | set(drama_perms))
    print("Unique seatings in front/back/drama:",
          drama_union_size, " (should equal total seatings with Amina)")


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

    def test_front_list_and_count_agree(self):
        """
        Rule: 'Count with person first' must match
        'length of list of permutations with person first'.
        """
        friends = ["Amina", "Lin", "Zahra"]
        front_list = permutations_with_person_first(friends, "Amina")
        self.assertEqual(
            len(front_list),
            count_with_person_first(friends, "Amina")
        )
        # Every permutation in the list should have Amina first
        for p in front_list:
            self.assertEqual(p[0], "Amina")

    def test_back_list_and_count_agree(self):
        friends = ["Amina", "Lin", "Zahra"]
        back_list = permutations_with_person_last(friends, "Amina")
        self.assertEqual(
            len(back_list),
            count_with_person_last(friends, "Amina")
        )
        for p in back_list:
            self.assertEqual(p[-1], "Amina")

    def test_drama_list_has_amini_in_middle_only(self):
        """
        "Amina Drama" rule:
        All 'drama' seatings must have Amina present, but NOT in
        the first or last seat.
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        drama = permutations_with_person_not_at_ends(friends, "Amina")
        for p in drama:
            self.assertIn("Amina", p)
            self.assertNotEqual(p[0], "Amina")
            self.assertNotEqual(p[-1], "Amina")

    def test_partition_of_permutations_with_amini(self):
        """
        For n >= 2, the permutations with Amina present should be
        partitioned into:
            - front
            - back
            - drama (middle)
        with no overlaps and correct total.
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        all_perms = generate_permutations(friends)

        front = set(permutations_with_person_first(friends, "Amina"))
        back = set(permutations_with_person_last(friends, "Amina"))
        drama = set(permutations_with_person_not_at_ends(friends, "Amina"))

        # All three sets are disjoint
        self.assertTrue(front.isdisjoint(back))
        self.assertTrue(front.isdisjoint(drama))
        self.assertTrue(back.isdisjoint(drama))

        # Union of front/back/drama should give all permutations with Amina
        with_amini = {p for p in all_perms if "Amina" in p}
        union = front | back | drama

        self.assertEqual(with_amini, union)


if __name__ == "__main__":
    # 1) Run the demo so we can see the options and the Amina Drama unfold
    main()

    print("\nRunning unit tests...\n")

    # 2) Run unit tests
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
