import os

"""
Given a set of text files containing synonyms 
for different words, complete the main program 
to output the synonyms for a specific word. 


Each text file contains synonyms for the word 
specified in the file’s name, and each row within 
the file lists the word’s synonyms that begin with 
the same letter, separated by a space.


The program reads a word and a letter from the user 
and opens the text file associated with the input word. 


The program then stores the contents of the text file 
into a dictionary predefined in the program. 


Finally the program searches the dictionary and 
outputs all the synonyms that begin with the input letter, 
one synonym per line, or a message if no synonyms that 
begin with the input letter are found.

Hints: Use the first letter of a synonym as the 
key when storing the synonym into the dictionary. 
Assume all letters are in lowercase.
"""


# The program then stores the contents of the text file 
# into a dictionary predefined in the program. 

# load the text file and store it in a dictionary.

# Get the directory path where the text files are located
directory = os.path.dirname(os.path.realpath(__file__))

# Get the list of text files in the directory
files = os.listdir(directory)

# Print the list of text files
for file in files:
    print(file)


# create a dictionary of dictionaries.
# the keys to the first dictionary is word we want a synonym for.
# the values are the individual word dictionaries.
# for the word dictionaries, the keys are the first letter of the synonym.
# the values are the list of synonyms that start with the letter.

dictionary_of_synonym_dictionaries = {}

# loop through the files
for file in files:
    if file.endswith(".txt"):
        print('file:', file)
        # open the file
        with open(file, "r") as f:
            # read the contents of the file
            contents = f.read()
            # print the contets
            print('our contents are: ', contents)
            # split the contents by new line
            
            lines = contents.split("\n")
            # print the lines
            print('our lines are: ', lines)
            
            # get the word from the file name
            word = file.split(".")[0]
            # create a dictionary for the word
            word_dict = {}
            # loop through the lines
            for line in lines:
                # split the line by space
                synonyms = line.split(" ")
                # loop through the synonyms
                for synonym in synonyms:
                    # get the first letter of the synonym
                    first_letter = synonym[0]
                    # check if the first letter is in the word_dict
                    if first_letter in word_dict:
                        # append the synonym to the list
                        word_dict[first_letter].append(synonym)
                    else:
                        # create a new list with the synonym
                        word_dict[first_letter] = [synonym]
            # add the word dictionary to the dictionary of synonym dictionaries
            dictionary_of_synonym_dictionaries[word] = word_dict


# loop through the dictionary of dictionaries and print the contents of each dictionary
