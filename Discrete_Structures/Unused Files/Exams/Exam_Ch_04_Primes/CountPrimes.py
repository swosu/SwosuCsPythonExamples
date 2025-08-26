'''
Programming: Estimating the number of primes less than x Write a program to count how many primes are less than 10, 100, 1,000, ...,
100,000,000. Fit a curve to your data and estimate the number of primes less than x, where x is a positive integer.
'''
import sympy
range_limit = 1
step = 2
for index in range (1,20):
    range_limit = range_limit * step
    #print (range_limit)
    number_of_primes = 0

    for check_number in range (1,range_limit):
        if(sympy.isprime(check_number)):
            number_of_primes += 1
    #print (number_of_primes)
    #print (f'there are {number_of_primes} less than {range_limit}.')
    print (f'{range_limit}\t {number_of_primes}')
