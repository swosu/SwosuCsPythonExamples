"""
batch_fetch_movies.py

Batch harvester for OMDb.

Goal:
- Systematically walk through "prefix" searches (0-9, a-z)
- For each prefix, walk pages 1..N (up to OMDb's 100-page limit)
- For each search hit, fetch FULL details by imdbID
- Append results to movies_batch.csv
- Remember where we left off using batch_state.json
- Respect a daily request budget so we don't hammer the API

Usage (typical, once per day):

    python batch_fetch_movies.py

You can also override the daily budget:

    python batch_fetch_movies.py 500
"""

import csv
import json
import sys
import time
from pathlib import Path
from typing import Any

import requests

# --- CONFIG -------------------------------------------------------------

API_KEY = "7ad6b576"  # TODO: for public repos, load this from an env var or config file
BASE_URL = "http://www.omdbapi.com/"

CSV_FILE = "movies_batch.csv"
STATE_FILE = "batch_state.json"

# OMDb free keys are limited to ~1000 requests/day.
# We'll stay safely under that by default.
DEFAULT_DAILY_BUDGET = 800  # total HTTP requests (search + detail)

# OMDb returns up to 10 results per search page, and allows pages 1..100.
MAX_PAGES_PER_PREFIX = 100

# We will iterate through these search prefixes in order.
PREFIXES = list("0123456789abcdefghijklmnopqrstuvwxyz")


# --- HELPERS ------------------------------------------------------------

class DailyLimitReached(Exception):
    """Raised when OMDb reports a daily request limit issue."""
    pass


def search_movies_page(query: str, page: int) -> list[dict[str, Any]]:
    """
    Use the OMDb 's' search parameter to get ONE PAGE of results.
    Returns a list of basic movie dicts from the 'Search' field.
    Raises DailyLimitReached if OMDb says we've hit a request limit.
    """
    params = {
        "apikey": API_KEY.strip(),
        "s": query,
        "type": "movie",
        "page": page,
    }

    print(f"[OMDb] Search '{query}' page {page}...")
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()

    if data.get("Response") == "False":
        error_msg = (data.get("Error") or "").lower()
        print(f"[OMDb] Search error: {data.get('Error')}")
        if "limit" in error_msg and "request" in error_msg:
            # e.g. "Request limit reached!"
            raise DailyLimitReached(data.get("Error"))
        # Other errors: "Movie not found!", "Too many results.", etc.
        return []

    results = data.get("Search", [])
    print(f"[OMDb] Page {page} returned {len(results)} results.")
    return results


def fetch_movie_details(imdb_id: str) -> dict[str, Any] | None:
    """
    Given an IMDb ID, fetch FULL movie details using 'i='.
    Returns a dict of movie data, or None if something goes wrong.
    Raises DailyLimitReached if OMDb says we've hit a request limit.
    """
    params = {
        "apikey": API_KEY.strip(),
        "i": imdb_id,
        "plot": "short",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()
    except Exception as e:
        print(f"[OMDb] Network error fetching {imdb_id}: {e}")
        return None

    if data.get("Response") == "False":
        error_msg = (data.get("Error") or "").lower()
        print(f"[OMDb] Detail error for {imdb_id}: {data.get('Error')}")
        if "limit" in error_msg and "request" in error_msg:
            raise DailyLimitReached(data.get("Error"))
        return None

    return data


def load_existing_ids(csv_path: Path) -> set[str]:
    """
    Read the existing CSV (if any) and return a set of imdbIDs.
    This lets us avoid adding duplicates when we fetch more later.
    """
    if not csv_path.exists():
        return set()

    ids: set[str] = set()
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            imdb_id = row.get("imdbID")
            if imdb_id:
                ids.add(imdb_id)

    return ids


def save_movies(csv_path: Path, movies: list[dict[str, Any]]) -> None:
    """
    Append movie detail records to the CSV file.
    If the file doesn't exist yet, write a header.
    We grab a wide set of OMDb fields so you can enjoy missing data.
    """
    fieldnames = [
        "imdbID",
        "Title",
        "Year",
        "Rated",
        "Released",
        "Runtime",
        "Genre",
        "Director",
        "Writer",
        "Actors",
        "Plot",
        "Language",
        "Country",
        "Awards",
        "Poster",
        "Metascore",
        "imdbRating",
        "imdbVotes",
        "Type",
        "DVD",
        "BoxOffice",
        "Production",
        "Website",
        "RatingsSummary",  # flattened from Ratings list
    ]

    file_exists = csv_path.exists()

    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for m in movies:
            ratings_list = m.get("Ratings", [])
            ratings_summary = "; ".join(
                f"{r.get('Source')}: {r.get('Value')}"
                for r in ratings_list
                if r.get("Source") and r.get("Value")
            )

            row = {
                "imdbID": m.get("imdbID", ""),
                "Title": m.get("Title", ""),
                "Year": m.get("Year", ""),
                "Rated": m.get("Rated", ""),
                "Released": m.get("Released", ""),
                "Runtime": m.get("Runtime", ""),
                "Genre": m.get("Genre", ""),
                "Director": m.get("Director", ""),
                "Writer": m.get("Writer", ""),
                "Actors": m.get("Actors", ""),
                "Plot": m.get("Plot", ""),
                "Language": m.get("Language", ""),
                "Country": m.get("Country", ""),
                "Awards": m.get("Awards", ""),
                "Poster": m.get("Poster", ""),
                "Metascore": m.get("Metascore", ""),
                "imdbRating": m.get("imdbRating", ""),
                "imdbVotes": m.get("imdbVotes", ""),
                "Type": m.get("Type", ""),
                "DVD": m.get("DVD", ""),
                "BoxOffice": m.get("BoxOffice", ""),
                "Production": m.get("Production", ""),
                "Website": m.get("Website", ""),
                "RatingsSummary": ratings_summary,
            }

            writer.writerow(row)


def load_state(state_path: Path) -> tuple[int, int]:
    """
    Load batch state:
        prefix_index: index into PREFIXES
        page:         current page for that prefix

    If no state exists yet, start at (0, 1).
    """
    if not state_path.exists():
        return 0, 1

    try:
        with state_path.open(encoding="utf-8") as f:
            data = json.load(f)
        prefix_index = int(data.get("prefix_index", 0))
        page = int(data.get("page", 1))
        return prefix_index, page
    except Exception as e:
        print(f"[State] Failed to load state ({e}), starting from beginning.")
        return 0, 1


def save_state(state_path: Path, prefix_index: int, page: int) -> None:
    """
    Save where we left off so the next run can continue.
    """
    data = {
        "prefix_index": prefix_index,
        "page": page,
    }
    with state_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[State] Saved state: prefix_index={prefix_index}, page={page}")


# --- MAIN BATCH LOGIC ---------------------------------------------------

def main():
    # Daily budget may optionally be passed on the command line.
    if len(sys.argv) >= 2:
        try:
            daily_budget = int(sys.argv[1])
        except ValueError:
            print("Usage: python batch_fetch_movies.py [daily_budget]")
            sys.exit(1)
    else:
        daily_budget = DEFAULT_DAILY_BUDGET

    print(f"[Config] Daily request budget: {daily_budget}")

    csv_path = Path(CSV_FILE)
    state_path = Path(STATE_FILE)

    # Load state: where did we leave off last run?
    prefix_index, page = load_state(state_path)
    print(f"[State] Starting at prefix_index={prefix_index}, page={page}")

    if prefix_index >= len(PREFIXES):
        print("[Info] We've already exhausted all prefixes. Nothing more to do.")
        return

    existing_ids = load_existing_ids(csv_path)
    print(f"[Local] Found {len(existing_ids)} existing movies in {CSV_FILE}")

    requests_used = 0
    detailed_movies: list[dict[str, Any]] = []

    try:
        while requests_used < daily_budget and prefix_index < len(PREFIXES):
            prefix = PREFIXES[prefix_index]
            if page > MAX_PAGES_PER_PREFIX:
                # Move to next prefix
                prefix_index += 1
                page = 1
                continue

            # --- Search page for current prefix ---
            search_results = search_movies_page(prefix, page)
            requests_used += 1  # one HTTP request used

            if not search_results:
                # No more results for this prefix; move on.
                print(f"[OMDb] No more results for prefix '{prefix}'.")
                prefix_index += 1
                page = 1
                continue

            # --- For each basic result, fetch full details ---
            total_results = len(search_results)
            for i, m in enumerate(search_results, start=1):
                if requests_used >= daily_budget:
                    print("[Info] Hit daily budget while fetching details.")
                    break

                imdb_id = m.get("imdbID")
                if not imdb_id:
                    continue

                if imdb_id in existing_ids:
                    print(f"[Local] Skipping {imdb_id} (already in CSV).")
                    continue

                print(
                    f"[Detail] Prefix '{prefix}' page {page} "
                    f"item {i}/{total_results}: {imdb_id}"
                )

                details = fetch_movie_details(imdb_id)
                requests_used += 1

                if details:
                    detailed_movies.append(details)
                    existing_ids.add(imdb_id)

                    # Be polite to the API
                    time.sleep(0.2)

            # Move on to next page for this prefix
            page += 1

    except DailyLimitReached as e:
        print(f"[OMDb] Daily limit reached according to API: {e}")
        print("[Info] Stopping early and saving progress.")
    finally:
        # Save whatever we fetched this run
        if detailed_movies:
            save_movies(csv_path, detailed_movies)
            print(
                f"[Local] Saved {len(detailed_movies)} new movies to "
                f"{csv_path.resolve()}"
            )
        else:
            print("[Local] No new movies to save this run.")

        # Save state for next run
        save_state(state_path, prefix_index, page)


if __name__ == "__main__":
    main()
