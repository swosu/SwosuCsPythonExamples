"""
fetch_movies.py

Use the OMDb API to search for movies and store results in a persistent CSV file.

Usage (from this folder, with your venv active):

    python fetch_movies.py "star wars" 3

This will:
- Search OMDb for "star wars"
- Grab up to 3 pages of results (10 per page, max 30 movies)
- Append any NEW movies to movies.csv (no duplicate imdbIDs)
"""

import csv
import sys
from pathlib import Path

import requests

API_KEY = "7ad6b576"   # TODO: for students, replace with "YOUR_OMDB_API_KEY_HERE"
BASE_URL = "http://www.omdbapi.com/"
CSV_FILE = "movies.csv"


def search_movies(query: str, max_pages: int = 1):
    """
    Use the OMDb 's' search parameter to find movies matching the query.
    Returns a list of movie dicts from the 'Search' field.
    """
    all_results = []

    for page in range(1, max_pages + 1):
        params = {
            "apikey": API_KEY.strip(),
            "s": query,
            "type": "movie",
            "page": page,
        }

        print(f"[OMDb] Searching '{query}' page {page}...")
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if data.get("Response") == "False":
            # Example: "Movie not found!", "Too many results."
            print(f"[OMDb] Stopping: {data.get('Error')}")
            break

        page_results = data.get("Search", [])
        print(f"[OMDb] Got {len(page_results)} results on page {page}")
        all_results.extend(page_results)

    return all_results


def load_existing_ids(csv_path: Path) -> set[str]:
    """
    Read the existing CSV (if any) and return a set of imdbIDs.
    This lets us avoid adding duplicates when we fetch more data later.
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


def save_movies(csv_path: Path, movies):
    """
    Append movies to the CSV file. If the file doesn't exist yet, write a header.
    """
    fieldnames = ["imdbID", "Title", "Year", "Type", "Poster"]
    file_exists = csv_path.exists()

    with csv_path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for m in movies:
            row = {
                "imdbID": m.get("imdbID", ""),
                "Title": m.get("Title", ""),
                "Year": m.get("Year", ""),
                "Type": m.get("Type", ""),
                "Poster": m.get("Poster", ""),
            }
            writer.writerow(row)


def main():
    # -----------------------------
    # Parse command-line arguments
    # -----------------------------
    if len(sys.argv) < 2:
        print("Usage: python fetch_movies.py <search term> [max_pages]")
        print("Example: python fetch_movies.py \"star wars\" 3")
        sys.exit(1)

    query = sys.argv[1]
    try:
        max_pages = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
    except ValueError:
        print("Error: max_pages must be an integer.")
        sys.exit(1)

    csv_path = Path(CSV_FILE)

    # -----------------------------
    # Load existing IDs
    # -----------------------------
    existing_ids = load_existing_ids(csv_path)
    print(f"[Local] Found {len(existing_ids)} existing movies in {CSV_FILE}")

    # -----------------------------
    # Fetch from OMDb
    # -----------------------------
    movies = search_movies(query, max_pages=max_pages)
    print(f"[OMDb] Total fetched this run: {len(movies)}")

    # -----------------------------
    # Filter out duplicates
    # -----------------------------
    new_movies = [m for m in movies if m.get("imdbID") not in existing_ids]
    print(f"[Local] New movies to add: {len(new_movies)}")

    # -----------------------------
    # Save to CSV
    # -----------------------------
    if new_movies:
        save_movies(csv_path, new_movies)
        print(f"[Local] Saved {len(new_movies)} new movies to {csv_path.resolve()}")
    else:
        print("[Local] Nothing new to save.")


if __name__ == "__main__":
    main()
