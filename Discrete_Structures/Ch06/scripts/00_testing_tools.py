#!/usr/bin/env python3
"""
permutations_with_tests.py

A tiny module to explore permutations with friends,
structured so we can build more features and tests later.
"""

import itertools
import math
import unittest


def generate_permutations(items):
    """
    Return a list of all permutations of the given list of items.
    """
    return list(itertools.permutations(items))


def count_permutations(items):
    """
    Return the number of permutations of the given list of items.
    This should always equal factorial(len(items)).
    """
    return len(generate_permutations(items))


def expected_permutation_count(items):
    """
    Return the mathematically expected number of permutations,
    using n! where n = len(items).
    """
    return math.factorial(len(items))


def main():
    """
    Simple demo of the core functionality.
    """
    friends = ["A", "L", "Z", "J"]
    perms = generate_permutations(friends)

    print("Friends:", friends)
    print("Permutations:")
    for p in perms:
        print("  ", p)

    print("\nNumber of permutations:", len(perms))
    print("Should be:", expected_permutation_count(friends))


class TestPermutations(unittest.TestCase):
    """
    Unit tests for our permutation functions.
    """

    def test_count_matches_factorial_for_4_items(self):
        friends = ["A", "L", "Z", "J"]
        self.assertEqual(
            count_permutations(friends),
            expected_permutation_count(friends),
            "Permutation count should match n! for 4 items",
        )

    def test_count_matches_factorial_for_empty_list(self):
        items = []
        self.assertEqual(count_permutations(items), 1)
        self.assertEqual(expected_permutation_count(items), 1)

    def test_count_matches_factorial_for_single_item(self):
        items = ["X"]
        self.assertEqual(count_permutations(items), 1)
        self.assertEqual(expected_permutation_count(items), 1)

    def test_all_permutations_are_unique(self):
        items = ["A", "B", "C"]
        perms = generate_permutations(items)
        # Convert to set to ensure there are no duplicates
        self.assertEqual(len(perms), len(set(perms)))

    def test_permutations_use_same_elements(self):
        items = ["A", "B", "C"]
        perms = generate_permutations(items)

        for p in perms:
            # Each permutation should be same length and same multiset of elements
            self.assertEqual(len(p), len(items))
            self.assertEqual(sorted(p), sorted(items))


if __name__ == "__main__":
    # 1) Run the little demo so we still see output like your original script
    main()

    print("\nRunning unit tests...\n")

    # 2) Run unit tests
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
