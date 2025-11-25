import pandas as pd
import requests
import sys

# --- Configuration ---
URL = "https://www.breakingpoint.gg/stats/advanced?timePeriod=2026&orderBy=kd"
OUTPUT_FILENAME = "cdl_advanced_stats.csv"

# --- Main Scraper Function ---
def scrape_cdl_stats():
    """Fetches the CDL advanced stats table and saves it to a CSV."""
    print(f"--- Starting Scraper ---")
    print(f"Fetching data from: {URL}")

    # Set headers to mimic a common web browser. This is often required 
    # to prevent servers from blocking automated scripts.
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # 1. Fetch the raw HTML content
        response = requests.get(URL, headers=headers)
        response.raise_for_status() # Check for HTTP errors (4xx or 5xx)

        # 2. Use pandas to read all HTML tables from the fetched text
        # 'flavor='lxml'' specifies the fast parser we installed.
        tables = pd.read_html(response.text, flavor='lxml')

        if not tables:
            print("❌ Error: No tables detected on the webpage by pandas. This might mean the data is loaded by JavaScript.")
            return

        # 3. Identify the main stats table. The main table is usually the largest one.
        # We find the table (DataFrame) with the maximum number of columns.
        main_table = max(tables, key=lambda x: x.shape[1])
        
        # 4. Data Cleanup Steps
        
        # Drop columns that resulted in all NaNs (often invisible borders/spacers in HTML)
        main_table = main_table.dropna(axis=1, how='all')
        
        # The site uses a complex header structure (e.g., 'HP STATS' over individual metrics).
        # We simplify the column names by keeping only the bottom level (e.g., 'K/D', 'T.E.S', 'HP K/D')
        if isinstance(main_table.columns, pd.MultiIndex):
            # Keep only the last (most specific) level of the multi-index header
            main_table.columns = main_table.columns.get_level_values(-1)

        # Remove the '#' ranking column as it's redundant once sorted
        if '#' in main_table.columns:
            main_table = main_table.drop(columns=['#'])

        # 5. Export the clean data to a CSV file
        main_table.to_csv(OUTPUT_FILENAME, index=False)
        
        print(f"\n✅ Success! Data successfully scraped and saved.")
        print(f"File: {OUTPUT_FILENAME}")
        print(f"Rows: {main_table.shape[0]}, Columns: {main_table.shape[1]}")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ A network error occurred: {e}")
        sys.exit(1)
    except ValueError:
        print("❌ A parsing error occurred. The webpage structure might have changed.")
        sys.exit(1)

if __name__ == "__main__":
    scrape_cdl_stats()