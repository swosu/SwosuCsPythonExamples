# main.py
from pet import Pet, Cat

# Create and print generic pet information
pet_name = input()
pet_age = int(input())
my_pet = Pet(pet_name, pet_age)
my_pet.print_info()

# Create and print cat information including breed
cat_name = input()
cat_age = int(input())
cat_breed = input()
my_cat = Cat(cat_name, cat_age, cat_breed)
my_cat.print_info()


