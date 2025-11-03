# -*- coding: utf-8 -*-
"""
13.7 LAB: Pet information (derived classes)
The base class Pet has attributes name and age. 

The derived class Cat inherits attributes from the base class (Pet) 
and includes a breed attribute. Complete the program to:

Create a generic pet, and print the pet's information using print_info().
Create a Cat pet, use print_info() to print the cat's information, 
and add a statement to print the cat's breed attribute.
Ex: If the input is:

Dobby
2
Kreacher
3
Scottish Fold
the output is:

Pet Information: 
   Name: Dobby
   Age: 2
Pet Information: 
   Name: Kreacher
   Age: 3
   Breed: Scottish Fold


Starter Code

class Pet:
    def __init__(self):
        self.name = ''
        self.age = 0
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.name }')
        print(f'   Age: { self.age }')

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self) 
        self.breed = ''

my_pet = Pet()
my_cat = Cat()

pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()

# TODO: Create generic pet (using pet_name, pet_age) 
and then call print_info()

# TODO: Create cat pet (using cat_name, cat_age, cat_breed) 
and then call print_info()

# TODO: Use my_cat.breed to output the breed of the cat

 
"""

class Pet:
    def __init__(self, pet_name, pet_age):
        self.stored_name = pet_name
        self.stored_age = pet_age
    
    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: { self.stored_name }')
        print(f'   Age: { self.stored_age }')
        
    def input_pet_name(self, given_name):
        self.stored_name = given_name
        
    def input_pet_age(self, given_age):
        self.stored_age = given_age
        
class Cat(Pet):
    def __init__(self, pet_name, pet_age, cat_breed):
        Pet.__init__(self, pet_name, pet_age) 
        self.stored_breed = cat_breed
        self.stored_things_I_knocked_off_today = []
        
    def print_info(self):
        Pet.print_info(self)
        print(f'   Breed: { self.stored_breed }')
    
        
if __name__ == "__main__":
    print('welcome to our simple testing...')
    
    hector = Pet('Frank', 6)
    hector.print_info()
    
    pet_name = input('What is your pet name? ')
    pet_age = int(input('What is your pet age? '))
    
    cat_name = input('What is your cat name? ')
    cat_age = int(input('What is your pet age? '))
    cat_breed = input('What type of cat do you have? ')
    
    my_pet = Pet(pet_name, pet_age)
    my_cat = Cat(cat_name, cat_age, cat_breed)
    
    my_pet.print_info()
    
    my_cat.print_info()
    
    

