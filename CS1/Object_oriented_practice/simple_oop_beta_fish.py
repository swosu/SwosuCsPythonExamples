import random


# https://www.programiz.com/python-programming/object-oriented-programming
class Beta_Fish:

    # class attribute
    species = "fish"

    # instance attribute
    def __init__(self, name):
        self.name = name
        self.has_weapon = True
        self.weapon_damage = 0
        self.armor_strength = 0
        self.health = 0
        self.has_magic = True
        self.magic_attack = 0
        self.magic_defend = 0


if __name__ == '__main__':
    #print('hello')

    # instantiate the Beta_Fish class
    blu = Beta_Fish("Blu")
    woo = Beta_Fish("Woo")

    rooneys_fish = Beta_Fish("Red")
    sarahs_fish = Beta_Fish("Fido")

    #sarahs_fish.set_average_speed(random.randint(1,sarahs_fish.age))
    #print(f"Sarah's bird can fly {sarahs_fish.get_average_speed()} miles per hour right now.")

    keep_going = True

    rounds = 0

    while(keep_going):
        # find speed for this leg
        #rooneys_fish.set_average_speed(random.randint(1,rooneys_fish.age))
        rounds += 1
        print('round complete')

        if 3 < rounds:
            keep_going = False




    # access the class attributes
    #print("Blu is a {}".format(blu.__class__.species))
    #print("Woo is also a {}".format(woo.__class__.species))

    #print(f"{rooneys_fish.name} is a {woo.__class__.species}.")


    # access the instance attributes
    #print("{} is {} years old".format( blu.name, blu.age))
    #print("{} is {} years old".format( woo.name, woo.age))

    #print("{} is {} years old".format( rooneys_fish.name, rooneys_fish.age))

