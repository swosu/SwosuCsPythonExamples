import random

# https://www.programiz.com/python-programming/object-oriented-programming
class Beta_Fish:

    # class attribute
    species = "fish"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.average_speed = 0
        self.distance_covered = 0

    def set_average_speed(self, speed):
        self.average_speed = speed

    def get_average_speed(self):
        return self.average_speed

    def add_to_distance(self, distance):
        self.distance_covered += distance

    def get_distance(self):
        return self.distance_covered


if __name__ == '__main__':
    #print('hello')

    # instantiate the Beta_Fish class
    blu = Beta_Fish("Blu", 10)
    woo = Beta_Fish("Woo", 15)

    rooneys_fish = Beta_Fish("Red", 20)
    sarahs_fish = Beta_Fish("Fido", 20)

    sarahs_fish.set_average_speed(random.randint(1,sarahs_fish.age))
    print(f"Sarah's bird can fly {sarahs_fish.get_average_speed()} miles per hour right now.")

    rooneys_fish.set_average_speed(random.randint(1,rooneys_fish.age))
    print(f"Rooney's bird can fly {rooneys_fish.get_average_speed()} miles per hour right now.")

    race_distance = 100
    keep_going = True

    while(keep_going):
        # find speed for this leg
        rooneys_fish.set_average_speed(random.randint(1,rooneys_fish.age))
        sarahs_fish.set_average_speed(random.randint(1,sarahs_fish.age))

        print(f'{rooneys_fish.name} and fly {rooneys_fish.get_average_speed()}')
        print(f'{sarahs_fish.name} and fly {sarahs_fish.get_average_speed()}')

        # add that time of flight times speed to the distance_covered
        rooneys_fish.add_to_distance(rooneys_fish.get_average_speed())
        sarahs_fish.add_to_distance(sarahs_fish.get_average_speed())

        print(f'\n{rooneys_fish.name} has covered {rooneys_fish.get_distance()}')
        print(f'{sarahs_fish.name} has covered {sarahs_fish.get_distance()}')

        if rooneys_fish.get_distance() > race_distance or sarahs_fish.get_distance() > race_distance:
            keep_going = False

    if rooneys_fish.get_distance() > sarahs_fish.get_distance():
        print(f"{rooneys_fish.name} is the winner!")
    else:
        print(f"{sarahs_fish.name} is the winner!")



    # access the class attributes
    #print("Blu is a {}".format(blu.__class__.species))
    #print("Woo is also a {}".format(woo.__class__.species))
    #print(f"{rooneys_fish.name} is a {woo.__class__.species}.")

    # access the instance attributes
    #print("{} is {} years old".format( blu.name, blu.age))
    #print("{} is {} years old".format( woo.name, woo.age))
    #print("{} is {} years old".format( rooneys_fish.name, rooneys_fish.age))
