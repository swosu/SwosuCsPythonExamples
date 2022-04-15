# https://www.programiz.com/python-programming/object-oriented-programming
class Fish:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.average_speed = 0
        self.distance_covered = 0

