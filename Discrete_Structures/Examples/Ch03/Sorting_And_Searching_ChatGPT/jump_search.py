import math

def jump_search(sequence, target_value=42):
    """Jump search algorithm for sorted sequences.
    Returns the index if found, otherwise -1.
    """
    n = len(sequence)
    step = int(math.sqrt(n))
    prev = 0

    # Jump forward until target could be inside block
    while prev < n and sequence[min(step, n) - 1] < target_value:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear scan within the identified block
    for i in range(prev, min(step, n)):
        if sequence[i] == target_value:
            return i
    return -1
