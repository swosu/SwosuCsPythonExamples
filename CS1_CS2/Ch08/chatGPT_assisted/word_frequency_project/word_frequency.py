# word_frequency.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Set, Tuple
import re


@dataclass
class WordFrequencyResult:
    """Data object: the counted frequencies plus useful metadata."""
    counts: Dict[str, int]
    total_tokens: int
    unique_tokens: int
    first_seen_order: List[str]  # preserves first appearance order of normalized tokens
    source: str


class WordFrequencyCounter:
    """
    Responsibility: tokenize + normalize + count words.
    Case-insensitive counting is handled by normalization.
    """

    def __init__(
        self,
        case_insensitive: bool = True,
        keep_apostrophes: bool = True,
        keep_hyphens: bool = False,
        ignore_numbers: bool = False,
        stopwords: Optional[Set[str]] = None,
    ) -> None:
        self.case_insensitive = case_insensitive
        self.keep_apostrophes = keep_apostrophes
        self.keep_hyphens = keep_hyphens
        self.ignore_numbers = ignore_numbers
        self.stopwords = {w.lower() for w in stopwords} if stopwords else set()

        self._token_pattern = self._build_token_pattern()

    # ---- Steps / function headings (core pipeline) ----

    def tokenize(self, text: str) -> List[str]:
        """Split raw text into candidate tokens (still not normalized)."""
        return self._token_pattern.findall(text)

    def normalize(self, token: str) -> str:
        """Normalize a token so comparisons are consistent (case-insensitive + cleanup)."""
        t = token.strip()

        if self.case_insensitive:
            t = t.lower()

        # If we don't keep apostrophes/hyphens, strip them out.
        if not self.keep_apostrophes:
            t = t.replace("'", "")
        if not self.keep_hyphens:
            t = t.replace("-", "")

        return t

    def count_words(self, text: str, source: str = "unknown") -> WordFrequencyResult:
        """Full pipeline: tokenize -> normalize -> count -> attach metadata."""
        raw_tokens = self.tokenize(text)

        counts: Dict[str, int] = {}
        first_seen_order: List[str] = []
        seen: Set[str] = set()
        total = 0

        for raw in raw_tokens:
            token = self.normalize(raw)

            if not token:
                continue
            if self.ignore_numbers and token.isdigit():
                continue
            if token in self.stopwords:
                continue

            total += 1

            if token not in counts:
                counts[token] = 1
            else:
                counts[token] += 1

            if token not in seen:
                seen.add(token)
                first_seen_order.append(token)

        return WordFrequencyResult(
            counts=counts,
            total_tokens=total,
            unique_tokens=len(counts),
            first_seen_order=first_seen_order,
            source=source,
        )

    # ---- Helpers ----

    def _build_token_pattern(self) -> re.Pattern:
        """
        Decide what "counts as a word" at the tokenization stage.

        We use a regex that can include apostrophes/hyphens depending on config.
        """
        # Base: letters and digits
        core = r"[A-Za-z0-9]+"

        if self.keep_apostrophes and self.keep_hyphens:
            # allow internal ' or - sequences: e.g., don't, state-of-the-art
            pattern = rf"{core}(?:['-]{core})*"
        elif self.keep_apostrophes:
            pattern = rf"{core}(?:'{core})*"
        elif self.keep_hyphens:
            pattern = rf"{core}(?:-{core})*"
        else:
            pattern = core

        return re.compile(pattern)
