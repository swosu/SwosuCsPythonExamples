import sys
from typing import List


def read_all_input() -> str:
    """
    Reads all input from stdin (works for one line OR multiple lines).
    Returns the raw text.
    """

    user_input = input("Please enter numbers (press enter to end input):\n")
    return user_input


def parse_integers(raw_text: str) -> List[int]:
    """
    Turns raw input text into a list of integers.
    Edge case: empty input => empty list.
    """
    if not raw_text:
        return []
    
    # Step 1: Split the raw text into individual tokens
    tokens = raw_text.split()
    
    # Step 2: Create an empty list to store the integers
    result = []
    
    # Step 3: Loop through each token and append to the list
    for token in tokens:
        num = int(token)
        result.append(num)
    
    return result


def filter_negatives(nums: List[int]) -> List[int]:
    """
    Keeps only negative integers (< 0).
    """
    return [n for n in nums if n < 0]
    # Step 1: Create an empty list to store the negative numbers
    negatives = []
    
    # Step 2: Loop through each number in the list
    for num in nums:
        # Step 3: Check if the number is negative
        if num < 0:
            # Step 4: If it is negative, append it to the list
            negatives.append(num)
    
    return negatives


def sort_descending(nums: List[int]) -> List[int]:
    """
    Returns a new list sorted from highest to lowest.
    """
    return sorted(nums, reverse=True)


def format_with_trailing_spaces(nums: List[int]) -> str:
    """
    Formats numbers so each value is followed by exactly one space.
    Edge case: empty list => empty string.
    """
    if not nums:
        return ""
    return " ".join(str(n) for n in nums) + " "


def main() -> None:
    raw = read_all_input()
    nums = parse_integers(raw)
    negatives = filter_negatives(nums)
    negatives_sorted = sort_descending(negatives)
    output = format_with_trailing_spaces(negatives_sorted)
    sys.stdout.write(output)  # no newline


if __name__ == "__main__":
    main()
