#!/usr/bin/env python3
"""
bible_verse_api_search.py

Interactive Bible keyword/phrase search with integrated downloader (no API key required).

- If run interactively (a real terminal), the script prompts for a keyword and optional choices.
- If run non-interactively (no TTY), the script requires --keyword/-k to be passed.
- On first run the script will attempt to download a full public JSON Bible and save bible_local.json.
- If download fails, it falls back to per-chapter remote fetching (cached locally).

Usage:
    # Interactive (recommended)
    python bible_verse_api_search.py

    # Non-interactive (scripted)
    python bible_verse_api_search.py --keyword love --whole-word --limit 20
"""

import argparse
import json
import os
import re
import sys
import textwrap
import time
from typing import Any, Dict, List, Optional, Tuple

# external dependency
try:
    import requests
except Exception:
    print("Install dependency: pip install requests", file=sys.stderr)
    raise

# ---------------------------
# Canonical book order (Protestant 66-book)
# ---------------------------
CANONICAL_BOOK_ORDER = [
    "Genesis","Exodus","Leviticus","Numbers","Deuteronomy",
    "Joshua","Judges","Ruth","1 Samuel","2 Samuel",
    "1 Kings","2 Kings","1 Chronicles","2 Chronicles","Ezra","Nehemiah","Esther",
    "Job","Psalms","Proverbs","Ecclesiastes","Song of Solomon",
    "Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel",
    "Hosea","Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah",
    "Haggai","Zechariah","Malachi",
    "Matthew","Mark","Luke","John","Acts",
    "Romans","1 Corinthians","2 Corinthians","Galatians","Ephesians","Philippians","Colossians",
    "1 Thessalonians","2 Thessalonians","1 Timothy","2 Timothy","Titus","Philemon",
    "Hebrews","James","1 Peter","2 Peter","1 John","2 John","3 John","Jude","Revelation"
]
BOOK_TO_CANONICAL_INDEX = {name: index for index, name in enumerate(CANONICAL_BOOK_ORDER)}

# ---------------------------
# Filenames & remote patterns
# ---------------------------
DEFAULT_LOCAL_BIBLE_FILENAME = "bible_local.json"
PER_CHAPTER_CACHE_DIRECTORY = "cache_bible_chapters"
REMOTE_PER_CHAPTER_URL_PATTERN = "https://bible-api.com/{book}%20{chapter}?translation=web"
REMOTE_FETCH_DELAY_SECONDS = 0.12

# Candidate raw JSON sources (example raw GitHub URLs)
CANDIDATE_RAW_JSON_SOURCES: List[Tuple[str, str]] = [
    ("KJV - mirror (example)", "https://raw.githubusercontent.com/thiagobodruk/bible/master/json/kjv.json"),
    ("WEB - mirror (example)", "https://raw.githubusercontent.com/scrollmapper/bible_databases/master/json/web.json"),
]

# ---------------------------
# Types
# ---------------------------
JsonType = Any
BibleStructureType = Dict[str, Dict[str, List[Dict[str, str]]]]

# ---------------------------
# VerseMatch class
# ---------------------------
class VerseMatch:
    def __init__(self, book_name: str, chapter_number: int, verse_number: int, verse_text: str):
        self.book_name = book_name
        self.chapter_number = chapter_number
        self.verse_number = verse_number
        self.verse_text = verse_text

    def canonical_sort_key(self):
        book_index = BOOK_TO_CANONICAL_INDEX.get(self.book_name, 999)
        return (book_index, self.chapter_number, self.verse_number)

    def reference_string(self) -> str:
        return f"{self.book_name} {self.chapter_number}:{self.verse_number}"

# ---------------------------
# Downloader & Normalizer
# ---------------------------
def download_json_from_url(raw_url: str, timeout_seconds: int = 20) -> Optional[JsonType]:
    try:
        response = requests.get(raw_url, timeout=timeout_seconds)
        response.raise_for_status()
        return response.json()
    except Exception as exc:
        print(f"  [!] Failed to download/parse {raw_url!r}: {exc}")
        return None

def describe_top_level_shape(sample_json: JsonType) -> str:
    if sample_json is None:
        return "None"
    if isinstance(sample_json, dict):
        sample_keys = list(sample_json.keys())[:8]
        return f"dict with keys: {', '.join(repr(k) for k in sample_keys)}"
    if isinstance(sample_json, list):
        return f"list with {len(sample_json)} elements; first element type: {type(sample_json[0]).__name__ if sample_json else 'n/a'}"
    return f"{type(sample_json).__name__}"

def normalize_common_shapes(raw_json: JsonType) -> Optional[BibleStructureType]:
    # Flat list of verse objects: [{"book":"Genesis","chapter":1,"verse":1,"text":"..."}]
    if isinstance(raw_json, list):
        if raw_json and isinstance(raw_json[0], dict) and all(key in raw_json[0] for key in ("book","chapter","verse","text")):
            grouped: BibleStructureType = {}
            for verse_obj in raw_json:
                try:
                    book_name = str(verse_obj["book"])
                    chapter_str = str(int(verse_obj["chapter"]))
                    verse_str = str(int(verse_obj["verse"]))
                    text_str = str(verse_obj["text"] or "")
                except Exception:
                    continue
                grouped.setdefault(book_name, {}).setdefault(chapter_str, []).append({"verse": verse_str, "text": text_str})
            for book, chapters in grouped.items():
                for ch, verses in chapters.items():
                    verses.sort(key=lambda v: int(v["verse"]) if str(v["verse"]).isdigit() else v["verse"])
            return grouped

        # List of book objects with "name" and "chapters"
        possible_books: BibleStructureType = {}
        found_any = False
        for book_object in raw_json:
            if not isinstance(book_object, dict):
                continue
            book_name = book_object.get("name") or book_object.get("book_name") or book_object.get("book")
            chapters_blob = book_object.get("chapters") or book_object.get("chapter") or book_object.get("verses")
            if book_name and isinstance(chapters_blob, dict):
                normalized_chapters: Dict[str, List[Dict[str,str]]] = {}
                for chapter_key, chapter_value in chapters_blob.items():
                    if isinstance(chapter_value, dict):
                        verse_list = []
                        for verse_key, verse_text in sorted(chapter_value.items(), key=lambda kv: int(str(kv[0])) if str(kv[0]).isdigit() else str(kv[0])):
                            verse_list.append({"verse": str(verse_key), "text": str(verse_text)})
                        normalized_chapters[str(chapter_key)] = verse_list
                    elif isinstance(chapter_value, list):
                        verse_list = []
                        for v in chapter_value:
                            if isinstance(v, dict) and "verse" in v and "text" in v:
                                verse_list.append({"verse": str(v["verse"]), "text": str(v["text"])})
                        if verse_list:
                            normalized_chapters[str(chapter_key)] = verse_list
                if normalized_chapters:
                    possible_books[str(book_name)] = normalized_chapters
                    found_any = True
        if found_any:
            return possible_books

    # Top-level dict mapping book->chapters
    if isinstance(raw_json, dict):
        possible_output: BibleStructureType = {}
        found_any = False
        for top_key, top_value in raw_json.items():
            if isinstance(top_value, dict):
                chapters_blob = top_value.get("chapters") if "chapters" in top_value else None
                if chapters_blob is None:
                    if all(isinstance(k, str) and k.isdigit() for k in top_value.keys()):
                        chapters_blob = top_value
                if isinstance(chapters_blob, dict):
                    normalized_chapters: Dict[str, List[Dict[str,str]]] = {}
                    for chapter_key, chapter_value in chapters_blob.items():
                        if isinstance(chapter_value, dict):
                            verse_list = []
                            for verse_key, verse_text in sorted(chapter_value.items(), key=lambda kv: int(str(kv[0])) if str(kv[0]).isdigit() else str(kv[0])):
                                verse_list.append({"verse": str(verse_key), "text": str(verse_text)})
                            normalized_chapters[str(chapter_key)] = verse_list
                        elif isinstance(chapter_value, list):
                            verse_list = []
                            for v in chapter_value:
                                if isinstance(v, dict) and "verse" in v and "text" in v:
                                    verse_list.append({"verse": str(v["verse"]), "text": str(v["text"])})
                            if verse_list:
                                normalized_chapters[str(chapter_key)] = verse_list
                    if normalized_chapters:
                        possible_output[str(top_key)] = normalized_chapters
                        found_any = True
        if found_any:
            return possible_output
    return None

def attempt_download_and_normalize_from_source(source_label: str, source_url: str) -> Tuple[Optional[BibleStructureType], Optional[str]]:
    print(f"Trying source: {source_label} → {source_url}")
    raw_data = download_json_from_url(source_url)
    if raw_data is None:
        return None, "download_failed"
    print(f"  top-level shape: {describe_top_level_shape(raw_data)}")
    normalized = normalize_common_shapes(raw_data)
    if normalized:
        return normalized, None
    snippet = textwrap.shorten(str(list(raw_data)[:10]) if isinstance(raw_data, list) else str(list(raw_data.keys())[:10]) if isinstance(raw_data, dict) else str(type(raw_data)), width=800)
    return None, f"unrecognized_shape: {describe_top_level_shape(raw_data)}; sample keys/elements: {snippet}"

def write_local_bible_file(normalized_bible: BibleStructureType, output_filename: str) -> bool:
    try:
        with open(output_filename, "w", encoding="utf-8") as output_file:
            json.dump(normalized_bible, output_file, ensure_ascii=False, indent=2)
        return True
    except Exception as exc:
        print(f"[!] Failed to write {output_filename}: {exc}", file=sys.stderr)
        return False

# ---------------------------
# Local load & per-chapter cache
# ---------------------------
def load_local_bible_file(local_filename: str) -> Optional[BibleStructureType]:
    if not os.path.isfile(local_filename):
        return None
    try:
        with open(local_filename, "r", encoding="utf-8") as in_file:
            data = json.load(in_file)
        if isinstance(data, dict):
            return data
    except Exception as exc:
        print(f"[!] Failed to load local bible file {local_filename}: {exc}", file=sys.stderr)
    return None

def ensure_cache_directory_exists(cache_directory: str) -> None:
    if not os.path.isdir(cache_directory):
        os.makedirs(cache_directory, exist_ok=True)

def cache_filename_for_chapter(book_name: str, chapter_number: int) -> str:
    safe_book_name = re.sub(r"[^\w\d]", "_", book_name)
    return os.path.join(PER_CHAPTER_CACHE_DIRECTORY, f"{safe_book_name}_ch{chapter_number}.json")

def fetch_chapter_and_cache(book_name: str, chapter_number: int) -> Optional[List[Dict[str,str]]]:
    ensure_cache_directory_exists(PER_CHAPTER_CACHE_DIRECTORY)
    cache_path = cache_filename_for_chapter(book_name, chapter_number)
    if os.path.isfile(cache_path):
        try:
            with open(cache_path, "r", encoding="utf-8") as cache_file:
                cached_data = json.load(cache_file)
            if isinstance(cached_data, list):
                return cached_data
            if isinstance(cached_data, dict) and "verses" in cached_data:
                return cached_data["verses"]
        except Exception:
            pass

    remote_url = REMOTE_PER_CHAPTER_URL_PATTERN.format(book=book_name.replace(" ", "%20"), chapter=chapter_number)
    try:
        resp = requests.get(remote_url, timeout=10)
        resp.raise_for_status()
        remote_json = resp.json()
    except Exception:
        return None

    if isinstance(remote_json, dict) and "verses" in remote_json and isinstance(remote_json["verses"], list):
        verses_list: List[Dict[str,str]] = []
        for verse_entry in remote_json["verses"]:
            verse_num = str(verse_entry.get("verse") or verse_entry.get("verse_number") or "")
            verse_text = verse_entry.get("text") or verse_entry.get("content") or ""
            verses_list.append({"verse": verse_num, "text": verse_text})
        try:
            with open(cache_path, "w", encoding="utf-8") as cache_file:
                json.dump(verses_list, cache_file, ensure_ascii=False, indent=2)
        except Exception:
            pass
        time.sleep(REMOTE_FETCH_DELAY_SECONDS)
        return verses_list

    if isinstance(remote_json, dict) and "text" in remote_json and isinstance(remote_json["text"], str):
        raw_text = remote_json["text"]
        candidate_verses: List[Dict[str,str]] = []
        for match in re.finditer(r"(\d+)\s+([^\n]+)", raw_text):
            candidate_verses.append({"verse": match.group(1), "text": match.group(2).strip()})
        if candidate_verses:
            try:
                with open(cache_path, "w", encoding="utf-8") as cache_file:
                    json.dump(candidate_verses, cache_file, ensure_ascii=False, indent=2)
            except Exception:
                pass
            time.sleep(REMOTE_FETCH_DELAY_SECONDS)
            return candidate_verses

    return None

# ---------------------------
# Searching utilities
# ---------------------------
def build_search_regex(search_keyword: str, require_whole_word: bool) -> re.Pattern:
    escaped_keyword = re.escape(search_keyword.strip())
    pattern_text = escaped_keyword
    if require_whole_word:
        pattern_text = r"\b" + pattern_text + r"\b"
    return re.compile(pattern_text, re.IGNORECASE)

def find_matches_in_bible(
    search_keyword: str,
    local_bible_data: Optional[BibleStructureType] = None,
    require_whole_word: bool = False,
    restrict_to_testament: Optional[str] = None,
    restrict_to_book: Optional[str] = None,
    maximum_results: Optional[int] = None
) -> List[VerseMatch]:
    compiled_pattern = build_search_regex(search_keyword, require_whole_word)
    results: List[VerseMatch] = []

    books_to_search = CANONICAL_BOOK_ORDER.copy()
    if restrict_to_testament:
        if restrict_to_testament.lower() == "old":
            books_to_search = CANONICAL_BOOK_ORDER[:39]
        elif restrict_to_testament.lower() == "new":
            books_to_search = CANONICAL_BOOK_ORDER[39:]
    if restrict_to_book:
        candidate_normalized = restrict_to_book.strip().title()
        if candidate_normalized in BOOK_TO_CANONICAL_INDEX:
            books_to_search = [candidate_normalized]
        else:
            found_book = None
            lower_request = restrict_to_book.strip().lower().replace(".", "")
            for book_name in CANONICAL_BOOK_ORDER:
                if lower_request in book_name.lower().replace(" ", "").replace(".", ""):
                    found_book = book_name
                    break
            if found_book:
                books_to_search = [found_book]

    for book_name in books_to_search:
        if local_bible_data and book_name in local_bible_data:
            chapters_for_book = local_bible_data[book_name]
            for chapter_str in sorted(chapters_for_book.keys(), key=lambda s: int(s) if str(s).isdigit() else s):
                chapter_int = int(chapter_str) if str(chapter_str).isdigit() else 0
                verse_list = chapters_for_book[chapter_str]
                for verse_entry in verse_list:
                    verse_num = int(verse_entry.get("verse") or 0)
                    verse_text = verse_entry.get("text") or ""
                    if compiled_pattern.search(verse_text):
                        results.append(VerseMatch(book_name, chapter_int, verse_num, verse_text))
                        if maximum_results and len(results) >= maximum_results:
                            break
                if maximum_results and len(results) >= maximum_results:
                    break
            if maximum_results and len(results) >= maximum_results:
                break
        else:
            for candidate_chapter in range(1, 201):
                chapter_cache_path = cache_filename_for_chapter(book_name, candidate_chapter)
                verse_list = None
                if os.path.isfile(chapter_cache_path):
                    try:
                        with open(chapter_cache_path, "r", encoding="utf-8") as cache_file:
                            verse_list = json.load(cache_file)
                    except Exception:
                        verse_list = None
                else:
                    verse_list = fetch_chapter_and_cache(book_name, candidate_chapter)
                if not verse_list:
                    break
                for verse_item in verse_list:
                    verse_num = int(verse_item.get("verse") or 0)
                    verse_text = verse_item.get("text") or ""
                    if compiled_pattern.search(verse_text):
                        results.append(VerseMatch(book_name, candidate_chapter, verse_num, verse_text))
                        if maximum_results and len(results) >= maximum_results:
                            break
                if maximum_results and len(results) >= maximum_results:
                    break
            if maximum_results and len(results) >= maximum_results:
                break

    results.sort(key=lambda vm: vm.canonical_sort_key())
    return results

# ---------------------------
# Interactive prompts & argument parsing
# ---------------------------
def interactive_prompt_for_string(prompt_text: str, default_value: Optional[str] = None) -> str:
    if default_value is None:
        prompt_suffix = ": "
    else:
        prompt_suffix = f" [{default_value}]: "
    try:
        entered = input(prompt_text + prompt_suffix).strip()
    except EOFError:
        entered = ""
    if entered == "":
        return default_value or ""
    return entered

def interactive_prompt_for_yes_no(prompt_text: str, default_yes: bool = True) -> bool:
    default_marker = "Y/n" if default_yes else "y/N"
    try:
        entered = input(f"{prompt_text} ({default_marker}): ").strip().lower()
    except EOFError:
        entered = ""
    if entered == "":
        return default_yes
    return entered in ("y", "yes")

def parse_command_line_arguments_with_interactive_fallback() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bible keyword/phrase search (interactive fallback)")
    parser.add_argument("--keyword", "-k", required=False, help="Keyword or phrase to search for.")
    parser.add_argument("--whole-word", action="store_true", help="Match whole words only.")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of results to return.")
    parser.add_argument("--testament", choices=["old", "new"], help="Limit search to 'old' or 'new' testament.")
    parser.add_argument("--book", help="Limit search to a single book (name or partial match).")
    parser.add_argument("--local-file", default=DEFAULT_LOCAL_BIBLE_FILENAME, help=f"Local bible filename (default: {DEFAULT_LOCAL_BIBLE_FILENAME}).")
    parser.add_argument("--source-url", help="Optional raw JSON URL to try when building local bible file.")
    args = parser.parse_args()

    # If running in a terminal (interactive), prompt for missing values
    if sys.stdin.isatty():
        if not args.keyword:
            args.keyword = ""
            while not args.keyword:
                args.keyword = interactive_prompt_for_string("Enter search keyword or phrase (required)").strip()
        # ask if exact phrase match is desired
        wants_phrase_mode = interactive_prompt_for_yes_no("Treat the input as an exact phrase (vs keyword anywhere)?", default_yes=False)
        # whole-word option
        wants_whole_word = interactive_prompt_for_yes_no("Require whole-word matches only?", default_yes=False)
        # limit
        limit_input = interactive_prompt_for_string("Maximum results to return (press Enter for no limit)", default_value="")
        parsed_limit = None
        if limit_input:
            try:
                parsed_limit = int(limit_input)
            except Exception:
                parsed_limit = None
        # testament
        testament_input = interactive_prompt_for_string("Limit to testament? (old/new) or press Enter for both", default_value="")
        testament_choice = testament_input.lower() if testament_input.lower() in ("old", "new") else None
        # book
        book_input = interactive_prompt_for_string("Limit to a single book (name or partial) or press Enter for all", default_value="")
        # source URL for downloader
        source_url_input = interactive_prompt_for_string("Optional source URL to download a full JSON bible (press Enter to try defaults)", default_value="")

        # Map interactive answers back into args object expected by the rest of the script
        # We use 'phrase mode' by converting it into a search keyword that will be used verbatim below.
        args.phrase = wants_phrase_mode
        args.whole_word = wants_whole_word
        args.limit = parsed_limit
        args.testament = testament_choice
        args.book = book_input or None
        args.source_url = source_url_input or None
    else:
        # Non-interactive environment (e.g., piped runs) -> require keyword
        if not args.keyword:
            parser.error("A search keyword is required in non-interactive mode (--keyword/-k).")
        # ensure default attributes exist
        args.phrase = False
        args.whole_word = bool(args.whole_word)
    return args

# ---------------------------
# Build local bible if missing
# ---------------------------
def attempt_build_local_bible(local_filename: str, user_provided_source_url: Optional[str] = None) -> Optional[BibleStructureType]:
    if user_provided_source_url:
        candidates = [("User provided", user_provided_source_url)]
    else:
        candidates = []
    candidates.extend(CANDIDATE_RAW_JSON_SOURCES)

    last_diagnostic = None
    for label, url in candidates:
        normalized_structure, diagnostic = attempt_download_and_normalize_from_source(label, url)
        if normalized_structure:
            success = write_local_bible_file(normalized_structure, local_filename)
            if success:
                print(f"Saved normalized local bible to: {local_filename}")
                return normalized_structure
            else:
                print(f"[!] Normalized data found but failed to write {local_filename}.")
                return None
        last_diagnostic = diagnostic

    print("[!] Failed to automatically produce a normalized local bible file.")
    if last_diagnostic:
        print("Last diagnostic hint:", last_diagnostic)
    return None

# ---------------------------
# Main
# ---------------------------
def main():
    args = parse_command_line_arguments_with_interactive_fallback()

    # If phrase mode is active, we use the input verbatim (don't split). For our search engine that distinction
    # only affects how the user perceives search; regex is built from the full string.
    search_keyword = args.keyword.strip()
    require_whole_word_flag = bool(args.whole_word)
    maximum_results = args.limit
    restrict_testament = args.testament
    restrict_book = args.book
    local_file_path = args.local_file
    user_source_url = getattr(args, "source_url", None)

    # Ensure local Bible exists (try to load; if missing, attempt download)
    local_bible_data = load_local_bible_file(local_file_path)
    if local_bible_data is None:
        print(f"Local bible file '{local_file_path}' not found. Attempting automatic download/normalize...")
        local_bible_data = attempt_build_local_bible(local_file_path, user_source_url)

    if local_bible_data is None:
        print("Proceeding with remote per-chapter fetch fallback (will cache chapters).")

    # Run search
    matches = find_matches_in_bible(
        search_keyword=search_keyword,
        local_bible_data=local_bible_data,
        require_whole_word=require_whole_word_flag,
        restrict_to_testament=restrict_testament,
        restrict_to_book=restrict_book,
        maximum_results=maximum_results
    )

    if not matches:
        print("No matches found.")
        return

    # Print matches with modest formatting and highlighting of matched text
    # For simplicity, highlight by surrounding match with ** markers (console-friendly)
    highlight_pattern = re.compile(re.escape(search_keyword), re.IGNORECASE)
    for match in matches:
        display_text = match.verse_text
        try:
            display_text = highlight_pattern.sub(lambda m: f"**{m.group(0)}**", display_text)
        except re.error:
            # fallback: no highlighting if regex fails (shouldn't happen)
            pass
        print(f"{match.reference_string()} — {display_text}")

if __name__ == "__main__":
    main()
