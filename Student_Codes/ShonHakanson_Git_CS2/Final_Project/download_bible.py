#!/usr/bin/env python3
"""
download_and_prepare_bible.py

One-shot downloader + normalizer to produce `bible_local.json` in the canonical structure used
by the keyword search tool.

Features:
- Tries several public candidate JSON sources (raw GitHub URLs); you can add more to CANDIDATE_SOURCE_LIST.
- If a candidate source fails or has an unfamiliar shape, attempts flexible normalization heuristics.
- Accepts a --url override to try any other raw JSON URL you provide.
- Writes `bible_local.json` (or another filename via --output) with the structure:
    { "Genesis": { "1": [ {"verse":"1","text":"..."}, ... ], ... }, ... }
- Prints a short summary of books / chapters / verses found.

Usage:
    pip install requests
    python download_and_prepare_bible.py            # tries built-in candidate sources
    python download_and_prepare_bible.py --url <RAW_JSON_URL>  # try a specific URL
    python download_and_prepare_bible.py --output my_bible.json

Notes:
- If the script cannot automatically normalize a given JSON shape, it will print diagnostic hints showing the top-level keys/structure
  so you can point to a different source or paste the structure for me to adapt.
"""
import argparse
import json
import os
import sys
import textwrap
from typing import Any, Dict, List, Optional, Tuple

try:
    import requests
except Exception:
    print("This script requires the 'requests' package. Install with: pip install requests", file=sys.stderr)
    raise

# --------------------------
# Configuration
# --------------------------
OUTPUT_FILENAME_DEFAULT = "bible_local.json"

# Candidate sources (raw JSON URLs). These are example raw GitHub URLs commonly used by public repos.
# If any become invalid, pass --url to provide a working raw JSON URL.
CANDIDATE_SOURCE_LIST = [
    # KJV JSON (common repo) - if invalid, supply your own
    ("KJV - thiagobodruk (common public mirror)", "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/kjv.json"),
    # WEB JSON from public mirrors / repos (example)
    ("WEB - public mirror (example)", "https://raw.githubusercontent.com/scrollmapper/bible_databases/master/json/web.json"),
    # Another KJV mirror (example)
    ("KJV - another repository (example)", "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/kjv.json"),
    # If you'd like, add more candidate sources here as (label, url) tuples.
]

# --------------------------
# Helpers: shape inspection & normalization
# --------------------------
def try_download_json_from_url(raw_url: str, timeout_seconds: int = 20) -> Optional[Any]:
    """Download JSON from a raw URL and return the parsed JSON or None on error."""
    try:
        response = requests.get(raw_url, timeout=timeout_seconds)
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print(f"  [!] Download or JSON parse failed for {raw_url!r}: {exc}")
        return None

def guess_top_level_shape(sample_json: Any) -> str:
    """Return a short human-friendly description of the top-level JSON shape for diagnostics."""
    if sample_json is None:
        return "None"
    if isinstance(sample_json, dict):
        keys = list(sample_json.keys())[:8]
        key_sample = ", ".join(repr(k) for k in keys)
        return f"dict with keys: {key_sample} (showing up to 8)"
    if isinstance(sample_json, list):
        return f"list with {len(sample_json)} elements; first element type: {type(sample_json[0]).__name__ if sample_json else 'n/a'}"
    return f"{type(sample_json).__name__}"

def normalize_common_book_list_shape(raw_json: Any) -> Optional[Dict[str, Dict[str, List[Dict[str, str]]]]]:
    """
    Normalize a common shape where JSON is a list of book objects, e.g.
    [
      {"name":"Genesis","chapters":{"1":[{"verse":"1","text":"..."},...]},...},
      ...
    ]
    or a dict where keys are book names mapping to {"chapters": {...}} or directly chapters.
    """
    normalized: Dict[str, Dict[str, List[Dict[str, str]]]] = {}

    # Case A: list of book objects
    if isinstance(raw_json, list):
        # try to find first element that looks like a book object
        for candidate_book in raw_json:
            if not isinstance(candidate_book, dict):
                continue
        # iterate array and attempt to extract book name + chapters
        for book_object in raw_json:
            if not isinstance(book_object, dict):
                continue
            # heuristics: check common keys: 'name'/'book_name' and 'chapters'/'chapter'
            book_name = None
            if "name" in book_object:
                book_name = book_object.get("name")
            elif "book_name" in book_object:
                book_name = book_object.get("book_name")
            elif "book" in book_object:
                book_name = book_object.get("book")
            # fallback: maybe the object key is the canonical book name
            # extract chapters structure
            chapters_candidate = book_object.get("chapters") or book_object.get("chapter") or book_object.get("verses")
            # Some datasets have nested 'chapters': {"1": {"1":"text", "2":"text"}, ...}
            if book_name and isinstance(chapters_candidate, dict):
                normalized_book_chapters: Dict[str, List[Dict[str, str]]] = {}
                # chapters_candidate may map chapter->dict(verse->text) or chapter->list
                for chapter_key, chapter_value in chapters_candidate.items():
                    # if chapter_value is dict of verse->text
                    if isinstance(chapter_value, dict):
                        verse_list: List[Dict[str, str]] = []
                        for verse_key, verse_val in sorted(chapter_value.items(), key=lambda kv: int(str(kv[0])) if str(kv[0]).isdigit() else str(kv[0])):
                            verse_list.append({"verse": str(verse_key), "text": str(verse_val)})
                        normalized_book_chapters[str(chapter_key)] = verse_list
                    elif isinstance(chapter_value, list):
                        # assume list of {"verse":n,"text":"..."} or plain strings
                        verse_list = []
                        for v in chapter_value:
                            if isinstance(v, dict) and "verse" in v and "text" in v:
                                verse_list.append({"verse": str(v["verse"]), "text": str(v["text"])})
                            elif isinstance(v, str):
                                # ambiguous: we cannot determine verse numbers reliably; skip
                                pass
                        if verse_list:
                            normalized_book_chapters[str(chapter_key)] = verse_list
                if normalized_book_chapters:
                    normalized[str(book_name)] = normalized_book_chapters
        if normalized:
            return normalized

    # Case B: top-level dict with book keys
    if isinstance(raw_json, dict):
        possible_books = {}
        for candidate_book_name, candidate_book_value in raw_json.items():
            # Accept if candidate_book_value is dict with chapter keys or list
            if isinstance(candidate_book_value, dict):
                # candidate_book_value might be chapters mapping or a book object with 'chapters'
                chapters_blob = None
                if "chapters" in candidate_book_value and isinstance(candidate_book_value["chapters"], dict):
                    chapters_blob = candidate_book_value["chapters"]
                elif all(isinstance(k, str) and k.isdigit() for k in candidate_book_value.keys()):
                    # candidate_book_value looks like direct chapters mapping "1": {...}
                    chapters_blob = candidate_book_value
                if isinstance(chapters_blob, dict):
                    normalized_chapters = {}
                    for chapter_key, chapter_value in chapters_blob.items():
                        if isinstance(chapter_value, dict):
                            # verse->text mapping
                            verse_list = []
                            for verse_key, verse_text in sorted(chapter_value.items(), key=lambda kv: int(str(kv[0])) if str(kv[0]).isdigit() else str(kv[0])):
                                verse_list.append({"verse": str(verse_key), "text": str(verse_text)})
                            normalized_chapters[str(chapter_key)] = verse_list
                        elif isinstance(chapter_value, list):
                            verse_list = []
                            for item in chapter_value:
                                if isinstance(item, dict) and "verse" in item and "text" in item:
                                    verse_list.append({"verse": str(item["verse"]), "text": str(item["text"])})
                            if verse_list:
                                normalized_chapters[str(chapter_key)] = verse_list
                    if normalized_chapters:
                        possible_books[candidate_book_name] = normalized_chapters
        if possible_books:
            return possible_books

    # If we couldn't normalize, return None
    return None

def normalize_other_shapes(raw_json: Any) -> Optional[Dict[str, Dict[str, List[Dict[str, str]]]]]:
    """
    Additional heuristics for other shapes:
    - Some datasets are an object with "books": [ { "name": "...", "chapters": [...] } ]
    - Others are a list of verses with fields book, chapter, verse, text; we can group them.
    """
    if raw_json is None:
        return None

    # Case: {"books":[{...}, ...]}
    if isinstance(raw_json, dict) and "books" in raw_json and isinstance(raw_json["books"], list):
        candidate = normalize_common_book_list_shape(raw_json["books"])
        if candidate:
            return candidate

    # Case: list of verse objects like [ {"book":"Genesis", "chapter":1, "verse":1, "text":"..."}, ... ]
    if isinstance(raw_json, list):
        if raw_json and isinstance(raw_json[0], dict) and all(k in raw_json[0] for k in ("book", "chapter", "verse", "text")):
            grouped: Dict[str, Dict[str, List[Dict[str, str]]]] = {}
            for verse_obj in raw_json:
                try:
                    book_name = str(verse_obj.get("book"))
                    chapter_str = str(int(verse_obj.get("chapter")))
                    verse_str = str(int(verse_obj.get("verse")))
                    text_str = str(verse_obj.get("text") or "")
                except Exception:
                    continue
                grouped.setdefault(book_name, {}).setdefault(chapter_str, []).append({"verse": verse_str, "text": text_str})
            # Optionally sort verse lists by verse number
            for b, chs in grouped.items():
                for ch, verses in chs.items():
                    verses.sort(key=lambda v: int(v["verse"]) if str(v["verse"]).isdigit() else v["verse"])
            return grouped

    return None

# --------------------------
# Main orchestration
# --------------------------
def attempt_download_and_normalize(source_label: str, source_url: str) -> Tuple[Optional[Dict[str, Dict[str, List[Dict[str, str]]]]], Optional[str]]:
    """
    Try to download the JSON and normalize. Returns (normalized_structure_or_None, diagnostic_message_or_None)
    """
    print(f"Trying source: {source_label} → {source_url}")
    raw_data = try_download_json_from_url(source_url)
    if raw_data is None:
        return None, "download_failed"

    shape_hint = guess_top_level_shape(raw_data)
    print(f"  top-level shape: {shape_hint}")

    normalized = normalize_common_book_list_shape(raw_data)
    if normalized:
        return normalized, None

    normalized = normalize_other_shapes(raw_data)
    if normalized:
        return normalized, None

    # As a last resort, attempt to inspect top-level keys and print a short sample for diagnostics
    diagnostic_snippet = textwrap.shorten(json.dumps(raw_data, default=str)[:2000], width=1200, placeholder="... (truncated for diagnostics)")
    return None, f"unrecognized_shape: {shape_hint}. sample: {diagnostic_snippet}"

def write_bible_local_file(normalized_structure: Dict[str, Dict[str, List[Dict[str, str]]]], output_filename: str) -> bool:
    try:
        with open(output_filename, "w", encoding="utf-8") as out_file:
            json.dump(normalized_structure, out_file, ensure_ascii=False, indent=2)
        return True
    except Exception as exc:
        print(f"[!] Failed to write {output_filename}: {exc}", file=sys.stderr)
        return False

def summarize_and_print(normalized_structure: Dict[str, Dict[str, List[Dict[str, str]]]]) -> None:
    total_books = len(normalized_structure)
    total_chapters = sum(len(chs) for chs in normalized_structure.values())
    total_verses = sum(len(vs) for chs in normalized_structure.values() for vs in chs.values())
    print(f"\nSaved bible_local.json structure summary:")
    print(f"  Books: {total_books}")
    print(f"  Chapters (total): {total_chapters}")
    print(f"  Verses (total): {total_verses}")
    # show first/last book found
    book_names_sorted = sorted(normalized_structure.keys())
    print(f"  Example books found (up to 6): {', '.join(book_names_sorted[:6])}")

def main():
    parser = argparse.ArgumentParser(description="Download + normalize public Bible JSON into bible_local.json")
    parser.add_argument("--url", "-u", help="Optional raw JSON URL to try first (e.g., raw GitHub URL)")
    parser.add_argument("--output", "-o", default=OUTPUT_FILENAME_DEFAULT, help=f"Output filename (default: {OUTPUT_FILENAME_DEFAULT})")
    args = parser.parse_args()

    candidates = []
    if args.url:
        candidates.append(("User-provided URL", args.url))
    candidates.extend(CANDIDATE_SOURCE_LIST)

    normalization_result = None
    last_diagnostic = None

    for label, url in candidates:
        normalized_structure, diagnostic = attempt_download_and_normalize(label, url)
        if normalized_structure:
            normalization_result = normalized_structure
            break
        last_diagnostic = diagnostic

    if normalization_result is None:
        print("\n[!] Failed to automatically normalize any candidate source.")
        if last_diagnostic:
            print("Last diagnostic hint:")
            print(last_diagnostic)
        print("\nOptions to proceed:")
        print("  1) Provide a different raw JSON URL using --url <RAW_JSON_URL>")
        print("  2) If you have a JSON file locally, move it to the current directory and rename to 'bible_local.json'")
        print("  3) Paste the top-level JSON keys/shape here and I can adapt the normalizer to it.")
        sys.exit(2)

    # Write output
    output_written = write_bible_local_file(normalization_result, args.output)
    if not output_written:
        sys.exit(3)

    summarize_and_print(normalization_result)
    print(f"\nWrote normalized Bible JSON to: {args.output}")
    print("You can now run the keyword search script against this file (bible_keyword_search.py).")

if __name__ == "__main__":
    main()
