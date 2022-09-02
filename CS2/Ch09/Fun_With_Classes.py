# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:23:11 2022

@author: evertj
"""

class Time:
    """ A class that represents a time of day """
    def __init__(self):
        self.hours = 0
        self.minutes = 0


my_time = Time()
my_time.hours = 7
my_time.minutes = 15

print(f'my_time: {my_time.hours} hours', end=' ')
print(f'and {my_time.minutes} minutes')

your_time = Time()
your_time.hours = 42
your_time.minutes = 3

print(f'your_time: {your_time.hours} hours', end=' ')
print(f'and {your_time.minutes} minutes')

miller_time = Time()
miller_time.hours = 5
miller_time.minutes = 0

print(f'miller_time: {miller_time.hours} hours', end=' ')
print(f'and {miller_time.minutes} minutes')

print('now we change miller time.')
miller_time.hours = 17

print(f'miller_time: {miller_time.hours} hours', end=' ')
print(f'and {miller_time.minutes} minutes')

print(f'your_time: {your_time.hours} hours', end=' ')
print(f'and {your_time.minutes} minutes')

print(f'my_time: {my_time.hours} hours', end=' ')
print(f'and {my_time.minutes} minutes')