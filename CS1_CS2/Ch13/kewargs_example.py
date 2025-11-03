# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 13:55:05 2023

@author: evertj
"""

class Pet():
    def __init__(self, **kwargs):
        self.name = kwargs["pet_name"] if "pet_name" in kwargs else "You're pet does not have a name..."
        self.age = kwargs["pet_age"] if "pet_age" in kwargs else "You're pet does not have a name..."
        self.breed = kwargs["pet_breed"] if "pet_breed" in kwargs else "You're pet is unidentifiable..."
        print(self.__dict__)
    def sort_pet(self):
        if self.breed == "cat":
            print(f"You're cat may be {self.age}, but they still have 9 lives!!!")

pet1 = Pet(pet_name= input("what is your pet's name???"), 
           pet_age= input("What is your pet's age???"), 
           pet_breed= input("What is your pet's breed???"))


