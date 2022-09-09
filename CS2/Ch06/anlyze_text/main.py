"""

23.14 LAB*: Program: Authoring assistant
(1) Prompt the user to enter a string of their choosing.
Store the text in a string. Output the string. (1 pt)

Ex:

Enter a sample text:
we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

(2) Implement the print_menu() function to print the following command menu. (1 pt)

Ex:

MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

(3) Implement the execute_menu() function that takes 2 parameters: a character representing the user's choice and the user provided sample text. execute_menu() performs the menu options, according to the user's choice, by calling the appropriate functions described below. (1 pt)


(4) In the main program, call print_menu() and prompt for the user's choice of menu options for analyzing/editing the string. Each option is represented by a single character.

If an invalid character is entered, continue to prompt for a valid choice. When a valid option is entered, execute the option by calling execute_menu(). Then, print the menu and prompt for a new option. Continue until the user enters 'q'. Hint: Implement Quit before implementing other options. (1 pt)

Ex:

MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

Choose an option:

(5) Implement the get_num_of_non_WS_characters() function. get_num_of_non_WS_characters() has a string parameter and returns the number of characters in the string, excluding all whitespace. Call get_num_of_non_WS_characters() in the execute_menu() function, and then output the returned value. (4 pts)

Ex:

Enter a sample text:
we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

You entered: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  nothing ends here;  our hopes and our journeys continue!

MENU
c - Number of non-whitespace characters
w - Number of words
f - Fix capitalization
r - Replace punctuation
s - Shorten spaces
q - Quit

Choose an option:
c
Number of non-whitespace characters: 181

(6) Implement the get_num_of_words() function. get_num_of_words() has a string parameter and returns the number of words in the string. Hint: Words end when a space is reached except for the last word in a sentence. Call get_num_of_words() in the execute_menu() function, and then output the returned value. (3 pts)

Ex:

Number of words: 35

(7) Implement the fix_capitalization() function. fix_capitalization() has a string parameter and returns an updated string, where lowercase letters at the beginning of sentences are replaced with uppercase letters. fix_capitalization() also returns the number of letters that have been capitalized. Call fix_capitalization() in the execute_menu() function, and then output the number of letters capitalized followed by the edited string. Hint 1: Look up and use Python functions .islower() and .upper() to complete this task. Hint 2: Create an empty string and use string concatenation to make edits to the string. (3 pts)

Ex:

Number of letters capitalized: 3
Edited text: We'll continue our quest in space.  There will be more shuttle flights and more shuttle crews and,  yes;  more volunteers, more civilians,  more teachers in space.  Nothing ends here;  our hopes and our journeys continue!

(8) Implement the replace_punctuation() function. replace_punctuation() has a string parameter and two keyword argument parameters exclamation_count and semicolon_count. replace_punctuation() updates the string by replacing each exclamation point (!) character with a period (.) and each semicolon (;) character with a comma (,). replace_punctuation() also counts the number of times each character is replaced and outputs those counts. Lastly, replace_punctuation() returns the updated string. Call replace_punctuation() in the execute_menu() function, and then output the edited string. (3 pts)

Ex:

Punctuation replaced
exclamation_count: 1
semicolon_count: 2
Edited text: we'll continue our quest in space.  there will be more shuttle flights and more shuttle crews and,  yes,  more volunteers, more civilians,  more teachers in space.  nothing ends here,  our hopes and our journeys continue.

(9) Implement the shorten_space() function. shorten_space() has a string parameter and updates the string by replacing all sequences of 2 or more spaces with a single space. shorten_space() returns the string. Call shorten_space() in the execute_menu() function, and then output the edited string. Hint: Look up and use Python function .isspace(). (3 pt)

Ex:

Edited text: we'll continue our quest in space. there will be more shuttle flights and more shuttle crews and, yes; more volunteers, more civilians, more teachers in space. nothing ends here; our hopes and our journeys continue!
Starter Code:
"""

# Define your functions here.
def get_user_string():
    user_string = input('please enter a string.')
    return user_string

def print_user_string(user_string):
    print(f'you entered: {user_string}')

if __name__ == '__main__':
    # Complete the main program here.
    user_string = get_user_string()
    print_user_string(user_string)
