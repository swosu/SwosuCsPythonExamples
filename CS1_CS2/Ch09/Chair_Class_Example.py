# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:07:36 2023

@author: evertj
"""

import random
    
class Chair_Class:
    
    def __init__(self, given_name):
        self.data = []
        print(f'my given name is: {given_name}.')
        self.our_saved_name = given_name 
        self.leg_count = 3
        self.lucky_number = random.randint(1, 1_000_000)
        
    def print_my_stored_name(self):
        print(f'my stored name is: {self.our_saved_name}.')
        
    def do_other_stuff():
        print('we are doing other stuff.')
        
    def set_leg_count(self, number_of_legs):
        print("isn't that nice...")
        self.leg_count = number_of_legs
        print(f'our number of legs is: {self.leg_count}')
        
    def print_leg_count(self):
        print(f'our leg count is: {self.leg_count}.')


if __name__ == '__main__':
    print('hello')
    
    jeremy_chair = Chair_Class('stool')
    attrs = vars(jeremy_chair)
    print(', '.join("%s: %s" % item for item in attrs.items()))
    
    
    jeremy_chair.print_my_stored_name()
    Chair_Class.do_other_stuff()
    jeremy_chair.print_my_stored_name()
    Chair_Class.do_other_stuff()
    Chair_Class.do_other_stuff()
    jeremy_chair.print_leg_count()
    
    joe_chair = Chair_Class('wheelie chair')
    joe_chair.print_my_stored_name()
    joe_chair.set_leg_count(4)
    
    attrs = vars(joe_chair)
    print('joe chair')
    print(', '.join("%s: %s" % item for item in attrs.items()))