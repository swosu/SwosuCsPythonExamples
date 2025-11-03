# Linear Search implementation
def linear_search(data, target):
    start_time = time.time()
    comparisons = 0
    
    for i, item in enumerate(data):
        comparisons += 1
        if hasattr(item, 'value'):
            if item.value == target:
                return {
                    'index': i,
                    'time': time.time() - start_time,
                    'comparisons': comparisons
                }
        else:
            if item == target:
                return {
                    'index': i,
                    'time': time.time() - start_time,
                    'comparisons': comparisons
                }
    
    return {
        'index': -1,
        'time': time.time() - start_time,
        'comparisons': comparisons
    }

# Binary Search implementation
def binary_search(data, target):
    start_time = time.time()
    comparisons = 0
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        
        current_value = data[mid].value if hasattr(data[mid], 'value') else data[mid]
        
        if current_value == target:
            return {
                'index': mid,
                'time': time.time() - start_time,
                'comparisons': comparisons
            }
        elif current_value < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return {
        'index': -1,
        'time': time.time() - start_time,
        'comparisons': comparisons
    }

# Test searching on datasets
all_search_results = []

for name, data in {**datasets, **sorted_datasets}.items():
    # Determine target (middle element for fairness)
    if len(data) == 0:
        continue
    
    if hasattr(data[0], 'value'):
        target = data[len(data)//2].value
    else:
        target = data[len(data)//2]
    
    # Test linear search
    linear_result = linear_search(data, target)
    all_search_results.append({
        'dataset': name,
        'algorithm': 'linear',
        'time': linear_result['time'],
        'comparisons': linear_result['comparisons'],
        'size': len(data),
        'type': 'numbers' if isinstance(data[0], (int, float)) else 
               'strings' if isinstance(data[0], str) else 'objects',
        'sorted': 'sorted' in name
    })
    
    # Test binary search if data is sorted
    if 'sorted' in name:
        binary_result = binary_search(data, target)
        all_search_results.append({
            'dataset': name,
            'algorithm': 'binary',
            'time': binary_result['time'],
            'comparisons': binary_result['comparisons'],
            'size': len(data),
            'type': 'numbers' if isinstance(data[0], (int, float)) else 
                   'strings' if isinstance(data[0], str) else 'objects',
            'sorted': True
        })
    else:
        # Test binary search with sorting
        sort_start = time.time()
        if hasattr(data[0], 'value'):
            sorted_data = sorted(data, key=lambda x: x.value)
        else:
            sorted_data = sorted(data)
        sort_time = time.time() - sort_start
        
        binary_result = binary_search(sorted_data, target)
        all_search_results.append({
            'dataset': name,
            'algorithm': 'binary_with_sort',
            'time': binary_result['time'] + sort_time,
            'comparisons': binary_result['comparisons'],
            'size': len(data),
            'type': 'numbers' if isinstance(data[0], (int, float)) else 
                   'strings' if isinstance(data[0], str) else 'objects',
            'sorted': False,
            'sort_time': sort_time
        })

# Save search results
keys = all_search_results[0].keys()
with open('search_results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keys)
    writer.writeheader()
    writer.writerows(all_search_results)

print("Search tests completed and results saved!")