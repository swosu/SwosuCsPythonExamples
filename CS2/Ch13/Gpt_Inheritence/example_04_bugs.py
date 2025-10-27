# ========================================
# 🏚️ The Bad Idea Pet Adoption Game™
# ========================================

class Pet:
    """Base class for all pets."""
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(f"Pet Information:")
        print(f"   Name: {self.name}")
        print(f"   Age: {self.age}")

    def describe(self):
        print(f"{self.name} is a generic pet. Nothing weird... yet.")

# ------------------------------
# Living Pets (animals)
# ------------------------------
class LivingPet(Pet):
    def __init__(self, name, age=0):
        super().__init__(name, age)
        self.alive = True

    def eat(self):
        print(f"{self.name} munches happily. 🥩")

    def poop(self):
        print(f"{self.name} looks very proud of their little deposit. 💩")

class Mammal(LivingPet):
    def __init__(self, name, age=0, species="Generic Mammal"):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a noise vaguely like '{self.species}' noises.")
# ------------------------------
# Subclasses of Bugs
# ------------------------------
class Spider(LivingPet):
     def __init__(self, name, age=0, species="Generic Spider"):
        super().__init__(name, age)
         self.species = species

    def make_sound(self):
        print(f"{self.name} the {self.breed} meows judgmentally. 😾")

# ------------------------------
# Subclasses of Mammals
# ------------------------------
class Cat(Mammal):
    def __init__(self, name, age=0, breed="Domestic Cat"):
        super().__init__(name, age, "Cat")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} the {self.breed} meows judgmentally. 😾")

class Dog(Mammal):
    def __init__(self, name, age=0, breed="Dog"):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} the {self.breed} barks enthusiastically! 🐶")

# The “Horrible Pet” line-up:
class Lion(Cat):
    def make_sound(self):
        print(f"{self.name} the Lion roars majestically! 🦁")

    def kill_you(self):
        print(f"{self.name} pounces! 💀 You are a snack.")

class Hyena(Dog):
    def make_sound(self):
        print(f"{self.name} the Hyena laughs maniacally. 😈")

    def kill_you(self):
        print(f"{self.name} forms a pack and you don’t make it. 💀")

class Wolf(Dog):
    def make_sound(self):
        print(f"{self.name} howls at the moon. 🌕")

# ------------------------------
# Birds
# ------------------------------
class Bird(LivingPet):
    def __init__(self, name, age=0, species="Bird"):
        super().__init__(name, age)
        self.species = species

    def sing(self):
        print(f"{self.name} the {self.species} chirps melodically. 🎵")

class Parrot(Bird):
    def sing(self):
        print(f"{self.name} squawks, 'Polly wants a bad idea!' 🦜")

# ------------------------------
# Mythical Pets
# ------------------------------
class Dragon(LivingPet):
    def __init__(self, name, age=0, element="Fire"):
        super().__init__(name, age)
        self.element = element

    def breathe(self):
        print(f"{self.name} exhales {self.element}! 🌋")
    
    def kill_you(self):
        print(f"{self.name} incinerates your mortgage paperwork. 🔥")

# ------------------------------
# Unalive Pets
# ------------------------------
class UnalivePet(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.alive = False

class PetRock(UnalivePet):
    def describe(self):
        print(f"{self.name} just sits there. A solid companion. 🪨")

    def eat(self):
        print(f"{self.name} refuses to eat. Dignified silence.")

class ImaginaryPet(UnalivePet):
    def __init__(self, name, power="Unknown"):
        super().__init__(name)
        self.power = power

    def describe(self):
        print(f"{self.name} exists only when you believe hard enough. ✨")
        print(f"They have {self.power} powers.")

# ------------------------------
# Sample Adoptions
# ------------------------------
def run_bad_idea_adoptions():
    print("=== 🏚️ Welcome to the Bad Idea Pet Adoption Center! ===\n")

    pets = [
        Cat("Sir Whiskerton", 2, "Scottish Fold"),
        Dog("Borkley", 4, "Golden Retriever"),
        Lion("Mufatso", 7),
        Hyena("Giggles", 5),
        Wolf("Luna", 3),
        Dragon("Sizzleton", 402, "Plasma Lightning"),
        Parrot("Professor Screech", 11),
        PetRock("Rocky Balboa"),
        ImaginaryPet("Fluffernimbus", "rainbow beam vision")
    ]

    for p in pets:
        print("\n--- New Adoption ---")
        p.print_info()
        if hasattr(p, 'describe'): p.describe()
        if hasattr(p, 'make_sound'): p.make_sound()
        if hasattr(p, 'sing'): p.sing()
        if hasattr(p, 'breathe'): p.breathe()
        if hasattr(p, 'eat'): p.eat()
        if hasattr(p, 'poop'): p.poop()
        if hasattr(p, 'kill_you'): p.kill_you()

    print("\nThank you for adopting irresponsibly! 🫡")

# Run the “game”
if __name__ == "__main__":
    run_bad_idea_adoptions()
