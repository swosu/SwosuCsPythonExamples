"""11.11 LAB: Unique random numbers (random module)
Given integer inputs seed, how_many, and max_num, generate a list of how_many 
unique random integers from 0 to max_num (inclusive).

Complete function unique_random_ints(how_many, max_num):
Generate a list of how_many random integers from 0 to max_num (inclusive).
When a random number exists in the list, a new random number must be 
generated; use a global variable, retries, to count the number of times an 
existing number is generated.
Return the list.
Complete __main__:
Initialize the random module with the seed value.
Call unique_random_ints() to get a list of random integers.
Output the list of random integers and the value of retries, according to 
the output format shown in the example below.
Refer to the section on the standard library to learn more about the random 
module and pseudo-random numbers.

Ex: If the input is:

2
5
7
the output is

0 1 5 2 4 retries=1


Starter Code"""

import random

def unique_random_ints(how_many, max_num):
    #Return a list of how_many unique randomly generated numbers from
    #0 to max_num (inclusive) using seed to initialize the random module

    # Type your code here. #


if __name__ == '__main__':
    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    # Type your code here. #