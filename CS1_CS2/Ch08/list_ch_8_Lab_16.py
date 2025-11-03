def calculate_max(numbers):
    # Initialize maximum to the first number
    maximum = numbers[0]
    
    # Iterate through the list
    for number in numbers:
        # If the current number is greater than the maximum, update the maximum
        if number > maximum:
            maximum = number
    
    return maximum

def calculate_sum(numbers):
    # Initialize sum to 0
    sum_of_numbers = 0
    
    # Iterate through the list
    for number in numbers:
        # Add the current number to the sum
        sum_of_numbers += number
    
    return sum_of_numbers

def main():
    # Read input numbers as a list of floats
    numbers = list(map(float, input("Enter numbers separated by spaces and press enter when you are finished: ").split()))
    
    # Calculate max and average
    maximum = calculate_max(numbers)
    sum_of_numbers = calculate_sum(numbers)
    average = sum_of_numbers / len(numbers)
    
    # Output results with two decimal places
    print(f"{maximum:.2f} {average:.2f}")


if __name__ == "__main__":
    main()
