# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:54:35 2022

@author: evertj
"""

def is_odd(number):
    # if the number divided by 2 has a remainder zero, its even
    # % is the modulo operator.
    # Modulo means what is the remainder after division.
    if 0 == number % 2:
        return False
    else:
        return True

def remove_evens(nums):
    # Type your code here.
    #print('hello from inside the function.')
    seperate_list = []
    #print(f'here is our initial seperate list: {seperate_list}.')
    for number in nums:
        #print(f'our number is: {number}.')
        if is_odd(number):
            seperate_list.append(number)
            #print(f'after {number} our seperate list is: {seperate_list}.')
    return seperate_list
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 42]
    result = remove_evens(nums)
    #print('hello')
    
    print(result)