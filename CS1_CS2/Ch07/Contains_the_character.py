"""
24.2 LAB: Contains the character
Write a program that reads a character, then reads in a list of words. 
The output of the program is every word in the list that contains 
the character at least once. 
Assume at least one word in the list will contain the given character.

Ex: If the input is:

z
hello zoo sleep drizzle
the output is:

zoo,drizzle,
Keep in mind that the character 'a' is not equal to the character 'A'.

For coding simplicity, follow each output word by a comma, even the last one. 
Do not end with newline.
"""

if __name__ == '__main__':
    character = input('please enter a character that we will be looking for : ')
    words = input('please enter a list of words to search through: ')
    tokens = words.split()
    for word in tokens:
        if character in word:
            print(word + ',', end = '')