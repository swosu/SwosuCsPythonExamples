"""
Write a program that 
first reads in the name of an input file 
and then reads the file using the csv.reader() method. 

The file contains a list of words separated by commas. 

The program must output the words 
and their frequencies 
(the number of times each word appears in the file) 
without any duplicates.
"""

input_file = input("Enter the name of the input file: ")

import csv

with open(input_file, 'r') as f:
    reader = csv.reader(f)
    words = []
    for row in reader:
        for word in row:
            words.append(word)

#create a dictionary to store the frequency of each word

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

for word in word_freq:
    print(f"{word}: {word_freq[word]}")