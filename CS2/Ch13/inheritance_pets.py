# Base class: Pet
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        print(f"A new {self.species} named {self.name} has been adopted!")

    def speak(self):
        print(f"{self.name} makes a mysterious pet noise...")

    def info(self):
        return f"{self.name} is a {self.species}."

# Derived class: Dog
class Dog(Pet):
    def __init__(self, name, breed):
        # super() calls the __init__ of the parent class Pet
        super().__init__(name, species="dog")
        self.breed = breed
        print(f"{self.name} is a {self.breed} dog!")

    def speak(self):
        # super() can also be used to call a parent method
        super().speak()
        print(f"{self.name} barks: 'Woof! Woof!'")

# Derived class: Cat
class Cat(Pet):
    def __init__(self, name, color):
        # Call the parent constructor
        super().__init__(name, species="cat")
        self.color = color
        print(f"{self.name} is a {self.color} cat!")

    def speak(self):
        print(f"{self.name} meows: 'Meow~'")

# Let's see it in action!
if __name__ == "__main__":
    bella = Dog("Bella", "Golden Retriever")
    bella.speak()
    print(bella.info())

    print()  # separator

    luna = Cat("Luna", "gray")
    luna.speak()
    print(luna.info())
