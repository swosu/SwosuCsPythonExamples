class Dog:
    def __init__(self, name, eye_color="brown"):
        # __init__ runs whenever we create a new Dog
        self.name = name
        self.color = "brown"  # Attribute with a default value
        self.eye_color = eye_color  # New attribute with default value "brown"

    def bark(self):
        # A method: something our dog can do
        print(f"{self.name} says: Woof woof!")

    def sit(self):
        print(f"{self.name} sits down.")

    def eat(self, food):
        print(f"{self.name} is eating {self.food_choice}.")

# Create two Dog objects
dog_one = Dog("Buddy")
dog_two = Dog("Bella")
dog_three = Dog("Charlie")

dog_one.color = "black"  # Change the color attribute for dog_one
dog_two.color = "white"   # Change the color attribute for dog_two

dog_one.food_choice = "chicken"  # Add a new attribute food_choice to dog_one
dog_two.eat()
# Call their method
dog_one.bark()   # Buddy says: Woof woof!
dog_two.bark()   # Bella says: Woof woof!

print(f"{dog_one.name} is {dog_one.color}.")  # Buddy is black.
print(f"{dog_two.name} is {dog_two.color}.")  # Bella is brown.
print(f"{dog_three.name} is {dog_three.color}.")  # Charlie is brown.

dog_one.sit()  # Buddy sits down.
dog_two.sit()  # Bella sits down.
dog_three.sit()  # Charlie sits down.   