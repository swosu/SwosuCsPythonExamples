"""
6.21 LAB: Convert to binary - functions

Write a program that 

takes in a positive integer as input, and 

outputs a string of 1's and 0's representing the integer in binary. 

For an integer x, the algorithm is:

As long as x is greater than 0
   Output x % 2 (remainder is either 0 or 1)
   x = x // 2
Note: The above algorithm outputs the 0's and 1's in reverse order. 

You will need to write a second function to reverse the string.

Ex: If the input is:

6
the output is:

110
The program must define and call the following two functions. 

Define a function named int_to_reverse_binary() 
that takes an integer as a parameter and 
returns a string of 1's and 0's representing the integer in binary (in reverse). 

Define a function named string_reverse() that takes an input string as a parameter 
and returns a string representing the input string in reverse.
def int_to_reverse_binary(integer_value)
def string_reverse(input_string)

Book Starter Code:

# Define your functions here.

if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
"""

def say_hello():
    print('hello')
    
def say_howdy(repeat_count):
    for index in range(0, repeat_count):
        print(f'howdy count is {index}')
        
def get_name():
    the_name_you_are_wanting = input('what is your name?')
    return the_name_you_are_wanting

def get_user_number():
    our_number = int(input('what number would you like to convert?'))
    return our_number

def get_binary_conversion_reversed(working_number):
    binary_conversion_reversed = ''
    while working_number > 0:
        binary_conversion_reversed = binary_conversion_reversed +\
            str(working_number % 2)
        #print( working_number % 2, end = '')# (remainder is either 0 or 1)
        
        working_number = working_number // 2
    #print()
    #print(binary_conversion_reversed)
    return binary_conversion_reversed

def get_reversed_string(original_string):
    reversed_string = original_string  [::-1]
    return reversed_string

if __name__ == '__main__':
    
    #say_hello()
    #say_howdy(11)
    
    #my_name = get_name()
    #print(f'hello {my_name}.')
    our_number = get_user_number()
    
    
    binary_conversion_reversed = get_binary_conversion_reversed(our_number)

    
    binary_conversion = get_reversed_string(binary_conversion_reversed)
    print(binary_conversion)
    