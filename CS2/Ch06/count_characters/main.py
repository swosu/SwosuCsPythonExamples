"""
(1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)

Ex:

Enter a sentence or phrase:
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.
(2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)

(3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)

(4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)

Ex:

Enter a sentence or phrase:
The only thing we have to fear is fear itself.

You entered: The only thing we have to fear is fear itself.

Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.
"""

def say_hello():
    print('Hello and welcome to our text analyzer.')

def get_user_string():
    user_string = input('please enter a string of your choice. ')
    return user_string

def get_number_of_characters(user_string):
    char_count = 0
    for characters in user_string:
        char_count += 1
    return char_count

def get_string_with_no_spaces(user_string):
    new_string = ''
    for characters in user_string:
        if ' ' == characters:
            print('that was a space.')
        else:
            new_string = new_string + characters
    return new_string

if __name__ == '__main__':
    say_hello()

    user_string = get_user_string()
    print(f'you entered: {user_string}.')

    number_of_characters = get_number_of_characters(user_string)
    print(f'your string had {number_of_characters} characters.')

    no_spaces_string = get_string_with_no_spaces(user_string)
    print(f'your string with no spaces is {no_spaces_string}.')
