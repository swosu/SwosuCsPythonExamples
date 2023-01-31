#1)

25.4 LAB: Scrabble points
Scrabble is a word game in which words are constructed from letter tiles, each letter tile containing a point value. The value of a word is the sum of each tile's points added to any points provided by the word's placement on the game board.

Write a program using the given dictionary of letters and point values that takes a word as input and outputs the base total value of the word (before being put onto a board).

Ex: If the input is:

PYTHON
the output is:

PYTHON is worth 14 points.


Starter Code

tile_dict = { 'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 
              'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 
                            'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10 }    

                            ''' Type your code here. '''


                            #2)

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

                            # The words parameter is a list of strings.
                            def build_dictionary(words):
                                # The frequencies dictionary will be built with your code below.
                                    # Each key is a word string and the corresponding value is an integer 
                                        # indicating that word's frequency.
                                            
                                                ''' Type your code here (remove the "pass" statement below) '''
                                                    pass

                                                    # The following code asks for input, splits the input into a word list, 
                                                    # calls build_dictionary(), and displays the contents sorted by key.
                                                    if __name__ == '__main__':
                                                        words = input().split()
                                                            your_dictionary = build_dictionary(words)
                                                                sorted_keys = sorted(your_dictionary.keys())
                                                                    for key in sorted_keys:
                                                                            print(f'{ key } - { str(your_dictionary[key]) }')


                                                                            #3)

                                                                             

                                                                             5.14 LAB: Warm up: People's weights (Lists)

                                                                             Clone
                                                                             Edit lab

                                                                             Note
                                                                             (1) Prompt the user to enter four numbers, each corresponding to a person's weight in pounds. Store all weights in a list. Output the list. (2 pts)

                                                                             Ex:

                                                                             Enter weight 1:
                                                                             236.0
                                                                             Enter weight 2:
                                                                             89.5
                                                                             Enter weight 3:
                                                                             176.0
                                                                             Enter weight 4:
                                                                             166.3
                                                                             Weights: [236.0, 89.5, 176.0, 166.3]
                                                                             (2) Output the average of the list's elements with two digits after the decimal point. Hint: Use a conversion specifier to output with a certain number of digits after the decimal point. (1 pt)

                                                                             (3) Output the max list element with two digits after the decimal point. (1 pt)

                                                                             Ex:

                                                                             Enter weight 1:
                                                                             236.0
                                                                             Enter weight 2:
                                                                             89.5
                                                                             Enter weight 3:
                                                                             176.0
                                                                             Enter weight 4:
                                                                             166.3
                                                                             Weights: [236.0, 89.5, 176.0, 166.3]

                                                                             Average weight: 166.95
                                                                             Max weight: 236.00
                                                                             (4) Prompt the user for a number between 1 and 4. Output the weight at the user specified location and the corresponding value in kilograms. 1 kilogram is equal to 2.2 pounds. (3 pts)


                                                                             Ex:

                                                                             Enter a list location (1 - 4):
                                                                             3
                                                                             Weight in pounds: 176.00
                                                                             Weight in kilograms: 80.00
                                                                             (5) Sort the list's elements from least heavy to heaviest weight. (2 pts)


                                                                             Ex:

                                                                             Sorted list: [89.5, 166.3, 176.0, 236.0]
                                                                             Output the average and max weights as floating-point values with two digits after the decimal point, which can be achieved as follows:
                                                                             print(f'{your_value:.2f}')
