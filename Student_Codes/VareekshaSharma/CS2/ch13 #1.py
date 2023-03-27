'''13.7 LAB: Pet information (derived classes)
The base class Pet has attributes name and age. The derived class Cat inherits attributes from the base class (Pet) and includes a breed attribute. Complete the program to:

Create a generic pet, and print the pet's information using print_info().
Create a Cat pet, use print_info() to print the cat's information, and add a statement to print the cat's breed attribute.
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


Starter Code'''

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

# TODO: Create generic pet (using pet_name, pet_age) and then call print_info()

# TODO: Create cat pet (using cat_name, cat_age, cat_breed) and then call print_info()

# TODO: Use my_cat.breed to output the breed of the cat