import numpy as np
import concurrent.futures

def builtin_sort(arr):
    # Python’s Timsort (same used by list.sort() / sorted)
    return sorted(arr)

def parallel_builtin_sort(arr, workers=4):
    # Simple parallel version: chunk + numpy sort + merge
    size = len(arr)
    chunks = np.array_split(np.array(arr), workers)
    with concurrent.futures.ProcessPoolExecutor(workers) as ex:
        sorted_chunks = list(ex.map(np.sort, chunks))
    # merge the sorted chunks
    result = np.concatenate(sorted_chunks)
    return np.sort(result)
