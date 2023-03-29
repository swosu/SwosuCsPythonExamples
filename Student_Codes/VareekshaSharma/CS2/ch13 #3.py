'''13.11 LAB: Plant information
Given a base Plant class and a derived Flower class, write a program to create a list called my_garden. Store objects that belong to the Plant class or the Flower class in the list. Create a function called print_list(), that uses the print_info() instance methods defined in the respective classes and prints each element in my_garden. The program should read plants or flowers from input (ending with -1), add each Plant or Flower to the my_garden list, and output each element in my_garden using the print_info() function.

Note: A list can contain different data types and also different objects.

Ex. If the input is:

plant Spirea 10 
flower Hydrangea 30 false lilac 
flower Rose 6 false white
plant Mint 4
-1
the output is:

Plant Information: 
   Plant name: Spirea
   Cost: 10

Plant Information: 
   Plant name: Hydrangea
   Cost: 30
   Annual: false
   Color of flowers: lilac

Plant Information: 
   Plant name: Rose
   Cost: 6
   Annual: false
   Color of flowers: white

Plant Information: 
   Plant name: Mint
   Cost: 4


Starter Code'''

class Plant:
    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')

class Flower(Plant):
    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f'   Plant name: { self.plant_name }')
        print(f'   Cost: { self.plant_cost }')
        print(f'   Annual: { self.is_annual }')
        print(f'   Color of flowers: { self.color_of_flowers }')

# TODO:  Define the print_list() function that prints a list of plant (or flower) objects 
def print_list(my_garden):
    for plant in my_garden:
        plant.print_info()
        print()

if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input("Enter the plant/flower and it's details in the format (without the commas)): plant/flower, name, cost, true or false if annual or not, and flower color: ")
    
    while user_string != '-1':
        plant_type, *args = user_string.split()
        plant_name, plant_cost = args[:2]

        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        if plant_type == "plant":
            my_garden.append(Plant(plant_name, int(plant_cost)))
        elif plant_type == "flower":
            is_annual = args[2] == 'true'
            color_of_flowers = args[3]
            my_garden.append(Flower(plant_name, int(plant_cost), is_annual, color_of_flowers))
        user_string = input("if finished, type '-1,' or continue giving input: ")

    # TODO: Call the print_list() function to print my_garden
    print_list(my_garden)
