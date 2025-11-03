"""
Write a program that reads integers user_num and div_num as input, 
and outputs user_num divided by div_num three times using floor divisions.

Ex: If the input is:

2000
2
the output is:

1000 500 250
Note: In Python 3, floor division discards fractions. Ex: 6 // 4 is 1 (the 0.5 is discarded).
"""
user_number = int(input("what is the number you want to start with? "))
print('you entered', user_number, 'as your starting number')
divisor_number = int(input("what is the number you want to divide by? "))
print('you entered', divisor_number, 'as your divisor number')

print('for our first division, we will divide', user_number, 'by', divisor_number)
second_number = user_number // divisor_number
print("the answer is", second_number)

print('for our second division, we will divide', second_number, 'by', divisor_number)
third_number = second_number // divisor_number
print("the answer is", third_number)

print('for our third division, we will divide', third_number, 'by', divisor_number)
fourth_number = third_number // divisor_number
print("the answer is", fourth_number)

print('getting all three results on the same line:')
print(second_number, third_number, fourth_number)

print('splitting over three lines.')
print(user_number // divisor_number, end = ' ')
print(user_number // divisor_number // divisor_number, end = ' ')
print(user_number // divisor_number // divisor_number // divisor_number, end = ' ')