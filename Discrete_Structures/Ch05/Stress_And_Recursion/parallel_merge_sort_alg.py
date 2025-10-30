from tracker import Tracker
from merge_sort_alg import merge
import concurrent.futures

def parallel_merge_sort(arr, t: Tracker, workers=4):
    """Top-level parallel merge sort — parallelizes only one split."""
    t.call()
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # Run two halves in parallel just once
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
        left_future = executor.submit(merge_sort_wrapper, left)
        right_future = executor.submit(merge_sort_wrapper, right)
        left_sorted = left_future.result()
        right_sorted = right_future.result()

    result = merge(left_sorted, right_sorted, t)
    return result

def merge_sort_wrapper(data):
    """Helper so child processes don’t need tracker logic."""
    from merge_sort_alg import merge_sort
    dummy_tracker = Tracker()
    return merge_sort(data, dummy_tracker)
