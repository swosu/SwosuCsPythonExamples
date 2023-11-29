"""
3.16 LAB: Simple statistics

Given 4 floating-point numbers. Use a string formatting expression with 
conversion specifiers to output their product and their average as integers (rounded), 
then as floating-point numbers.

Output each rounded integer using the following:
print(f'{your_value:.0f}')

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.3f}')

Ex: If the input is:

8.3
10.4
5.0
4.8


the output is:

2072 7
2071.680 7.125
 

Starter code from book:

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

''' Type your code here. '''
"""

# create a list my_numbers to hold the 4 numbers
my_numbers = []

# get the 4 numbers from the user
for i in range(4):
    my_numbers.append(float(input('please enter a number: ')))

print('thank you for entering the numbers')

# print out the list of numbers
print(my_numbers)

# find the average of the numbers and save it to my_average_float
my_sum_of_all_my_numbers = sum(my_numbers)
print('the sum of all the numbers is: ', my_sum_of_all_my_numbers)
my_number_of_numbers = len(my_numbers)
print('the number of numbers is: ', my_number_of_numbers)
my_average_float = my_sum_of_all_my_numbers / my_number_of_numbers
print('the average of the numbers is: ', my_average_float)

# find the product of the numbers and save it to my_product_float
my_product_float = 1
for individual_number in my_numbers:
    #my_product_float *= individual_number
    my_product_float = my_product_float * individual_number
    print('after multiplying by ', individual_number, ' the product is: ', my_product_float)

print('the product of the numbers is: ', my_product_float)

# round the product to an integer and save it to my_product_int
my_product_int = int(my_product_float)
# print out the average as an integer
print('the product of the numbers as an integer is: ', my_product_int)

#round the average and save it to my product_rounded_int
my_product_rounded_int = round(my_product_float)
# print out the average as an integer
print('the product of the numbers as a rounded integer is: ', my_product_rounded_int)