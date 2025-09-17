def linear_search(sequence, target_value=42):
    for index, element in enumerate(sequence):
        if element == target_value:
            return index
    return -1
