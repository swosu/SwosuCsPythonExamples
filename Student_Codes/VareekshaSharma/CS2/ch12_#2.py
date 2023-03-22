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

input_file = input("Enter the name of the input file: ")

# Read input file and create dictionary
data = {}
with open(input_file, 'r') as file:
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        num_seasons = int(lines[i].strip())
        tv_show = lines[i+1].strip()
        if num_seasons in data:
            data[num_seasons].append(tv_show)
        else:
            data[num_seasons] = [tv_show]

# Sort dictionary by key and write to output_keys.txt
with open('output_keys.txt', 'w') as file:
    for key in sorted(data.keys(), reverse=True):
        tv_shows = "; ".join(data[key])
        file.write(str(key) + ": " + tv_shows + "\n")

# Sort dictionary by value and write to output_titles.txt
with open('output_titles.txt', 'w') as file:
    for tv_show in sorted(data.values(), key=lambda x: x[0], reverse=True):
        file.write(tv_show[0] + "\n")
