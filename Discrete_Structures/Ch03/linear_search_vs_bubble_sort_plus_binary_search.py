import random
import time
import string

import random

def generate_random_list(size):
    """Generate a random list of integers using a simple loop."""
    min_value = 1
    max_value = size * 1000

    numbers = []

    for index in range(size):
        value = random.randint(min_value, max_value)
        numbers.append(value)

    return numbers


def linear_search(arr, target):
    """Perform a linear search on the array."""
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == target:
            end_time = time.time()
            return f"Target found at index {i} in {len(arr)} elements."
    return "Target not found."

def bubble_sort(arr):
    """Sort the array using bubble sort."""
    start_time = time.time()
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    return f"Sorted array: {arr} in {end_time - start_time:.6f} seconds."

def binary_search(arr, target):
    """Perform a binary search on the sorted array."""
    start_time = time.time()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            end_time = time.time()
            return f"Target found at index {mid} in {len(arr)} elements."
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    end_time = time.time()
    return f"Target not found."

def main():
    # Generate a random list of 1000 integers.
    arr = generate_random_list(1000)
    
    print("Unsorted array:")
    print(arr)

    linear_search_result = linear_search(arr[:], arr[0])
    bubble_sort_result = bubble_sort(arr[:])
    binary_search_result = binary_search(generate_random_list(10), 500)

    print("\nLinear Search Result:", linear_search_result)
    print("Bubble Sort Result:", bubble_sort_result)
    print("Binary Search Result:", binary_search_result)

if __name__ == "__main__":
    main()
