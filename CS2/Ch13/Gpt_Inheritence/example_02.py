# Base Class
class Pet:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: {self.name}')
        print(f'   Age: {self.age}')

# Derived classes
class Cat(Pet):
    def __init__(self, name='', age=0, breed=''):
        super().__init__(name, age)
        self.breed = breed

    def print_info(self):
        super().print_info()
        print(f'   Breed: {self.breed}')

# "Dangerous" subclasses
class WildCat(Cat):
    def __init__(self, name='', age=0, breed='', danger_level='high'):
        super().__init__(name, age, breed)
        self.danger_level = danger_level

    def make_noise(self):
        print(f'{self.name} roars menacingly! 🦁')

    def kill_you(self):
        print(f'{self.name} ({self.breed}) pounces! 💀 You are definitely lunch.')

class WildDog(Pet):
    def __init__(self, name='', age=0, species='Hyena'):
        super().__init__(name, age)
        self.species = species

    def laugh(self):
        print(f'{self.name} the {self.species} laughs eerily in the distance... 😈')

    def kill_you(self):
        print(f'{self.name} ({self.species}) charges with a blood-curdling scream! 💀')

# Examples in action
print("=== Tame Pets ===")
my_pet = Pet("Mittens", 3)
my_cat = Cat("Fluffy", 2, "Scottish Fold")

my_pet.print_info()
my_cat.print_info()

print("\n=== Horrible Pets ===")
scar = WildCat("Scar", 5, "Lion")
scar.print_info()
scar.make_noise()
scar.kill_you()

giggles = WildDog("Giggles", 4, "Hyena")
giggles.print_info()
giggles.laugh()
giggles.kill_you()
