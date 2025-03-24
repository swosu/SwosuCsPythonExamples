class Pet:
    """
    A simple class to represent a pet.
    
    Attributes:
        name (str): The name of the pet.
        species (str): The type of animal the pet is.
        is_alive (bool): Whether the pet is alive.
        hunger (int): A measure of how hungry the pet is (0-10).
        energy (int): A measure of how much energy the pet has (0-10).
    """
    
    def __init__(self, name, species):
        """Initialize the pet with a name and species, defaulting to alive, not hungry, and full of energy."""
        self.name = name
        self.species = species
        self.is_alive = True
        self.hunger = 5  # 0 means full, 10 means very hungry
        self.energy = 5  # 0 means exhausted, 10 means fully rested

    def speak(self):
        """Make the pet produce a sound based on its species."""
        if self.species == "dog":
            return "Woof!"
        elif self.species == "cat":
            return "Meow!"
        elif self.species == "bird":
            return "Chirp!"
        else:
            return "Some generic animal noise!"

if __name__ == "__main__":
    
    #print(Pet.__doc__)
    # Creating pet instances
    pet1 = Pet("Buddy", "dog")
    parker_pet = Pet("Octavia", "cat")

    print(parker_pet.speak())  # Should print "Woof!"