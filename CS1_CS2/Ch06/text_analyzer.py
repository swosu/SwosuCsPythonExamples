"""
23.13 LAB: Warm up: Text analyzer & modifier
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

def say_hello_to_the_world():
    print("Hello from a custom function.")

def ask_user_for_a_sentence():
    user_sentence = input('please enter a sentence of your coosing and then press enter.')
    return user_sentence

def get_num_of_characters(input_str):
    print(f'you passed me the string {input_str}.')
    number_of_characters = 0
    for character in input_str:
        number_of_characters += 1

    print(f'inside the function, num of char was {number_of_characters}.')
    return number_of_characters


if __name__ == '__main__':
    # Type your code here
    say_hello_to_the_world()

    user_sentence = ask_user_for_a_sentence()
    print("You entered: ", end = '')
    print(user_sentence)

    number_of_characters = get_num_of_characters(user_sentence)
    print(f'the string {user_sentence} had {number_of_characters} characters.')
