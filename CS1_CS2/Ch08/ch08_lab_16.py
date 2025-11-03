def get_input_numbers():
    """Get a list of non-negative floating-point numbers from user input."""
    input_data = input("Enter non-negative floating-point numbers separated by spaces and press enter after the last number: ")
    numbers = list(map(float, input_data.split()))
    return [num for num in numbers if num >= 0]  # Filter out negative numbers

def calculate_max(numbers):
    """Return the maximum value from a list of numbers."""
    return max(numbers) if numbers else 0.0  # Return 0.0 if the list is empty

def calculate_average(numbers):
    """Return the average of a list of numbers."""
    return sum(numbers) / len(numbers) if numbers else 0.0  # Return 0.0 if the list is empty

def main():
    """Main function to execute the program."""
    numbers = get_input_numbers()
    max_value = calculate_max(numbers)
    average_value = calculate_average(numbers)
    
    # Print the results formatted to two decimal places
    print(f"{max_value:.2f} {average_value:.2f}")

if __name__ == "__main__":
    main()