# chap6_discussion_cookies.py
import math
from itertools import product
from textwrap import dedent

def stars_bars(n, k):
    return math.comb(n + k - 1, k - 1)

def brute_count(n, k):
    return sum(1 for t in product(range(n + 1), repeat=k) if sum(t) == n)

def main():
    n, k = 6, 4
    formula = stars_bars(n, k)
    brute = brute_count(n, k)

    section1 = "1) One-sentence summary\nHow many multisets of size 6 can be chosen from 4 cookie types (order and identity of individual cookies don’t matter)?"

    section2 = dedent("""\
    2) References & resources
    - Discrete Mathematics: an Open Introduction (Section 6.5: Stars and Bars / combinations with repetition)
    - Overview: https://discrete.openmathbooks.org/dmoi3.html""")

    section3 = dedent("""\
    3) Assumptions & key observations
    - Order does not matter; only the type counts.
    - Unlimited supply of each type (or at least 6 of each).
    - Let (x1, x2, x3, x4) be counts of each cookie type with x1 + x2 + x3 + x4 = 6.
    - This is a standard stars & bars problem (nonnegative integer solutions).""")

    work_math = math.comb(n + k - 1, k - 1)
    section4 = dedent(f"""\
    4) Work (path to solution)
    We count nonnegative integer solutions to x1 + x2 + x3 + x4 = 6.
    By stars & bars, the number is C(6 + 4 − 1, 4 − 1) = C(9, 3) = {work_math}.
    Brute-force verification by enumeration yields {brute}.""")

    section5 = dedent(f"""\
    5) Final answer & justification
    Answer: {formula}.
    Justification: Placing 3 bars among 9 total positions (6 stars + 3 bars) partitions 6 identical cookies into 4 labeled groups, giving C(9,3) = {formula}. The brute-force enumeration matches, confirming correctness.""")

    print(section1, end="\n\n")
    print(section2, end="\n\n")
    print(section3, end="\n\n")
    print(section4, end="\n\n")
    print(section5)

if __name__ == "__main__":
    main()
