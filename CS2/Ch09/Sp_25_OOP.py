class Pet:
    def __init__(self, name = "none", species = "unknown"):
        self.__name = name
        self.__owner = "none"
        self.__species = species
        self.__hunger_level = 5
        print("I am a pet!") # Output: I am a pet!

    def __str__(self):
        return (f"Pet(name = {self.__name} \n"
            f"     owner = {self.__owner} \n"
            f"     species = {self.__species}\n"
            f"     hunger_level = {self.__hunger_level}")
    
    def set_owner(self, owner_name):
        self.__owner = owner_name

    def eat(self):
        print("I like to eat because I am not a rock!")

    def set_species(self, species):
        self.__species = species

if __name__ == "__main__":
    lillie = Pet("lillie") # Create an instance of the Pet class
    sam = Pet("sam", "Bradford") # Create another instance of the Pet class

    lillie.set_species("Dog") # Set the species of lillie

    lillie.eat()  # Call the eat method # Output: Hello!
    sam.eat()  # Call the eat method # Output: Hello!

    lillie.set_owner("Alice") # Set the owner of lillie
    sam.set_owner("Bob") # Set the owner of sam

    sam.__owner = "Charlie" # Change the owner

    print(lillie) # Output: Pet(owner=none)
    print(sam)    # Output: Pet(owner=none)

    
