# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 13:43:34 2023

@author: evertj
Written using ChatGPT 3.5
"""

'''
[236.0, 89.5, 176.0, 166.3]
Average weight: 166.95
Max weight: 236.00
'''

# Create an empty list to store the weights
weights = []

# Use a loop to prompt the user for each weight
for i in range(1, 5):
    weight = float(input(f"Enter weight {i}: "))
    weights.append(weight)

# Output the list of weights
print(f"Weights: {weights}")


# Calculate the average of the weights
average = sum(weights) / len(weights)

rounded_average = round(average, 2)

# Output the average with two digits after the decimal point
print(f"Rounded Average: {rounded_average:.2f}")
print(f"Average: {average:.2f}")

'''
# Define a number
number = 12.3456

# Round the number to two digits
rounded_number = round(number, 2)

# Print the rounded number
print(rounded_number)
'''