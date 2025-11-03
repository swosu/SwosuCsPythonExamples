import random
import string
import pandas as pd
from datetime import datetime

# Custom object class
class DataObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __repr__(self):
        return f"DataObject(name='{self.name}', value={self.value})"

# Function to generate random strings
def random_string(length=5):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

# Create datasets
datasets = {}

# 1. Small random numbers (100 elements)
datasets['small_random_numbers'] = [random.randint(0, 1000) for _ in range(100)]

# 2. Large random numbers (10,000 elements)
datasets['large_random_numbers'] = [random.randint(0, 10000) for _ in range(10000)]

# 3. Small nearly sorted numbers (100 elements)
datasets['small_nearly_sorted_numbers'] = list(range(100))
for _ in range(10):
    i, j = random.randint(0, 99), random.randint(0, 99)
    datasets['small_nearly_sorted_numbers'][i], datasets['small_nearly_sorted_numbers'][j] = \
        datasets['small_nearly_sorted_numbers'][j], datasets['small_nearly_sorted_numbers'][i]

# 4. Large nearly sorted numbers (10,000 elements)
datasets['large_nearly_sorted_numbers'] = list(range(10000))
for _ in range(1000):
    i, j = random.randint(0, 9999), random.randint(0, 9999)
    datasets['large_nearly_sorted_numbers'][i], datasets['large_nearly_sorted_numbers'][j] = \
        datasets['large_nearly_sorted_numbers'][j], datasets['large_nearly_sorted_numbers'][i]

# 5. Small random strings (100 elements)
datasets['small_random_strings'] = [random_string() for _ in range(100)]

# 6. Large random strings (10,000 elements)
datasets['large_random_strings'] = [random_string() for _ in range(10000)]

# 7. Small objects (100 elements)
datasets['small_objects'] = [DataObject(random_string(), random.randint(0, 1000)) for _ in range(100)]

# 8. Large objects (10,000 elements)
datasets['large_objects'] = [DataObject(random_string(), random.randint(0, 10000)) for _ in range(10000)]

# 9. Small reversed numbers (100 elements)
datasets['small_reversed_numbers'] = list(range(100, 0, -1))

# 10. Large reversed numbers (10,000 elements)
datasets['large_reversed_numbers'] = list(range(10000, 0, -1))

# Create sorted versions of all datasets
sorted_datasets = {}
for name, data in datasets.items():
    if 'reversed' in name:
        sorted_datasets[f"sorted_{name}"] = sorted(data)
    elif 'nearly_sorted' in name:
        sorted_datasets[f"sorted_{name}"] = sorted(data)
    else:
        sorted_datasets[f"sorted_{name}"] = sorted(data.copy())

# Save datasets to files
for name, data in {**datasets, **sorted_datasets}.items():
    if all(isinstance(x, (int, float, str)) for x in data):
        pd.Series(data).to_csv(f'datasets/{name}.csv', index=False)
    else:
        # For objects, save as name,value pairs
        pd.DataFrame([{'name': obj.name, 'value': obj.value} for obj in data]).to_csv(f'datasets/{name}.csv', index=False)

print("All datasets created and saved!")