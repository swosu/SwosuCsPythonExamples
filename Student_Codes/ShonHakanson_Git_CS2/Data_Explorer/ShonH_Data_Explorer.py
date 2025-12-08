import requests
import json
import time 
import sys
import matplotlib.pyplot as plt
import csv

from models import (
    FoodProduct, 
    create_product_from_api_data, 
    linear_search_products, 
    binary_search_products,
    sort_products_by_nutriscore,
    sort_products_by_energy,
    sort_products_by_category,
    sort_products_by_name,
    load_products_from_csv,

    # NEW imports
    insertion_sort_by_nutriscore,
    insertion_sort_by_energy,
    insertion_sort_by_category,
    insertion_sort_by_name
)

CUSTOM_USER_AGENT = 'ShonH_Data_Explorer.py/1.0 (shonhakanson@yahoo.com)' 
HEADERS = {'User-Agent': CUSTOM_USER_AGENT}
BASE_SEARCH_URL = 'https://world.openfoodfacts.org/cgi/search.pl'


# ================================================================
# API DATA LOADING
# ================================================================
def fetch_products_by_search(query: str, limit: int = 100) -> list[FoodProduct]:
    print(f"\nSearching API for: '{query}'...")
    params = {
        'search_terms': query, 'page_size': limit, 'json': 1,
        'fields': 'code,product_name,nutriscore_grade,nutriments,categories'
    }
    try:
        response = requests.get(BASE_SEARCH_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        raw_products = data.get('products', [])
        if not raw_products:
            print("No results found for that query.")
            return []

        product_list = []
        for raw_product in raw_products:
            product_obj = create_product_from_api_data(raw_product)
            if product_obj:
                product_list.append(product_obj)

        print(f"Successfully loaded {len(product_list)} valid products.")
        time.sleep(1)
        return product_list
    
    except requests.exceptions.RequestException as e:
        print(f"\n🛑 API Error: {e}")
        return []


# ================================================================
# SEARCH MENU
# ================================================================
def search_menu(records: list[FoodProduct]):
    if not records:
        print("🛑 Data not loaded. Use Option 1 first.")
        return

    while True:
        print("\n--- Search Menu ---")
        print("1. Linear Search (keyword in name)")
        print("2. Binary Search (exact name match)")
        print("3. Back")
        choice = input("Enter search option: ")

        if choice == '1':
            search_key = input("Enter keyword: ")
            results = linear_search_products(records, search_key)
            break

        elif choice == '2':
            search_key = input("Enter exact product name: ")
            results = binary_search_products(records, search_key)
            break

        elif choice == '3':
            return

        else:
            print("Invalid option.")

    if results:
        print(f"\nFound {len(results)} results (showing up to 5):")
        for r in results[:5]:
            print(r)
    else:
        print("No matches found.")


# ================================================================
# SORT MENU (UPDATED — NOW HAS TIMSORT + INSERTION SORT)
# ================================================================
def sort_menu(records: list[FoodProduct]) -> list[FoodProduct]:
    if not records:
        print("🛑 Data not loaded.")
        return records

    while True:
        print("\n--- Sort Menu ---")
        print("1. Nutri-score")
        print("2. Energy")
        print("3. Category")
        print("4. Name")
        print("5. Back")
        choice = input("Enter choice: ")

        if choice == '5':
            return records

        # Ask which sorting algorithm
        print("\nChoose sorting method:")
        print("1. Python sort() (Timsort)")
        print("2. Insertion Sort (manual)")
        method = input("Enter method: ")

        # Nutriscore
        if choice == '1':
            if method == '1':
                return sort_products_by_nutriscore(records)
            else:
                return insertion_sort_by_nutriscore(records)

        # Energy
        elif choice == '2':
            if method == '1':
                return sort_products_by_energy(records)
            else:
                return insertion_sort_by_energy(records)

        # Category
        elif choice == '3':
            if method == '1':
                return sort_products_by_category(records)
            else:
                return insertion_sort_by_category(records)

        # Name
        elif choice == '4':
            if method == '1':
                return sort_products_by_name(records)
            else:
                return insertion_sort_by_name(records)

        else:
            print("Invalid option.")


# ================================================================
# FILE SAVING (unchanged)
# ================================================================
def save_menu(records: list[FoodProduct]):
    if not records:
        print("🛑 No data to save.")
        return

    filename = input("Enter filename to save (example: foods.csv): ")

    try:
        with open(filename, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Barcode", "Name", "NutriScore", "Energy", "Category"])
            for p in records:
                writer.writerow([p.barcode, p.name, p.nutriscore, p.energy, p.category])

        print(f"\n✅ Saved {len(records)} records to {filename}")

    except Exception as e:
        print(f"\n❌ Error saving file: {e}")


# ================================================================
# PLOTTING (unchanged)
# ================================================================
def plot_energy_histogram(products: list[FoodProduct]):
    energies = []

    for p in products:
        try:
            energies.append(float(p.energy))
        except ValueError:
            continue

    if not energies:
        print("🛑 No valid numeric energy values to plot.")
        return

    plt.figure()
    plt.hist(energies, bins=10)
    plt.title("Energy (kJ) Distribution")
    plt.xlabel("Energy (kJ)")
    plt.ylabel("Frequency")
    plt.show()


def plot_category_bar_chart(products: list[FoodProduct]):
    from collections import Counter

    categories = [p.category for p in products if p.category not in ("", "N/A")]
    
    if not categories:
        print("🛑 No categories to plot.")
        return

    counts = Counter(categories)

    plt.figure()
    plt.bar(counts.keys(), counts.values())
    plt.xticks(rotation=45, ha="right")
    plt.title("Category Frequency (Top 20 Records)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()


def plot_data_menu(records: list[FoodProduct]):
    print("\n--- Plotting Menu ---")
    print("1. Use currently loaded API results (Top 20)")
    print("2. Load products from a saved CSV")
    print("3. Back")
    choice = input("Choose option: ")

    if choice == '1':
        if not records:
            print("🛑 No API data loaded.")
            return
        products = records[:20]

    elif choice == '2':
        filename = input("Enter CSV filename: ")
        products = load_products_from_csv(filename)
        if not products:
            return
        products = products[:20]

    else:
        return

    print("\nPlot Options:")
    print("1. Energy Histogram")
    print("2. Category Bar Chart")
    p = input("Choose plot type: ")

    if p == '1':
        plot_energy_histogram(products)
    elif p == '2':
        plot_category_bar_chart(products)
    else:
        print("Invalid plot choice.")


# ================================================================
# MAIN MENU (unchanged)
# ================================================================
def main_menu():
    data_records: list[FoodProduct] = [] 

    while True:
        print("\n--- Data Explorer Main Menu ---")
        print(f"Current Records in Memory: {len(data_records)}")
        print("1. Load Data (API Search)")
        print("2. Display Records (Top 20)")
        print("3. Search Records")
        print("4. Sort Records")
        print("5. Save Records to CSV")
        print("6. Plot Data")
        print("7. Quit")
        
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                search_term = input("Enter a search term: ")
                data_records = fetch_products_by_search(search_term)

            elif choice == '2':
                if data_records:
                    print("\n--- Top 20 Records ---")
                    for i, r in enumerate(data_records[:20]):
                        print(f"{i+1}. {r}")
                else:
                    print("No data loaded.")

            elif choice == '3':
                search_menu(data_records)

            elif choice == '4':
                data_records = sort_menu(data_records)

            elif choice == '5':
                save_menu(data_records)

            elif choice == '6':
                plot_data_menu(data_records)

            elif choice == '7':
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")
                
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main_menu()
