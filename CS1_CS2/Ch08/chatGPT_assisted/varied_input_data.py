"""
Statistics are often calculated with varying amounts of input data. 
Write a program that takes any number of non-negative floating-point numbers as input, 
and outputs the max and average, respectively.

Output the max and average with two digits after the decimal point.

Ex: If the input is:

14.25 25 0 5.75

the output is:

25.00 11.25
"""


while True:
    user_input = input("Enter non-negative floating-point numbers separated by spaces: ")

    # Split the input string into individual number strings
    number_strings = user_input.split()

    # Convert the number strings to floating-point numbers

    numbers = []
    for num in number_strings:
        if float(num) >= 0:
            numbers.append(float(num))
        else:
            print("Please enter only non-negative numbers.")
            break


    # Calculate max and average
    if numbers:
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)

        # Output the results with two digits after the decimal point
        print(f"{maximum:.2f} {average:.2f}")
        break

    