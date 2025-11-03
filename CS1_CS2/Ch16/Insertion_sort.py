def read_nums():
    """Read numbers from input and return them in a list"""
    return [int(num) for num in input().split()]

def print_nums(nums):
    """Output numbers, separating each item by a spaces;
    no space or newline before the first number or after the last."""
    print(' '.join([str(n) for n in nums]), end='')

def swap(nums, n, m):
    """Exchange nums[n] and nums[m]"""
    nums[n], nums[m] = nums[m], nums[n]

def insertion_sort(numbers):
    """Sort the list numbers using insertion sort"""
    # Added for solution
    # Global because used outside of fn
    global swaps
    global comparisons
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] is in correct position
        while j > 0:
            comparisons += 1                    # Added for solution
            if numbers[j] < numbers[j - 1]:     # A comparison
                swap(numbers, j, j-1)           # A swap
                swaps += 1                      # Added for solution
                j -= 1
            else:

                break                           # Needed for solution
        print_nums(numbers)                     # Added for solution
        print()

if __name__ == '__main__':
    # Added for solution
    # Global because used outside of fn
    global swaps
    global comparisons
    swaps = 0
    comparisons = 0

    # Step 1: Read numbers into a list
    numbers = read_nums()

    # Step 2: Output the numbers list
    print_nums(numbers);
    print(end='\n\n')

    # Step 3: Sort the numbers list
    insertion_sort(numbers)
    print()
    
    # Step 4: Output the number of comparisons and swaps
    # Added for solution
    print(f'comparisons: { comparisons }')
    print(f'swaps: { swaps }')
