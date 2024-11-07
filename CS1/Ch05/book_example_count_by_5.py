"""
5.16 LAB: Output range with increment of 5
Write a program whose input is two integers. 
Output the first integer and subsequent increments of 5 
as long as the value is less than or equal to the second integer.

Ex: If the input is:

-15
10
the output is:

-15 -10 -5 0 5 10 
Ex: If the second integer is less than the first as in:

20
5
the output is:

Second integer can't be less than the first.
For coding simplicity, output a space after every integer, 
including the last. End the output with a newline.
"""

# Prompt user for the first integer
#first_integer = int(input('please enter the number you want to start counting from: '))

first_integer = -15

# Prompt user for the second integer
#second_integer = int(input('please enter the number you want to stop counting at: '))
second_integer = 10

# Promt user for the step size
#step_size = int(input('please enter the step size you want to use between the numbers: '))
step_size = 5

if second_integer < first_integer:
    print('Second integer can\'t be less than the first.')
    numbers_printed = 0
    for index in range(first_integer, (second_integer + step_size), -1 * step_size):
        #print(index, end=' ')
        numbers_printed = numbers_printed + 1
        print('numbers printed: ', numbers_printed, 'index: ', index)

else:
    print('entering the else part')
    numbers_printed = 0

    for index in range(first_integer, (second_integer+step_size), step_size):
        #print(index, end=' ')
        numbers_printed = numbers_printed + 1
        print('numbers printed: ', numbers_printed, 'index: ', index)