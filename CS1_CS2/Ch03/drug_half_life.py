# -*- coding: utf-8 -*-
"""
A half-life is the amount of time it takes for a 
substance or entity to fall to half its original value. 
Caffeine has a half-life of about 6 hours in humans. 
Given caffeine amount (in mg) as input, output the caffeine level 
after 6, 12, and 24 hours. Use a string formatting expression with conversion 
specifiers to output the caffeine amount as floating-point numbers.

Output each floating-point value with two digits after the decimal point, 
which can be achieved as follows:
print(f'{your_value:.2f}')
Ex: If the input is:

100
the output is:

After 6 hours: 50.00 mg
After 12 hours: 25.00 mg
After 24 hours: 6.25 mg
Note: A cup of coffee has about 100 mg. A soda has about 40 mg. 
An "energy" drink (a misnomer) has between 100 mg and 200 mg.
"""
#print('hello, world.')

#starting_caffine = float(input('please enter a number of mg of caffine.'))/
starting_caffine = float(input())

#print(f'our caffine level at the beginning is {starting_caffine:.2f}')
#print(f'our string type is: {type(starting_caffine)}')

caffine_after_6_hours = starting_caffine / 2.0
print(f'After 6 hours: {caffine_after_6_hours:.2f} mg')

caffine_after_12_hours = starting_caffine / 4.0
print(f'After 12 hours: {caffine_after_12_hours:.2f} mg')

caffine_after_18_hours = starting_caffine / 8.0
#print(f'our caffine level after 18 hours is {caffine_after_18_hours:.2f}')

caffine_after_24_hours = starting_caffine / 16.0
print(f'After 24 hours: {caffine_after_24_hours:.2f} mg')





