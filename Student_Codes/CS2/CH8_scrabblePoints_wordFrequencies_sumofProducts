'''25.4 LAB: Scrabble points

Scrabble is a word game in which words are constructed from letter tiles, 
each letter tile containing a point value. 

The value of a word is the sum of each tile's points 
added to any points provided by the word's placement on the game board.

Write a program using the given dictionary of letters 
and point values that takes a word as input 
and outputs the base total value of the word 
(before being put onto a board).

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
              'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }


def calculate_word_value(word):
    total_value = 0
    for letter in word.upper():
        total_value += tile_dict.get(letter, 0)
    return total_value

word = input("Enter a word: ")
print("Base total value of the word:", calculate_word_value(word))
'''




'''25.5 LAB: Word frequencies (dictionaries)
Implement the build_dictionary() function to build 
a word frequency dictionary from a list of words.

def build_dictionary(words):
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies

if __name__ == '__main__':
    words = input("Word frequency Checker\nBegin typing: ")
    your_dictionary = build_dictionary(words)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(f'{ key } - { str(your_dictionary[key]) }')
'''



'''25.19 LAB: Sum of products
Write a program that reads two lists of integers 
and outputs the sum of multiplying the corresponding list items.

the program calculates (1 * 3) + (2 * 2) + (3 * 1) and outputs 10
the program calculates (2 * 1) + (3 + 1) + (4 * 1) + (5 * 1) and outputs 14


def sum_of_products(list1, list2):
    total = 0
    for num1, num2 in zip(list1, list2):
        total += num1 * num2
    return total


list1 = [int(x) for x in input("Enter the first list of integers separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter the second list of integers separated by spaces: ").split()]

result = sum_of_products(list1, list2)
print("The sum of products for the input lists is:", result)
'''
