# models.py

class FoodProduct:
    """Represents a single food product record for the Data Explorer."""
    def __init__(self, barcode, name, nutriscore, energy, category):
        self.barcode = barcode
        self.name = name
        self.nutriscore = nutriscore
        self.energy = energy  
        self.category = category
        
    def __str__(self):
        return (f"[{self.nutriscore.upper()}] {self.name[:40]:<40} | "
                f"Category: {self.category} | Energy (kJ): {self.energy}")

def create_product_from_api_data(raw_data: dict) -> 'FoodProduct' or None:
    """Maps raw JSON product data into a FoodProduct object."""
    product_data = raw_data
    barcode = product_data.get('code', 'N/A')
    name = product_data.get('product_name', '').strip()
    if not name or not barcode or barcode == 'N/A':
        return None
    nutriscore = product_data.get('nutriscore_grade', 'N/A')
    nutriments = product_data.get('nutriments', {})
    energy = nutriments.get('energy_100g', '0')
    categories = product_data.get('categories', '')
    category = categories.split(',')[0].strip() if categories else 'N/A'
    return FoodProduct(barcode, name, nutriscore, energy, category)


# --- SEARCH ALGORITHMS ---

def linear_search_products(records: list['FoodProduct'], search_term: str) -> list['FoodProduct']:
    """Implements the required Linear Search algorithm."""
    results = []
    search_term_lower = search_term.lower() 
    for product in records:
        if search_term_lower in product.name.lower():
            results.append(product)
    return results

def binary_search_products(records: list['FoodProduct'], search_term: str) -> list['FoodProduct']:
    """Implements Binary Search (requires data to be sorted by name internally)."""
    results = []
    sorted_records = sorted(records, key=lambda p: p.name.lower())
    low = 0
    high = len(sorted_records) - 1
    search_term_lower = search_term.lower()

    while low <= high:
        mid = (low + high) // 2
        product_name_lower = sorted_records[mid].name.lower()
        
        if product_name_lower == search_term_lower:
            results.append(sorted_records[mid])
            i = mid - 1
            while i >= 0 and sorted_records[i].name.lower() == search_term_lower:
                results.append(sorted_records[i])
                i -= 1
            i = mid + 1
            while i < len(sorted_records) and sorted_records[i].name.lower() == search_term_lower:
                results.append(sorted_records[i])
                i += 1
            break 
        
        elif product_name_lower < search_term_lower:
            low = mid + 1 
        else:
            high = mid - 1
            
    return results

# --- SORT ALGORITHMS (Timsort implementations) ---

def sort_products_by_nutriscore(records: list['FoodProduct']) -> list['FoodProduct']:
    """Sorts products by Nutri-Score (A to E) using Timsort."""
    return sorted(records, key=lambda p: p.nutriscore) 

def sort_products_by_energy(records: list['FoodProduct']) -> list['FoodProduct']:
    """Sorts products by Energy (low to high) using Timsort."""
    # We must ensure the energy field is treated as a number for correct sorting
    return sorted(records, key=lambda p: float(p.energy))

def sort_products_by_category(records: list['FoodProduct']) -> list['FoodProduct']:
    """Sorts products alphabetically by their main category using Timsort."""
    return sorted(records, key=lambda p: p.category.lower())

def sort_products_by_name(records: list['FoodProduct']) -> list['FoodProduct']:
    """Sorts products alphabetically by their name using Timsort."""
    return sorted(records, key=lambda p: p.name.lower())