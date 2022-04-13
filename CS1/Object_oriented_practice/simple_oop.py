# https://www.programiz.com/python-programming/object-oriented-programming
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    print('hello')

    # instantiate the Parrot class
    blu = Parrot("Blu", 10)
    woo = Parrot("Woo", 15)
    rp = Parrot("Red", 7)

    # access the class attributes
    print("Blu is a {}".format(blu.__class__.species))
    print("Woo is also a {}".format(woo.__class__.species))
    print(f"{rp.name} is a {woo.__class__.species}.")

    # access the instance attributes
    print("{} is {} years old".format( blu.name, blu.age))
    print("{} is {} years old".format( woo.name, woo.age))
    print("{} is {} years old".format( rp.name, rp.age))
