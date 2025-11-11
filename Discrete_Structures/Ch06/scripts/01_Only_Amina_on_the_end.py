#!/usr/bin/env python3
"""
seating_permutations_with_tests.py

Explore permutations of friends around a row of chairs.

Rules so far:
- Count all seatings.
- Count only seatings where Amina is in the first chair.
- Count only seatings where Amina is in the last chair.
- Count only seatings where Amina is in the first OR last chair.

Each rule is backed by unit tests so we can keep building safely.
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


# ---------- New "fixed person" rules ----------

def count_with_person_first(items, person):
    """
    Count permutations where `person` is in the FIRST position.
    """
    list_of_Amina_at_first = []
    # Generate all permutations of the items
    permutations = generate_permutations(items)
    
    # Initialize a counter for valid permutations
    valid_permutation_count = 0
    
    # Iterate through each permutation
    for permutation in permutations:
        # Check if the person is in the first position
        if permutation[0] == person:
            list_of_Amina_at_first.append(permutation)
            valid_permutation_count += 1

    #print off the list of times that Amina is at first
    print("List of permutations with", person, "at first:")
    for p in list_of_Amina_at_first:
        print("  ", p)
        
    
    # Return the total count of valid permutations
    return valid_permutation_count


def count_with_person_last(items, person):
    """
    Count permutations where `person` is in the LAST position.
    """
    perms = generate_permutations(items)
    return sum(1 for p in perms if p[-1] == person)


def count_with_person_first_or_last(items, person):
    """
    Count permutations where `person` is in the FIRST OR LAST position.

    Note: for n = 1, first == last, so there is only 1 seating,
    not 2.
    """
    perms = generate_permutations(items)
    return sum(1 for p in perms if p[0] == person or p[-1] == person)


def expected_person_fixed_first_or_last(items, person):
    """
    Expected count of seatings where `person` is in the first OR last seat.

    For n >= 2:
        - First seat fixed: (n-1)! ways
        - Last seat fixed:  (n-1)! ways
        - These are disjoint, so total = 2 * (n-1)!.

    For n = 1:
        There is exactly 1 seating (the person in the only chair).
    """
    n = len(items)
    if n == 0:
        return 0  # no people, no seatings
    if n == 1:
        return 1
    return 2 * math.factorial(n - 1)


# ---------- Demo / main program ----------

def main():
    """
    Demo showing how the counts line up with the formulas.
    """
    friends = ["Amina", "Lin", "Zahra", "Jake"]
    vip = "Amina"

    perms = generate_permutations(friends)

    print("Friends:", friends)
    print("\nAll permutations:")
    for p in perms:
        print("  ", p)

    n = len(friends)
    print("\n--- Summary ---")
    print(f"Total seatings: {count_permutations(friends)}")
    print(f"Should be: {expected_permutation_count(friends)} = {n}!")

    print(f"\nSeatings with {vip} in the FIRST chair:")
    first_count = count_with_person_first(friends, vip)
    print("  Python says:", first_count)
    print("  Formula (n-1)! says:", math.factorial(n - 1))

    print(f"\nSeatings with {vip} in the LAST chair:")
    last_count = count_with_person_last(friends, vip)
    print("  Python says:", last_count)
    print("  Formula (n-1)! says:", math.factorial(n - 1))

    print(f"\nSeatings with {vip} in the FIRST OR LAST chair:")
    first_or_last_count = count_with_person_first_or_last(friends, vip)
    print("  Python says:", first_or_last_count)
    print(
        "  Formula says:",
        expected_person_fixed_first_or_last(friends, vip),
        " = 2 * (n-1)! for n >= 2",
    )


# ---------- Unit tests: rules turned into code ----------

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
    Tests that embody our new 'fixed person at an end' rules.
    """

    def test_amini_first_matches_factorial_n_minus_1(self):
        """
        Rule: 'Count only seatings where Amina sits in the first chair.
        That count should be (n-1)!'
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        n = len(friends)
        count = count_with_person_first(friends, "Amina")
        self.assertEqual(count, math.factorial(n - 1))

    def test_amini_last_matches_factorial_n_minus_1(self):
        """
        Rule: 'Count only seatings where Amina sits in the last chair.
        That count should also be (n-1)!'
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        n = len(friends)
        count = count_with_person_last(friends, "Amina")
        self.assertEqual(count, math.factorial(n - 1))

    def test_amini_first_or_last_matches_2_factorial_n_minus_1_for_n_ge_2(self):
        """
        Rule: 'If Amina can sit in the first OR last chair,
        there should be 2 * (n-1)! seatings (for n >= 2).'
        """
        friends = ["Amina", "Lin", "Zahra", "Jake"]
        count = count_with_person_first_or_last(friends, "Amina")
        expected = expected_person_fixed_first_or_last(friends, "Amina")
        self.assertEqual(count, expected)

    def test_first_seatings_actually_have_person_first(self):
        """
        Rule (semantic): 'When we say Amina is in the first chair,
        she really must be in position 0 of every counted permutation.'
        """
        friends = ["Amina", "Lin", "Zahra"]
        perms = generate_permutations(friends)
        # Filter using our rule
        first_only = [p for p in perms if p[0] == "Amina"]

        # Every permutation we kept should have Amina at index 0
        for p in first_only:
            self.assertEqual(p[0], "Amina")

        # Our counting function should agree with this manual filter
        self.assertEqual(
            len(first_only),
            count_with_person_first(friends, "Amina")
        )

    def test_last_seatings_actually_have_person_last(self):
        """
        Same semantic rule, but for the last chair.
        """
        friends = ["Amina", "Lin", "Zahra"]
        perms = generate_permutations(friends)
        last_only = [p for p in perms if p[-1] == "Amina"]

        for p in last_only:
            self.assertEqual(p[-1], "Amina")

        self.assertEqual(
            len(last_only),
            count_with_person_last(friends, "Amina")
        )

    def test_first_or_last_handles_single_person_correctly(self):
        """
        Edge case rule: with just one person, first == last.
        There should only be 1 seating, and all counts agree.
        """
        friends = ["Amina"]
        self.assertEqual(count_permutations(friends), 1)
        self.assertEqual(count_with_person_first(friends, "Amina"), 1)
        self.assertEqual(count_with_person_last(friends, "Amina"), 1)
        self.assertEqual(
            count_with_person_first_or_last(friends, "Amina"),
            expected_person_fixed_first_or_last(friends, "Amina"),
        )
        self.assertEqual(expected_person_fixed_first_or_last(friends, "Amina"), 1)


if __name__ == "__main__":
    # 1) Run the little demo so we can *see* the permutations + counts
    main()

    print("\nRunning unit tests...\n")

    # 2) Run unit tests
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
