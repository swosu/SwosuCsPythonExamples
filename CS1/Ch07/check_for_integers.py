"""
# Problem : ) 

7.5 LAB: Checker for integer string
Forms often allow a user to enter an integer. 
Write a program that takes in a string representing an integer as input, 
and outputs Yes if every character is a digit 0-9 or No otherwise.

Ex: If the input is:

1995
the output is:

Yes
Ex: If the input is:

42,000
or any string with a non-integer character, the output is:

No
# Starter Code :

user_string = input()

''' Type your code here. '''
"""

def look_to_see_if_it_is_only_numbers_or_no_if_it_has_other_stuff(user_string):
    if user_string.isdigit():
        print('Yes')
    else:
        print('No')



if __name__ == "__main__":
    user_string = input('Please enter a string and press enter when you are done: ')

    look_to_see_if_it_is_only_numbers_or_no_if_it_has_other_stuff(user_string)
