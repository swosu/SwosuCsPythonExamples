import time
import sys
from functools import wraps

def analyze_sort(func):
    @wraps(func)
    def wrapper(data, *args, **kwargs):
        start_time = time.time()
        start_mem = sys.getsizeof(data)
        comparisons = [0]
        swaps = [0]
        
        def counted_compare(a, b):
            comparisons[0] += 1
            return a < b
        
        result = func(data, counted_compare, swaps, *args, **kwargs)
        
        end_time = time.time()
        end_mem = sys.getsizeof(data)
        time_taken = end_time - start_time
        mem_used = end_mem - start_mem
        
        return {
            'result': result,
            'time': time_taken,
            'comparisons': comparisons[0],
            'swaps': swaps[0],
            'memory': mem_used
        }
    return wrapper

# Bubble Sort implementation
@analyze_sort
def bubble_sort(data, compare, swaps):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if compare(data[j+1], data[j]):
                data[j], data[j+1] = data[j+1], data[j]
                swaps[0] += 1
    return data

# Merge Sort implementation
@analyze_sort
def merge_sort(data, compare, swaps):
    if len(data) <= 1:
        return data
    
    mid = len(data) // 2
    left = merge_sort(data[:mid], compare, swaps)
    right = merge_sort(data[mid:], compare, swaps)
    
    return merge(left, right, compare, swaps)

def merge(left, right, compare, swaps):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        swaps[0] += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort implementation
@analyze_sort
def quick_sort(data, compare, swaps):
    def _quick_sort(items):
        if len(items) <= 1:
            return items
        
        pivot = items[len(items) // 2]
        left = [x for x in items if compare(x, pivot)]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if compare(pivot, x)]
        
        swaps[0] += len(items) - 1
        
        return _quick_sort(left) + middle + _quick_sort(right)
    
    return _quick_sort(data)

# TimSort implementation
@analyze_sort
def tim_sort(data, compare, swaps):
    data.sort(key=lambda x: x.value if hasattr(x, 'value') else x)
    swaps[0] = len(data) * 2
    return data

def test_sorts_on_dataset(name, data):
    results = []
    
    # Make copies of the data for each sort
    data_bubble = data.copy() if hasattr(data, 'copy') else list(data)
    data_merge = data.copy() if hasattr(data, 'copy') else list(data)
    data_quick = data.copy() if hasattr(data, 'copy') else list(data)
    data_tim = data.copy() if hasattr(data, 'copy') else list(data)
    
    # Test each sort
    for sort_func in [bubble_sort, merge_sort, quick_sort, tim_sort]:
        sort_name = sort_func.__name__
        try:
            result = sort_func(data.copy() if hasattr(data, 'copy') else list(data))
            results.append({
                'dataset': name,
                'algorithm': sort_name,
                'time': result['time'],
                'comparisons': result['comparisons'],
                'swaps': result['swaps'],
                'memory': result['memory'],
                'size': len(data),
                'type': 'numbers' if isinstance(data[0], (int, float)) else 
                       'strings' if isinstance(data[0], str) else 'objects'
            })
        except Exception as e:
            print(f"Error with {sort_name} on {name}: {e}")
    
    return results