"""
24.3 LAB: Fun with characters
Complete the check_character() function which has 2 parameters: 
A string, and a specified index. 

The function checks the character at the specified index of the string parameter, 
and returns a string based on the type of character at that location 
indicating if the character is a letter, digit, whitespace, or unknown character.

Ex: The function calls below with the given arguments 
will return the following strings:

check_character('happy birthday', 2) returns "Character 'p' is a letter"
check_character('happy birthday', 5) returns "Character ' ' is a white space"
check_character('happy birthday 2 you', 15) returns "Character '2' is a digit"
check_character('happy birthday!', 14) returns "Character '!' is unknown"


Starter Code


"""

def check_character(word, index):
    print('you are in the function.')
    print(f'inside the function your inputs were {word} and {index}.')
    
    # get character from the word at that index
    our_character = word[index]
    print(f'our character was: {our_character}.')

    #returns a string based on the type of character at that location 
    # indicating if the character 
    # 
    # is a letter, digit, whitespace, or unknown character.

    # if it is a letter, return "it is a letter"
    result_string = ''
    if our_character.isalpha():
        #print("it is a letter")
        #return "letter"
        result_string = 'letter'

    elif our_character.isnumeric():
        #print("it is a number (digit)")
        #return "digit"
        result_string = 'digit'

    elif our_character.isspace():
        #print("it is a space")
        #return "space"
        result_string = 'space'

    
    else:
        #print("it is a unknown")
        #return "unknown"
        result_string = 'unknown'

    our_string = f'Character \'{our_character}\' is {result_string}'
    print(our_string)
    return our_string


  
if __name__ == '__main__': 
    print('second_test')

    word = 'one pie!ce!'

    index = 7

    print(f'your inputs were {word} and {index}.')

    our_result = check_character(word, index)

    print(f'our reslut was: {our_result}')
    

    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))