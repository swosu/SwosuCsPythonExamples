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