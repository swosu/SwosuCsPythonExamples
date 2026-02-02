class Dog:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.number_of_legs = 4
        self.has_tail = True
        self.fur_color = "brown"
        self.fur_length = "short"

    def fetch(self, item):
        print(f"{self.name} is fetching the {item}!")

    def bark(self):
        print("Woof!")

    def sit(self):
        print(f"{self.name} sits.")


# --- demo / test code ---
my_dog = Dog("Duke", "Jeremy")
my_dog.bark()
my_dog.sit()
print(my_dog.owner)

ripley = Dog("Ripley", "Ryan")
ripley.fetch("ball")