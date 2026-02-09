# linear_searcher.py
from __future__ import annotations

from typing import Sequence


def linear_search(data: Sequence[int], target: int) -> int:
    """
    Return the index of `target` in `data`, or -1 if not found.
    """
    for i, value in enumerate(data):
        if value == target:
            return i
    return -1


class LinearSearcher:
    """
    Small wrapper class for OOP usage.
    Keeps the linear search logic isolated in this file.
    """

    def search(self, data: Sequence[int], target: int) -> int:
        return linear_search(data, target)
