# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:33:11 2022

@author: evertj
"""

class Time:
    def __init__(self):
        self.seconds = 0
        self.hours = 0
        self.minutes = 0
        self.total_time_in_seconds = 0

    def print_time(self):
        print('Hours:', self.hours, end=' ')
        print('Minutes:', self.minutes, end=' ')
        print('Seconds:', self.seconds)
        
    def print_total_time_in_seconds(self):
        print('total time in seconds: ', self.total_time_in_seconds)
        
    def convert_to_seconds(self):
        self.total_time_in_seconds = self.hours * 3600 + \
            self.minutes * 60 + self.seconds


time1 = Time()
time1.hours = 10
time1.minutes = 10
time1.seconds = 5
time1.print_time()
time1.print_total_time_in_seconds()
print('run conversion')
time1.convert_to_seconds()
time1.print_total_time_in_seconds()

