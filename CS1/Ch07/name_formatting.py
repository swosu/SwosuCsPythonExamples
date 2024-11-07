"""
Many documents use a specific format for a person's name. 

Write a program that reads a person's name in the following format:

firstName middleName lastName (in one line)

and outputs the person's name in the following format:

lastName, firstInitial.middleInitial.

Ex: If the input is:

Pat Silly Doe
the output is:

Doe, P.S.
If the input has the following format:

firstName lastName (in one line)

the output is:

lastName, firstInitial.

Ex: If the input is:

Julia Clark
the output is:

Clark, J.
# Starter Code :

''' Type your code here. '''
"""

def get_user_name():
    print('please enter your name in the following format: ')
    print('firstName middleName lastName')
    print('or')
    print('firstName lastName')
    user_input = input('Please press enter when you are finished: ')
    return user_input


if __name__ == '__main__':
    user_input = get_user_name()

    print('you entered: ', user_input)