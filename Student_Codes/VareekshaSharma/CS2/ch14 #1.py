'''14.7 LAB: Fibonacci sequence (recursion)
The Fibonacci sequence begins with 0 and then 1 follows. All 
subsequent values are the sum of the previous two, for example: 
0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, 
which takes in an index, n, and returns the nth value in the 
sequence. Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
Note: Use recursion and DO NOT use any loops.


Starter Code'''

# TODO: Write recursive fibonacci() function

if __name__ == "__main__":
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')