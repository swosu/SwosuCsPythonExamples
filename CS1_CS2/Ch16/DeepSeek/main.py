import csv
from sorting_algorithms import test_sorts_on_dataset
from searching_algorithms import linear_search, binary_search
import pandas as pd
import os
import time

def load_datasets():
    datasets = {}
    # Load all CSV files from datasets directory
    for filename in os.listdir('datasets'):
        if filename.endswith('.csv'):
            name = filename[:-4]  # remove .csv extension
            try:
                df = pd.read_csv(f'datasets/{filename}')
                if 'name' in df.columns and 'value' in df.columns:
                    # Object dataset
                    data = [DataObject(row['name'], row['value']) for _, row in df.iterrows()]
                else:
                    # Primitive dataset
                    data = df.iloc[:, 0].tolist()
                datasets[name] = data
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    return datasets

class DataObject:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __lt__(self, other):
        return self.value < other.value
    
    def __repr__(self):
        return f"DataObject(name='{self.name}', value={self.value})"

def run_full_analysis():
    # Create directories
    os.makedirs('results', exist_ok=True)
    os.makedirs('plots', exist_ok=True)
    
    # 1. Load datasets
    datasets = load_datasets()
    if not datasets:
        print("No datasets found. Please run dataset_generator.py first.")
        return
    
    # 2. Run sorting tests
    all_sort_results = []
    for name, data in datasets.items():
        all_sort_results.extend(test_sorts_on_dataset(name, data))
    
    # Save sorting results
    with open('results/sort_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_sort_results[0].keys())
        writer.writeheader()
        writer.writerows(all_sort_results)
    
    # 3. Run searching tests
    all_search_results = []
    for name, data in datasets.items():
        if len(data) == 0:
            continue
        
        # Determine target (middle element)
        if hasattr(data[0], 'value'):
            target = data[len(data)//2].value
        else:
            target = data[len(data)//2]
        
        # Test linear search
        start_time = time.time()
        linear_result = linear_search(data, target)
        linear_time = time.time() - start_time
        
        all_search_results.append({
            'dataset': name,
            'algorithm': 'linear',
            'time': linear_time,
            'comparisons': linear_result['comparisons'],
            'size': len(data),
            'type': 'numbers' if isinstance(data[0], (int, float)) else 
                   'strings' if isinstance(data[0], str) else 'objects',
            'sorted': 'sorted' in name
        })
        
        # Test binary search if data is sorted
        if 'sorted' in name:
            start_time = time.time()
            binary_result = binary_search(data, target)
            binary_time = time.time() - start_time
            
            all_search_results.append({
                'dataset': name,
                'algorithm': 'binary',
                'time': binary_time,
                'comparisons': binary_result['comparisons'],
                'size': len(data),
                'type': 'numbers' if isinstance(data[0], (int, float)) else 
                       'strings' if isinstance(data[0], str) else 'objects',
                'sorted': True
            })
    
    # Save search results
    with open('results/search_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=all_search_results[0].keys())
        writer.writeheader()
        writer.writerows(all_search_results)
    
    # 4. Generate visualizations
    from visualization import create_visualizations
    create_visualizations()
    print("Project completed successfully!")

if __name__ == "__main__":
    run_full_analysis()