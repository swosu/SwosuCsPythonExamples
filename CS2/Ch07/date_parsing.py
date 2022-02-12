"""
24.6 LAB: Parsing dates
Visible to students
editEdit lab (Links to an external site.)noteNote
Write a program to read dates from input, one date per line.
Each date's format must be as follows:
March 1, 1990.
Any date not following that format is incorrect and should be ignored.
The input ends with -1 on a line alone.
Output each correct date as: 3/1/1990.

Hint: Use string[start:end] to get a substring when
parsing the string and extracting the date.
Use the split() method to break the input into tokens.

Ex: If the input is:

March 1, 1990
April 2 1995
7/15/20
December 13, 2003
-1
then the output is:

3/1/1990
12/13/2003


user_string = input()

# TODO: Read dates from input, parse the dates to find the one
#       in the correct format, and output in m/d/yyyy format
"""

def get_month_as_int(monthString):

    if monthString == 'January':
        month_int = 1
    elif monthString == 'February':
        month_int = 2
    elif monthString == 'March':
        month_int = 3
    elif monthString == 'April':
        month_int = 4
    elif monthString == 'May':
        month_int = 5
    elif monthString == 'June':
        month_int = 6
    elif monthString == 'July':
        month_int = 7
    elif monthString == 'August':
        month_int = 8
    elif monthString == 'September':
        month_int = 9
    elif monthString == 'October':
        month_int = 10
    elif monthString == 'November':
        month_int = 11
    elif monthString == 'December':
        month_int = 12
    else:
        month_int = 0

    return month_int

def get_date_as_int(stuff):
    new_date_as_int = ''
    #print(f'stuff is {stuff}.')
    #print(type(stuff))
    #new_stuff = stuff[0:1]
    #print(f'new stuff is {new_stuff}')
    #print(type(new_stuff))
    for index in stuff:
        if index.isnumeric():
            #print(f'{index} was numeric')
            new_date_as_int = new_date_as_int + index
        #else:
        #    print(f'{stuff(index)} was not numeric')
    return new_date_as_int


user_input = "bob"

while str(-1) != user_input:
    user_input = input('please input your date.')
    #print(f'you entered {user_input}.')
    tokens = user_input.split()
    #print('our tokens are:')
    #print(tokens)

    if str(-1) == user_input:
        break
    else:
        date_month = get_month_as_int(tokens[0])
        #print(f'you entered {tokens[0]} and as an int it is {date_month}.')

        date_day = get_date_as_int(tokens[1])
        #print(f'You entered {tokens[1]} and you get back {date_day}')

        print(f'As numbers, {user_input} becomes {date_month}/{date_day}/{tokens[2]}.')





    #placeholder_month = 'June'
    #date_month = get_month_as_int(placeholder_month)
    #print(f'you entered {placeholder_month} and as an int it is {date_month}.')
