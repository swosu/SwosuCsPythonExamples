# app.py
import requests
import json
import time 
import sys # For a quick exit on errors

# Import ALL worker functions from models.py
from models import (
    FoodProduct, 
    create_product_from_api_data, 
    linear_search_products, 
    binary_search_products,
    sort_products_by_nutriscore,
    sort_products_by_energy,
    sort_products_by_category,
    sort_products_by_name
)

# Configuration
CUSTOM_USER_AGENT = 'ShonH_Data_Explorer.py/1.0 (shonhakanson@yahoo.com)' 
HEADERS = {'User-Agent': CUSTOM_USER_AGENT}
BASE_SEARCH_URL = 'https://world.openfoodfacts.org/cgi/search.pl'

# --- API FETCH FUNCTION (Remains the same) ---
def fetch_products_by_search(query: str, limit: int = 100) -> list[FoodProduct]:
    """Fetches a list of products from the OFF API."""
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
        if '429' in str(e):
             print(f"\n🛑 Error fetching data from API: Rate limit hit (429 Too Many Requests). Please wait 60 seconds.")
        else:
             print(f"\n🛑 Error fetching data from API (check network/connection): {e}")
        return []

# --- NEW SUB-MENU FUNCTIONS ---

def search_menu(records: list[FoodProduct]):
    """Sub-menu for choosing a search type."""
    if not records:
        print("🛑 Data not loaded. Use Option 1 first.")
        return

    while True:
        print("\n--- Search Menu ---")
        print("1. Linear Search (Finds keyword in Product Name)")
        print("2. Binary Search (Finds EXACT Product Name)")
        print("3. Back to Main Menu")
        choice = input("Enter search option: ")

        if choice == '1':
            search_key = input("Enter product name or keyword (Linear Search): ")
            results = linear_search_products(records, search_key)
            break
        
        elif choice == '2':
            search_key = input("Enter product name (EXACT match for Binary Search): ")
            results = binary_search_products(records, search_key)
            break
            
        elif choice == '3':
            return # Exit back to main_menu loop
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
            continue
    
    # Display search results after breaking the loop
    if results:
        print(f"\n✅ Found {len(results)} matching products (showing top 5):")
        for i, record in enumerate(results[:5]):
            print(f"{i+1}. {record}")
    else:
        print("No products matched your search term.")

def sort_menu(records: list[FoodProduct]) -> list[FoodProduct]:
    """Sub-menu for choosing a field to sort by."""
    if not records:
        print("🛑 Data not loaded. Use Option 1 first.")
        return records

    while True:
        print("\n--- Sort Menu (Timsort) ---")
        print("1. Sort by Nutri-Score (A -> E)")
        print("2. Sort by Energy (Low -> High)")
        print("3. Sort by Category (A -> Z)")
        print("4. Sort by Product Name (A -> Z)")
        print("5. Back to Main Menu (Keep Current Order)")
        choice = input("Enter sort option: ")

        if choice == '1':
            records = sort_products_by_nutriscore(records)
            print("\n✅ Records sorted by Nutri-Score (A to E).")
            break
        elif choice == '2':
            records = sort_products_by_energy(records)
            print("\n✅ Records sorted by Energy (Low to High).")
            break
        elif choice == '3':
            records = sort_products_by_category(records)
            print("\n✅ Records sorted by Category (A to Z).")
            break
        elif choice == '4':
            records = sort_products_by_name(records)
            print("\n✅ Records sorted by Name (A to Z).")
            break
        elif choice == '5':
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid option. Please choose 1-5.")
            continue

    return records # Return the sorted list

def save_menu(records: list[FoodProduct]):
    """Implements the requirement to save results to a file (CSV)."""
    if not records:
        print("🛑 No data in memory to save.")
        return

    filename = input("Enter filename to save (e.g., 'filtered_data.csv'): ")

    try:
        
        with open(filename, 'w', encoding='utf-8') as f:
            # Write header row
            f.write("Barcode,Name,Nutri-Score,Energy(kJ),Category\n")
            
            # Write data rows
            for product in records:
                # Format data for CSV line
                line = f"{product.barcode},{product.name},{product.nutriscore},{product.energy},{product.category}\n"
                f.write(line)
        
        print(f"\n✅ Successfully saved {len(records)} records to {filename}")

    except Exception as e:
        
        print(f"\n❌ Error saving file: {e}")
        time.sleep(1)


# --- MAIN MENU LOOP ---
def main_menu():
    """Main application loop."""
    
    data_records: list[FoodProduct] = [] 

    while True:
        print("\n--- Data Explorer Main Menu ---")
        print(f"Current Records in Memory: {len(data_records)}")
        print("1. Load Data (API Search)")
        print("2. Display Records (Top 20)")
        print("3. Search Records (Open Search Menu)")
        print("4. Sort Records (Open Sort Menu)")
        print("5. Save Current Records to File (.csv)") # NEW REQUIREMENT
        print("6. Quit")
        
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                search_term = input("Enter a food category or search term (e.g., 'yogurt' or 'vegan'): ")
                data_records = fetch_products_by_search(search_term, limit=100) 
                
            elif choice == '2':
                if data_records:
                    print("\n--- Top 20 Records ---")
                    for i, record in enumerate(data_records[:20]): 
                        print(f"{i+1}. {record}")
                else:
                    print("No data loaded yet. Use option 1.")
            
            # Use the new sub-menus
            elif choice == '3': 
                search_menu(data_records)
            
            elif choice == '4':
                # Update data_records with the new sorted list returned from sort_menu
                data_records = sort_menu(data_records)

            elif choice == '5':
                save_menu(data_records) # Call the new save function
                
            elif choice == '6':
                print("Exiting Data Explorer. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except ValueError:
            print("Invalid input. Please enter a valid menu number.")
        except KeyboardInterrupt:
            print("\n\nKeyboard interrupt detected. Exiting Data Explorer.")
            sys.exit(0)


# To run the app:
if __name__ == "__main__":
    main_menu()