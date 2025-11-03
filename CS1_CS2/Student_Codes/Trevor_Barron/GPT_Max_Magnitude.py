"""
23.2 LAB: Max magnitude
Write a function max_magnitude() with three integer parameters 
that returns the largest magnitude value. Use the function in the 
main program that takes three integer inputs and outputs the largest magnitude value.

Ex: If the inputs are:

5
7
9
function max_magnitude() returns and the main program outputs:

9
Ex: If the inputs are:

-17
-8
-2
function max_magnitude() returns and the main program outputs:

-17
Note: The function does not just return the largest value, 
which for -17 -8 -2 would be -2. Though not necessary, 
you may use the built-in absolute value function to determine 
the max magnitude, but you must still output the input number (Ex: Output -17, not 17).

Your program must define and call the following function:
def max_magnitude(user_val1, user_val2, user_val3)

Starter Code

# Define your function here.

if __name__ == '__main__':
    # Type your code here.
"""

import math

def max_magnitude(a, b, c):
    """
    Returns the largest magnitude value among three integers a, b, and c.
    """
    return max(abs(a), abs(b), abs(c))

# Ask the user to input as many numbers as they want, separated by spaces
input_str = input("Enter numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]

# Find the largest magnitude value among the entered numbers
max_magnitude_value = -math.inf
for num in numbers:
    if abs(num) > max_magnitude_value:
        max_magnitude_value = abs(num)

# Output the largest magnitude value
print("The largest magnitude value is:", max_magnitude_value)
