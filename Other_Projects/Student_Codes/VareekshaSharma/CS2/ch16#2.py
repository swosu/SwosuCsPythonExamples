'''16.13 LAB: Merge sort
The program is the same as shown at the end of the Merge sort section, with the following changes:

Numbers are entered by a user in a separate helper function, read_nums(), instead of defining a specific list.
Output of the list has been moved to the function print_nums().
An output has been added to merge_sort(), showing the indices that will be passed to the recursive function calls.
Add code to the merge sort algorithm to count the number of comparisons performed.

Add code at the end of the program that outputs "comparisons: " followed by the number of comparisons performed (Ex: "comparisons: 12")

Hint: Use a global variable to count the comparisons.

Note: Take special care to look at the output of each test to better understand the merge sort algorithm.

Ex: When the input is:

3 2 1 5 9 8
the output is:

unsorted: 3 2 1 5 9 8

0 2 | 3 5
0 1 | 2 2
0 0 | 1 1
3 4 | 5 5
3 3 | 4 4

sorted:   1 2 3 5 8 9
comparisons: 8


Starter Code'''

comparisons = 0

# Read integers into a list and return the list.
def read_nums():
    nums = input("enter list of ints: ").split()
    return [int(num) for num in nums]

# Output the content of a list, separated by spaces.
def print_nums(numbers):
    for num in numbers:
        print (num, end=' ')
    print()

def merge(numbers, i, j, k):
    global comparisons
    merged_size = k - i + 1               
    merged_numbers = []                   
    for l in range(merged_size):
        merged_numbers.append(0)

    merge_pos = 0                         

    left_pos = i                          
    right_pos = j + 1                     

    while left_pos <= j and right_pos <= k:
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
    print_nums(f'{numbers} \n')

    merge_sort(numbers, 0, len(numbers) - 1)

    print ('\nsorted:', end=' ')
    print_nums(numbers)

    print(f'comparisons: {comparisons}')