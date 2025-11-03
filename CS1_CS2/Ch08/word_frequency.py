"""
25.13 LAB: Word frequencies (dictionaries)
Implement the build_dictionary() function to build a word frequency dictionary from a list of words.

Ex: If the words list is:

["hey", "hi", "Mark", "hi", "mark"]
the dictionary returned from calling build_dictionary(words) is:

{'hey': 1, 'hi': 2, 'Mark': 1, 'mark': 1}
Ex: If the words list is:

["zyBooks", "now", "zyBooks", "later", "zyBooks", "forever"]
the dictionary returned from calling build_dictionary(words) is:

{'zyBooks': 3, 'now': 1, 'later': 1, 'forever': 1}
The main code builds the word list from an input string, calls build_dictionary() to build the dictionary, and displays the dictionary sorted by key value.

Ex: If the input is:

hey hi Mark hi mark
the output is:

Mark - 1
hey - 1
hi - 2
mark - 1


Starter Code
"""
# The words parameter is a list of strings.
def build_dictionary(words):
    # The frequencies dictionary will be built with your code below.
    # Each key is a word string and the corresponding value is an integer
    # indicating that word's frequency.
    
    print('the function input the words list: ', words)

    print('we will build a dictionary called frequencies')
    frequencies = {}

    print('we will iterate through the words list')
    for word in words:
        print('the current word is: ', word)
        print('we will check if the word is in the dictionary')
        if word in frequencies:
            print('the word is in the dictionary')
            print('we will increment the value of the word in the dictionary')
            frequencies[word] = frequencies[word] + 1
        else:
            print('the word is not in the dictionary')
            print('we will add the word to the dictionary')
            frequencies[word] = 1

        print('after the word', word, 'the dictionary is: ', frequencies)

    print('the function will return the dictionary: ', frequencies)
    return frequencies



# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
if __name__ == '__main__':
    print('welcome to the word frequency program')
    print('Please input a list of words, seperated by spaces and currounded by quotes.')
    words_from_user = input('for example: hey hi Mark hi mark\n')
    print('you entered: ', words_from_user)
    print('now we split the string into a list of words')
    words = words_from_user.split()
    print('the list of words is: ', words)
    print('now we build a dictionary of word frequencies')
    your_dictionary = build_dictionary(words)
    print('back in the main code after building the dictionary')
    print('the dictionary is: ', your_dictionary)
    sorted_keys = sorted(your_dictionary.keys())
    for key in sorted_keys:
        print(f'{ key } - { str(your_dictionary[key]) }')
