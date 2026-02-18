#!/usr/bin/env python3
"""
But Do You Really Have a Dream? 🧠🔥
- Reads output.txt (preferred) or extracts from Full_text_I_Have_a_Dream_.pdf
- Performs word frequency analysis
- Writes results to a CSV

Run:
  python dream_word_frequency.py

Optional:
  python dream_word_frequency.py --top 50
  python dream_word_frequency.py --min-len 2
  python dream_word_frequency.py --keep-stopwords
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path


DEFAULT_STOPWORDS = {
    # A small, classroom-friendly stopword list (no giant dictionary lecture needed)
    "the", "a", "an", "and", "or", "but", "if", "then", "so", "to", "of", "in", "on",
    "for", "with", "as", "at", "by", "from", "into", "about", "over", "under",
    "is", "am", "are", "was", "were", "be", "been", "being",
    "it", "its", "this", "that", "these", "those",
    "i", "me", "my", "we", "us", "our", "you", "your", "he", "him", "his", "she", "her",
    "they", "them", "their",
    "not", "no", "nor",
    "will", "shall", "can", "could", "would", "should", "may", "might", "must",
    "do", "does", "did", "doing", "done",
    "have", "has", "had", "having",
    "there", "here", "when", "where", "why", "how", "what", "which", "who", "whom",
}


def extract_pdf_to_text(pdf_path: Path, txt_path: Path) -> str:
    """
    Extract text from a PDF using pdfminer.six.
    Writes to txt_path and returns the extracted text.
    """
    try:
        from pdfminer.high_level import extract_text  # type: ignore
    except ImportError as e:
        raise SystemExit(
            "pdfminer.six is not installed, so I can't extract from PDF.\n"
            "Install it with:\n"
            "  python -m pip install pdfminer.six"
        ) from e

    text = extract_text(str(pdf_path)) or ""
    text = text.strip() + "\n"
    txt_path.write_text(text, encoding="utf-8")
    return text


def load_text(txt_path: Path, pdf_path: Path) -> str:
    """
    Prefer txt_path if it exists. Otherwise extract from pdf_path into txt_path.
    """
    if txt_path.exists():
        return txt_path.read_text(encoding="utf-8", errors="replace")

    if not pdf_path.exists():
        raise SystemExit(f"Neither {txt_path.name} nor {pdf_path.name} exists in {txt_path.parent}")

    return extract_pdf_to_text(pdf_path, txt_path)


def tokenize(text: str, min_len: int) -> list[str]:
    """
    Normalize and tokenize words.
    - lowercases
    - keeps letters and apostrophes (so "don't" stays together)
    - strips most punctuation
    """
    text = text.lower()

    # Convert fancy apostrophes to normal apostrophe
    text = text.replace("’", "'")

    # Keep letters and apostrophes, turn everything else into spaces
    text = re.sub(r"[^a-z'\s]+", " ", text)

    # Split into candidate tokens
    tokens = [t.strip("'") for t in text.split()]

    # Remove empty + too-short tokens
    tokens = [t for t in tokens if len(t) >= min_len]

    return tokens


def write_csv(rows: list[dict], csv_path: Path) -> None:
    fieldnames = ["rank", "word", "count", "percent", "cumulative_percent"]
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Word frequency analysis for I Have a Dream speech.")
    parser.add_argument("--top", type=int, default=50, help="Print top N words to console (default 50)")
    parser.add_argument("--min-len", type=int, default=2, help="Minimum word length to keep (default 2)")
    parser.add_argument("--keep-stopwords", action="store_true", help="Keep common stopwords (default removes them)")
    parser.add_argument("--txt", type=str, default="output.txt", help="Input TXT filename (default output.txt)")
    parser.add_argument("--pdf", type=str, default="Full_text_I_Have_a_Dream_.pdf", help="Input PDF filename")
    parser.add_argument("--out", type=str, default="dream_word_frequency.csv", help="Output CSV filename")
    args = parser.parse_args()

    folder = Path.cwd()
    txt_path = folder / args.txt
    pdf_path = folder / args.pdf
    csv_path = folder / args.out

    raw_text = load_text(txt_path, pdf_path)

    tokens = tokenize(raw_text, min_len=args.min_len)

    if not args.keep_stopwords:
        tokens = [t for t in tokens if t not in DEFAULT_STOPWORDS]

    counts = Counter(tokens)
    total = sum(counts.values())

    if total == 0:
        raise SystemExit("No words found after cleaning. Is the text empty or scanned?")

    # Build sorted rows
    sorted_items = counts.most_common()
    rows: list[dict] = []

    cumulative = 0.0
    for idx, (word, count) in enumerate(sorted_items, start=1):
        percent = (count / total) * 100.0
        cumulative += percent
        rows.append(
            {
                "rank": idx,
                "word": word,
                "count": count,
                "percent": f"{percent:.4f}",
                "cumulative_percent": f"{cumulative:.4f}",
            }
        )

    write_csv(rows, csv_path)

    # Console preview
    print(f"\n✅ Wrote CSV: {csv_path}")
    print(f"Total counted words (after cleaning): {total}")
    print(f"Unique words: {len(counts)}")

    print(f"\nTop {args.top} words:")
    for i, (word, count) in enumerate(sorted_items[: args.top], start=1):
        print(f"{i:>3}. {word:<15} {count}")

    # A little dramatic flourish (optional but fun)
    print("\n🎤 Verdict: the speech has a dream... now let’s see if your text does too.\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
