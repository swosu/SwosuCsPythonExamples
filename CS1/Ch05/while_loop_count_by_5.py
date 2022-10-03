"""
Programming Assignment

#1) 

5.16 LAB: Output range with increment of 5



b. Output the first integer 

c. and subsequent increments of 5 

d. as long as the value is less than or equal to the second integer.

Ex: If the input is:

-15
10
the output is:

-15 -10 -5 0 5 10 
Ex: If the second integer is less than the first as in:

20
5
the output is:


For coding simplicity, output a space after every integer, including the last.

No code from book.
"""

#a. Write a program whose input is two integers. 
first_number = int(input('what is your first number to begin with? '))
second_number = int(input('how high do you want to count by 5? '))
print(f'you want to start with {first_number} and stop at or before {second_number}.')

if second_number < first_number:
    print('Second integer can\'t be less than the first.')

our_number = first_number

while our_number <= second_number:
    print(our_number, ' ', end='')
    our_number = our_number + 5