#!/usr/bin/env python3
# ASCII-only code; safe for LaTeX listings.

class DataTracker:
    def __init__(self):
        self.calls = 0
        self.adds = 0
        self.assigns = 0

    def reset(self):
        self.calls = 0
        self.adds = 0
        self.assigns = 0

def fib_recursive(n, trk: DataTracker):
    trk.calls += 1
    if n <= 1:
        trk.assigns += 1
        return n
    trk.adds += 1
    return fib_recursive(n - 1, trk) + fib_recursive(n - 2, trk)

def fib_memo(n, trk: DataTracker, memo=None):
    # Top-down memoization: O(n) time, O(n) space
    if memo is None:
        memo = {}
    trk.calls += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        trk.assigns += 1
        memo[n] = n
        return n
    trk.adds += 1
    val = fib_memo(n - 1, trk, memo) + fib_memo(n - 2, trk, memo)
    memo[n] = val
    return val

def fib_iter(n, trk: DataTracker):
    trk.calls += 1
    if n <= 1:
        trk.assigns += 1
        return n
    a, b = 0, 1
    trk.assigns += 2
    for _ in range(2, n + 1):
        trk.adds += 1
        a, b = b, a + b
        trk.assigns += 2
    return b

