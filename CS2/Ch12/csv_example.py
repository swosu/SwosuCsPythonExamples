print('hello')

import csv
import random

file_name = input('what file would you like to import?')

word_list = []

with open(str(file_name), 'r') as csvfile:
    user_file = csv.reader(csvfile, delimiter=',')

    for row in user_file:
        for index in range(len(row)):
            if row[index] not in word_list:
                print('{} {}'.format(row[index], row.count(row[index])))
                word_list.append(row[index])


herman_strength = 100
sherman_strength = 100

""" We are going to have two characters.
We are going to load their health from a csv file.
We are going to have them fight
We are going to append who wins to a different csv file.

After 100 battles, we will ask the csv file who won the most"""

# 1. Create the CSV file

#import csv # imported earlier
with open('herman_strength.csv', 'w', newline='') as csv_health_file:
    health_writer = csv.writer(csv_health_file, delimiter=',',
                            quotechar=' ',  quoting=csv.QUOTE_MINIMAL)
    health_writer.writerow([100])

with open('sherman_strength.csv', 'w', newline='') as csv_health_file:
    health_writer = csv.writer(csv_health_file, delimiter=',',
                            quotechar=' ',  quoting=csv.QUOTE_MINIMAL)
    health_writer.writerow([100])

# 2. Read the data from the CSV file

#import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

with open('herman_strength.csv',  newline='') as csv_health_file:
    health_reader = csv.reader(csv_health_file, delimiter=',',
                            quotechar=' ')
    read_in_herman_health = int(open('herman_strength.csv','r')
    #for row in health_reader:
    #    print(', '.join(row))

print('herman health is', read_in_herman_health)
