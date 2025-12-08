import csv

class FoodProduct:
    def __init__(self, barcode, name, nutriscore, energy, category):
        self.barcode = barcode
        self.name = name
        self.nutriscore = nutriscore
        self.energy = energy
        self.category = category
        
    def __str__(self):
        return (f"[{self.nutriscore.upper()}] {self.name[:40]:<40} | "
                f"Category: {self.category} | Energy (kJ): {self.energy}")


def create_product_from_api_data(raw_data: dict):
    barcode = raw_data.get('code', '')
    name = raw_data.get('product_name', '').strip()
    if not barcode or not name:
        return None

    nutriscore = raw_data.get('nutriscore_grade', 'N/A')
    nutriments = raw_data.get('nutriments', {})
    energy = nutriments.get('energy_100g', '0')

    categories = raw_data.get('categories', '')
    category = categories.split(',')[0].strip() if categories else 'N/A'

    return FoodProduct(barcode, name, nutriscore, energy, category)


# ================================================================
# CSV LOADING (used for plotting)
# ================================================================
def load_products_from_csv(filename: str) -> list[FoodProduct]:
    products = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    product = FoodProduct(
                        row["Barcode"],
                        row["Name"],
                        row["NutriScore"],
                        row["Energy"],
                        row["Category"]
                    )
                    products.append(product)
                except KeyError:
                    print("🛑 CSV format incorrect.")
                    return []

        print(f"Loaded {len(products)} products from {filename}")
        return products

    except FileNotFoundError:
        print("🛑 File not found.")
        return []
    except Exception as e:
        print(f"🛑 Error reading CSV: {e}")
        return []


# ================================================================
# SEARCHING
# ================================================================
def linear_search_products(records, search_term):
    results = []
    search_term_lower = search_term.lower()
    for product in records:
        if search_term_lower in product.name.lower():
            results.append(product)
    return results


def binary_search_products(records, search_term):
    results = []
    sorted_records = sorted(records, key=lambda p: p.name.lower())

    low, high = 0, len(sorted_records) - 1
    target = search_term.lower()

    while low <= high:
        mid = (low + high) // 2
        name = sorted_records[mid].name.lower()

        if name == target:
            results.append(sorted_records[mid])
            i = mid - 1
            while i >= 0 and sorted_records[i].name.lower() == target:
                results.append(sorted_records[i])
                i -= 1
            i = mid + 1
            while i < len(sorted_records) and sorted_records[i].name.lower() == target:
                results.append(sorted_records[i])
                i += 1
            break

        elif name < target:
            low = mid + 1
        else:
            high = mid - 1

    return results


# ================================================================
# SORTING (Timsort via Python’s sorted)
# ================================================================
def sort_products_by_nutriscore(records):
    return sorted(records, key=lambda p: p.nutriscore)

def sort_products_by_energy(records):
    return sorted(records, key=lambda p: float(p.energy))

def sort_products_by_category(records):
    return sorted(records, key=lambda p: p.category.lower())

def sort_products_by_name(records):
    return sorted(records, key=lambda p: p.name.lower())


# ================================================================
# INSERTION SORT (NEW)
# ================================================================
def insertion_sort(records, key_func):
    arr = records[:]  # copy
    try:
        for i in range(1, len(arr)):
            temp = arr[i]
            temp_key = key_func(temp)
            j = i - 1
            while j >= 0 and key_func(arr[j]) > temp_key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
    except Exception:
        return records[:]  # fail safe
    return arr


def insertion_sort_by_nutriscore(records):
    return insertion_sort(records, key_func=lambda p: p.nutriscore)

def insertion_sort_by_energy(records):
    return insertion_sort(records, key_func=lambda p: float(p.energy))

def insertion_sort_by_category(records):
    return insertion_sort(records, key_func=lambda p: p.category.lower())

def insertion_sort_by_name(records):
    return insertion_sort(records, key_func=lambda p: p.name.lower())
