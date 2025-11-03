# https://www.programiz.com/python-programming/object-oriented-programming
class Parrot:

    # class attribute
    species = "bird"

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