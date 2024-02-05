print(' start of code')
# get user number 1 as a string and covert it to a floating point number
user_number_1 = float(input('Enter a number for user number 1 that has a decimal point: '))
print('for user number 1, the number is:', user_number_1)

# get user number 2 as a string and covert it to a floating point number
user_number_2 = float(input('Enter a number for user number 2 that has a decimal point: '))
print('for user number 2, the number is:', user_number_2)

# get user number 3 as a string and covert it to a floating point number
user_number_3 = float(input('Enter a number for user number 3 that has a decimal point: '))
print('for user number 3, the number is:', user_number_3)

# get user number 4 as a string and covert it to a floating point number
user_number_4 = float(input('Enter a number for user number 4 that has a decimal point: '))
print('for user number 4, the number is:', user_number_4)

# find the product the the numbers by multiplying them together and storing the result in a variable called product
product = user_number_1 * user_number_2 * user_number_3 * user_number_4

# find the average of the numbers by adding them together and dividing by 4 and storing the result in a variable called average
average = (user_number_1 + user_number_2 + user_number_3 + user_number_4) / 4

# print off the product and average of the numbers as integers
# Output each rounded integer using the following:
#  print(f'{your_value:.0f}')
print(f'{product:.0f} {average:.0f}')

# print off the product and average of the numbers as floating point numbers
#Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
# print(f'{your_value:.3f}')
print(f'{product:.3f} {average:.3f}')

print(' end of code')