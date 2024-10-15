# A function that merges two sorted halves into a single sorted list
def merge(left_half, right_half):
    sorted_list = []  # This will store the sorted list
    left_index = 0  # Pointer for the left_half list
    right_index = 0  # Pointer for the right_half list

    # Keep merging until one of the lists is fully traversed
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            sorted_list.append(left_half[left_index])  # Add smaller element from left_half
            left_index += 1  # Move to the next element in left_half
        else:
            sorted_list.append(right_half[right_index])  # Add smaller element from right_half
            right_index += 1  # Move to the next element in right_half

    # If there are remaining elements in left_half, add them to sorted_list
    sorted_list.extend(left_half[left_index:])
    # If there are remaining elements in right_half, add them to sorted_list
    sorted_list.extend(right_half[right_index:])
    
    return sorted_list  # Return the merged and sorted list

# The main merge sort function that splits and merges the list
def merge_sort(lst):
    # Base case: if the list has 1 or 0 elements, it is already sorted
    if len(lst) <= 1:
        return lst

    # Find the middle index to split the list into two halves
    middle_index = len(lst) // 2

    # Split the list into left_half and right_half
    left_half = lst[:middle_index]
    right_half = lst[middle_index:]

    # Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves together
    return merge(sorted_left, sorted_right)

# Example usage
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print(f"Sorted List: {sorted_list}")
print(f'cheated method: {sorted(unsorted_list)}')