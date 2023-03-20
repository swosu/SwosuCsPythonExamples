'''12.8 LAB: Words in a range (lists)
Write a program that first reads in the name of an input file, followed 
by two strings representing the lower and upper bounds of a search range. 
The file should be read using the file.readlines() method. The input file 
contains a list of alphabetical, ten-letter strings, each on a separate line. 
Your program should determine if the strings from the list are within that 
range (inclusive of the bounds) and output the results.

Ex: If the input is:

input1.txt
ammoniated
millennium
and the contents of input1.txt are:

aspiration
classified
federation
graduation
millennium
philosophy
quadratics
transcript
wilderness
zoologists
the output is:

aspiration - in range
classified - in range
federation - in range
graduation - in range
millennium - in range
philosophy - not in range
quadratics - not in range
transcript - not in range
wilderness - not in range
zoologists - not in range
Notes:

End the output with a newline.
All input files are hosted in the zyLab and file names can be directly 
referred to. input1.txt is available to download so that the contents 
of the file can be seen. In the tests, the first word input always 
comes alphabetically before the second word input.


Starter Code'''

# Type your code here. 