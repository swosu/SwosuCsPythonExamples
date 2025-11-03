"""
2.16 LAB: Using math functions
Given three floating-point numbers x, y, and z, 

output x to the power of z, 
x to the power of (y to the power of z), 
the absolute value of (x minus y), 
and the square root of (x to the power of z).

Output each floating-point value with two digits after the decimal point, 
which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

Ex: If the input is:

5.0
1.5
3.2
Then the output is:

172.47 361.66 3.50 13.13

starter code:

''' Type your code here. '''
"""

import math

# get a value for x,y, and z. Tell the user to enter a number with a decimal point.
x = float(input('Enter a number for x that has a decimal point: '))
y = float(input('Enter a number for y that has a decimal point: '))
z = float(input('Enter a number for z that has a decimal point: '))

# output x to the power of z,
x_to_the_power_of_z = x ** z

# output x to the power of (y to the power of z),
x_to_the_power_of_y_to_the_power_of_z = x ** (y ** z)

# the absolute value of (x minus y),
absolute_value_of_x_minus_y = abs(x - y)

# and the square root of (x to the power of z).
square_root_of_x_to_the_power_of_z = math.sqrt(x ** z)

# Output each floating-point value with two digits after the decimal point,
print(f'{x_to_the_power_of_z:.2f} {x_to_the_power_of_y_to_the_power_of_z:.2f} {absolute_value_of_x_minus_y:.2f} {square_root_of_x_to_the_power_of_z:.2f}')



