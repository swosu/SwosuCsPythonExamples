import random

# https://www.programiz.com/python-programming/object-oriented-programming
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.average_speed = 0

    def set_average_speed(self, speed):
        self.average_speed = speed

    def get_average_speed(self):
        return self.average_speed

if __name__ == '__main__':
    print('hello')

    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)

    rp = Parrot("Red", 7)
    sp = Parrot("Fido", 20)

    sp.set_average_speed(random.randint(1,sp.age))
    print(f"Sarah's bird can fly {sp.get_average_speed()} miles per hour right now.")

    rp.set_average_speed(random.randint(1,sp.age))
    print(f"Rooney's bird can fly {rp.get_average_speed()} miles per hour right now.")

    # access the class attributes
    #print("Blu is a {}".format(blu.__class__.species))
    #print("Woo is also a {}".format(woo.__class__.species))
    #print(f"{rp.name} is a {woo.__class__.species}.")

    # access the instance attributes
    #print("{} is {} years old".format( blu.name, blu.age))
    #print("{} is {} years old".format( woo.name, woo.age))
    #print("{} is {} years old".format( rp.name, rp.age))
