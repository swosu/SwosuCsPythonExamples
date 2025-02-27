"""
Write a program that first reads in 
the name of an input file as a command line argument, 
followed by two strings, also on the command line, 
representing the lower and upper bounds of a search range. 

The file should be read using the file.readlines() method. 

The input file contains a list of alphabetical, ten-letter strings, 
each on a separate line. 
Your program should determine if the strings from the list are 
within that range (inclusive of the bounds) and output the results.
"""

import sys
import os

if len(sys.argv) != 4:
    
    print(f'Usage: {sys.argv[0]} input_file lower_bound upper_bound')
    sys.exit(1)  # 1 indicates error


print(f'Opening file {sys.argv[1]}.')

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# we should use the readlines method
lines = f.readlines()
"""
for word in lines:
    word = word.strip() 
    print(f"word: {word}")
"""

print(f'Closing file {sys.argv[1]}')
f.close()  # Done with the file, so close it

print('now we should print the results')

words_in_range = []
words_not_in_range = []

for word_index in lines:
    word = word_index.strip()
    #print(f"our word is: {word}")
    if word >= sys.argv[2] and word <= sys.argv[3]:
        words_in_range.append(word)
    else:
        words_not_in_range.append(word)

print(f"Words in range: {words_in_range}")
print(f"Words not in range: {words_not_in_range}")