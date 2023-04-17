# Added for solution
# Incremented in merge
# Printed in main
comparisons = 0

# Read integers into a list and return the list.
def read_nums():
    nums = input().split()
    return [int(num) for num in nums]

# Output the content of a list, separated by spaces.
def print_nums(numbers):
    for num in numbers:
        print (num, end=' ')
    print()

def merge(numbers, i, j, k):
    #  Added for solution
    global comparisons                    
    merged_size = k - i + 1  
    merged_numbers = []
    for l in range(merged_size):
        merged_numbers.append(0)

    merge_pos = 0                         

    left_pos = i                         
    right_pos = j + 1                   

    while left_pos <= j and right_pos <= k:
        # Added for solution
        comparisons += 1                  
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos = left_pos + 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    merge_pos = 0
    while merge_pos < merged_size:
        numbers[i + merge_pos] = merged_numbers[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(numbers, i, k):
    j = 0
    if i < k:
        j = (i + k) // 2 
        # Trace output added to code in book
        print(f'{ i } { j } | { j + 1 } { k }')

        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)

        merge(numbers, i, j, k)


if __name__ == '__main__':
    numbers = read_nums()

    print ('unsorted:', end=' ')
    print_nums(numbers)
    print()

    merge_sort(numbers, 0, len(numbers) - 1)

    print ('\nsorted:', end=' ')
    print_nums(numbers)

    # Added for solution
    print(f'comparisons: { comparisons }')