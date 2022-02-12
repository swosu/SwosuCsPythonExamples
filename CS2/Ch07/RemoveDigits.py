print('hello')

"""
Visible to students
editEdit lab (Links to an external site.)noteNote
Write a program that removes all digits from the given input.
I like purple socks.
Ex: If the input is:

1244Crescent
the output is:

Crescent
The program must define and call the following function that takes a string as parameter and returns the string without any digits.

def remove_digits(user_string)
"""


def remove_digits(user_string):
    #print(f'Inside the functiuon call. The user input was: {user_string}')
    no_number_word = ''

    for character in (user_string):
        #print(character, end='')
        if not character.isnumeric():
            no_number_word = no_number_word + character
            #print(' add to our new word.', end = '')
            #print(' new word is', no_number_word)

    #print(no_number_word)
    return no_number_word

if __name__ == '__main__':

    our_input = input('Please enter an address (example: 1244Crescent)')
    #print(f'The user input was: {our_input}')
    new_word = remove_digits(our_input)
    print(f'after removing all numbers, the word is {new_word}.')
