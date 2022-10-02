"""
#3) 19.7 LAB: Square root
Given a floating-point number as input, output the square root of the given number.
Hint: Use the appropriate function from the math module to perform the operation.

Ex: If the input is:
9.0
the output is:
Sqrt: 3.0
"""

import math

user_input = float(input('what would you like to take the square root of?'))

print(f'You entered {user_input}, with a type of {type(user_input)}.')

square_root_of_user_input = math.sqrt(user_input)

print(f'The square root of {user_input} is {square_root_of_user_input}.')
