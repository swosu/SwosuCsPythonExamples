class Dog:
    def __init__(self, name, breed):
        # Object attributes (also called instance variables)
        self.name = name
        self.breed = breed
    
    def bark(self):
        # Method that prints a message
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Golden Retriever")

#please print off the dog name and breed
print(f"my dog is named {my_dog.name} and is a {my_dog.breed}")
Ryder_dog = Dog("Scooby", "Scottish Terrier")
print(f"Ryder's Dog is named {Ryder_dog.name} and is a {Ryder_dog.breed}")

my_dog.breed = "Dalmatian"
print(f"my dog is named {my_dog.name} and is a {my_dog.breed}")
