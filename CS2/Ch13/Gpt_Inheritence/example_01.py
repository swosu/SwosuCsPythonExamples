# Base class: Pet
class Pet:
    def __init__(self):
        # Initialize default values
        self.name = ''
        self.age = 0

    def __str__(self):
        # String representation for printing
        return f'Pet Information:\n   Name: {self.name}\n   Age: {self.age}'

    def print_info(self):
        # Print general pet information
        print(self)

# Derived class: Cat (inherits from Pet)
class Cat(Pet):
    def __init__(self):
        # Initialize the parent class first (Pet)
        super().__init__()   # same as Pet.__init__(self)
        # Add new attribute for breed
        self.breed = ''

# Create empty Pet and Cat objects
my_pet = Pet()
my_cat = Cat()

# Input data
pet_name = input()
pet_age = int(input())
cat_name = input()
cat_age = int(input())
cat_breed = input()

# Assign values to the Pet instance
my_pet.name = pet_name
my_pet.age = pet_age

# Assign values to the Cat instance
my_cat.name = cat_name
my_cat.age = cat_age
my_cat.breed = cat_breed

# Print both
my_pet.print_info()
my_cat.print_info()
print(f'   Breed: {my_cat.breed}')
