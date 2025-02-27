# pet.py
class Pet:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def print_info(self):
        print(f'Pet Information:')
        print(f'   Name: {self.name}')
        print(f'   Age: {self.age}')


class Cat(Pet):
    def __init__(self, name='', age=0, breed=''):
        super().__init__(name, age)
        self.breed = breed
        self.is_fixed = True
        self.has_claws = True

    def print_info(self):
        super().print_info()
        print(f'   Breed: {self.breed}')
        print(f'   Fixed: {self.is_fixed}')
        print(f'   Declawed: {not self.has_claws}')
