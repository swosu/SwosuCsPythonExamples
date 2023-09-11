"""
25.4 LAB: Scrabble points
Scrabble is a word game in which words are constructed from letter tiles, 
each letter tile containing a point value. 
The value of a word is the sum of each tile's points added 
to any points provided by the word's placement on the game board.

Write a program using the given dictionary of letters 
and point values that takes a word as input and outputs 
the base total value of the word (before being put onto a board).

Ex: If the input is:

PYTHON
the output is:

PYTHON is worth 14 points.


Starter Code

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 
                'G': 2, 'H': 4, 'I': 1, 'J': 8, 
                'K': 5, 'L': 1, 'M': 3, 'N': 1, 
                'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
                'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }    

''' Type your code here. '''
"""

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 
                'G': 2, 'H': 4, 'I': 1, 'J': 8, 
                'K': 5, 'L': 1, 'M': 3, 'N': 1, 
                'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
                'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }

def print_points(word):
        
    total = 0
    for letter in word:
        points_for_letter = tile_dict[letter.upper()]
        print(f"{letter.upper()} is worth {points_for_letter} points.")
        total += tile_dict[letter.upper()]
    print(f"{word} is worth {total} points.")  

def check_for_dictionary_file():
    import os
    if os.path.isfile("words.txt") == False:
        print("File not found.")
        print('downloading file...')
        import urllib.request
        url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
        urllib.request.urlretrieve(url, "words.txt")
        print("File downloaded.")


def word_is_in_dict(word):

    print("Checking if word is in dictionary...")
    check_for_dictionary_file()
   

    with open("words.txt", "r") as f:
        for line in f:
            if word.lower() in line:
                return True
    return False


if __name__ == "__main__":
    word = input("Please enter a word: ")

    if word.isalpha() == False:
        print("Invalid input, not a letter.")
        exit()

    if len(word) == 0:
        print("Invalid input, nothing entered.")
        exit()

    if word_is_in_dict(word) == False:
        print("Invalid input")
        exit()
    else:
        print_points(word)

    