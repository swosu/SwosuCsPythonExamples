'''12.10 LAB: Sorting TV Shows (dictionaries and lists)
Write a program that first reads in the name of an input file and then 
reads the input file using the file.readlines() method. The input file 
contains an unsorted list of number of seasons followed by the corresponding 
TV show. Your program should put the contents of the input file into a 
dictionary where the number of seasons are the keys, and a list of TV 
shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (greatest to least) and output the results 
to a file named output_keys.txt. Separate multiple TV shows associated 
with the same key with a semicolon (;), ordering by appearance in the 
input file. Next, sort the dictionary by values (in reverse alphabetical 
order), and output the results to a file named output_titles.txt.

Ex: If the input is:

file1.txt
and the contents of file1.txt are:

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote
the file output_keys.txt should contain:

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons
and the file output_titles.txt should contain:

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace
Note: End each output file with a newline, and file1.txt is available to download.


Starter Code

contents of file1.txt

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote'''

# Type your code here

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

'''filename = input("Enter the name of the input file: ")

# Create an empty dictionary to store the data
data = {}

# Read the input file into the dictionary
with open(filename, 'r') as file:
    for line in file:
        line = line.strip().split()
        seasons = (line[0])
        title = ' '.join(line[1:])
        if seasons in data:
            data[seasons].append(title)
        else:
            data[seasons] = [title]

# Sort the dictionary by key (greatest to least) and output the results to a file
with open("output_keys.txt", 'w') as file:
    for key in sorted(data.keys(), reverse=True):
        titles = ';'.join(data[key])
        file.write(f"{key}: {titles}\n")

# Sort the dictionary by values (in reverse alphabetical order) and output the results to a file
with open("output_titles.txt", 'w') as file:
    for key, values in sorted(data.items(), key=lambda x: x[1], reverse=True):
        for title in sorted(values, reverse=True):
            file.write(f"{key}: {title}\n")

filename = input("Enter the name of the input file: ")

# Create an empty dictionary to store the data
data = {}

# Read the input file
with open(filename, 'r') as file:
    lines = file.readlines()

# Parse the lines of the input file and add them to the dictionary
for line in lines:
    # Split the line into a number of seasons and a TV show
    num_seasons, tv_show = line.strip().split(' ')

    # Convert the number of seasons to an integer
    num_seasons = int(num_seasons)

    # If the number of seasons is not already in the dictionary, add it with an empty list
    if num_seasons not in data:
        data[num_seasons] = []

    # Add the TV show to the list of shows for the corresponding number of seasons
    data[num_seasons].append(tv_show)

# Sort the dictionary by key (greatest to least)
sorted_data_by_key = dict(sorted(data.items(), reverse=True))

# Output the results to a file named output_keys.txt
with open('output_keys.txt', 'w') as file:
    for num_seasons, tv_shows in sorted_data_by_key.items():
        # Join the list of TV shows with a semicolon and write to the output file
        file.write(f'{num_seasons}: {": ".join(tv_shows)}\n')

# Sort the dictionary by values (in reverse alphabetical order)
sorted_data_by_value = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

# Output the results to a file named output_titles.txt
with open('output_titles.txt', 'w') as file:
    for num_seasons, tv_shows in sorted_data_by_value.items():
        # Join the list of TV shows with a semicolon and write to the output file
        file.write(f'{num_seasons}: {": ".join(tv_shows)}\n')
'''

input_file = input("Enter the name of the input file: ")

# Read the input file and build the dictionary
shows = {}
with open(input_file) as f:
    lines = f.readlines()
    for line in lines:
        num_seasons, title = line.strip().split(maxsplit=1), line.strip().split(maxsplit=1)
        num_seasons = int(num_seasons)
        if num_seasons not in shows:
            shows[num_seasons] = []
        shows[num_seasons].append(title)

# Sort the dictionary by key (greatest to least)
sorted_shows_by_key = dict(sorted(shows.items(), reverse=True))

# Output the sorted dictionary to a file
with open("output_keys.txt", "w") as f:
    for num_seasons, titles in sorted_shows_by_key.items():
        f.write(f"{num_seasons}: ")
        f.write("; ".join(titles))
        f.write("\n")

# Sort the dictionary by values (in reverse alphabetical order)
sorted_shows_by_title = dict(sorted(shows.items(), key=lambda x: x[1][0], reverse=True))

# Output the sorted dictionary to a file
with open("output_titles.txt", "w") as f:
    for num_seasons, titles in sorted_shows_by_title.items():
        f.write(f"{num_seasons}: ")
        f.write("; ".join(titles))
        f.write("\n")


