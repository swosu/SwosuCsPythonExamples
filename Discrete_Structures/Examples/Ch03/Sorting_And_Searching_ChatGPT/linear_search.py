def linear_search(arr, target=42):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
