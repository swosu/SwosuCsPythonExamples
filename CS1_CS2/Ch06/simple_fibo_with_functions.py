"""
The Fibonacci sequence begins with 0 
and then 1 follows. 
All subsequent values are the sum of the previous two, 
ex: 0, 1, 1, 2, 3, 5, 8, 13. 
Complete the fibonacci() function, 
which has an index, n (starting at 0), 
as a parameter and returns the nth value in the sequence. 
Any negative index values should return -1.

Ex: If the input is:

7
the output is:

fibonacci(7) is 13
"""
# Starter Code :

 

def fibonacci(n):
    # Type your code here. 

    if -1 >= n:
        return -1
    elif 1 == n:
        return 0
    elif 2 == n:
        return 1
    else:
        number_list = [0, 1]
        for index in range (2,(n + 1)):
            number_list.append(number_list[-1] + number_list[-2])

        print('our number list is: ', number_list)

        return number_list[-1]
        


if __name__ == '__main__':
    #start_num = int(input())
    start_num = 7
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
