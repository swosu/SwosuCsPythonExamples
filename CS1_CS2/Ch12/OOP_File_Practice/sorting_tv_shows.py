# print off the files in the current directory
import os
for filename in os.listdir('.'):
    print(filename)


"""
file1.txt
input1.txt
output_keys.txt
simple_file_check.py
sorting_tv_shows.py
words_in_a_range.py
"""

#  read the input file using the file.readlines() method.

our_file = open('file1.txt', 'r')
lines = our_file.readlines()
print(lines)


#  put the contents of the input file into a 
# dictionary where the number of seasons are 
# the keys, and a list of TV shows are the values 
# (since multiple shows could have the same 
# number of seasons).

tv_shows = {}

# Read all lines and strip whitespace
lines = [line.strip() for line in lines]

# Process lines in pairs: seasons, show
for i in range(0, len(lines), 2):
    seasons = int(lines[i])
    show = lines[i + 1]

    if seasons not in tv_shows:
        tv_shows[seasons] = []
    tv_shows[seasons].append(show)

# Print results
for seasons, shows in tv_shows.items():
    print(f"{seasons} seasons:")
    for show in shows:
        print(f"  {show}")


# Sort the dictionary by key (greatest to least) 
sorted_tv_shows = dict(sorted(tv_shows.items(), key=lambda item: item[0], reverse=True))


#output the results to a file named output_keys.txt