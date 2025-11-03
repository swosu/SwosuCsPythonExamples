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
For coding simplicity, output a space after every integer, including the last.
"""

#starting_number = int(input('what is your starting number? '))
#ending_number = int(input('what is your ending number? '))
starting_number = int(input())
ending_number = int(input())
if ending_number < starting_number:
    print('Second integer can\'t be less than the first.')
else:
    step_size = 5
    our_list = list(range(starting_number, (ending_number + step_size), step_size))
    #print(our_list)

    for our_item in our_list:
        if ending_number >= our_item:
            print(our_item, end = ' ')

    print()
