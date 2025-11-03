# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 13:15:55 2022

@author: evertj
"""

def fibbo(n):
    print('you gave us', n)
    if (0 == n):
        print('that is a big fat zero!!!')
        return 0
    elif (1 == n):
        print('yeah, the first month')
        return 1
    elif 0 > n:
        print("negative bunnies don't exist...")
        return -1
    elif 1 < n:
        #initialize the list with starting elements: 0, 1
        fibonacciSeries = [0,1]
        for i in range(2, n+1):
            #elment in series = sum of its previous two numbers
            nextement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
            #append the element to the series
            fibonacciSeries.append(nextement)
        print('after the for loop.')
        print(fibonacciSeries)
        return fibonacciSeries[-1]
    else:
        return 0
    
    
print('start')

n = 5
output = fibbo(n)
print('output was:', output)
