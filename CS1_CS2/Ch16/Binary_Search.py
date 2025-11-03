# recursions and comparisons are set in binary_search and used in main()
recursions = 0
comparisons = 0

# lower and upper are the indicies (inclusive) between which the will
# look for target in nums
def binary_search(nums, target, lower, upper):
    global recursions
    global comparisons

    recursions += 1                       # Each time the function is called
    index = (lower + upper) // 2
    comparisons += 1                      # Next line is a comparison
    if target == nums[index]:
        return index;
   # The following line does not count as a comparison because
   # the code does not compare list elements
    elif (lower == upper):                # Does not count as a comparison
        return -1;                        # Target is not in list

    comparisons += 1                      # Next line is a comparison
    if target < nums[index]:
        return binary_search(nums, target, lower, index - 1)
    else:
        return binary_search(nums, target, index + 1, upper)

if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]

    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
