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

# TODO:  Define the print_list() function that prints a list of plant (or flower) 
# objects 
    def print_list(plant_list):
        for plant in plant_list:
            plant.print_info()


if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []


    user_string = input()
    
    while user_string != '-1':
        # TODO: Check if input is a plant or flower
        #       If plant, create a plant object and add to my_garden
        #       If flower, create a flower object and add to my_garden
        #       If neither, print "Invalid input"
        #       If valid input, print "Plant added to my garden"
        #       If invalid input, print "Invalid input"
        #       If input is -1, exit the loop
        if user_string == 'plant':
            plant_name = input()
            plant_cost = input()
            plant = Plant(plant_name, plant_cost)
            my_garden.append(plant)
            print("Plant added to my garden")
        elif user_string == 'flower':
            plant_name = input()
            plant_cost = input()
            is_annual = input()
            color_of_flowers = input()
            flower = Flower(plant_name, plant_cost, is_annual, color_of_flowers)
            my_garden.append(flower)
            print("Plant added to my garden")
        elif user_string == '-1':
            break
        else:
            print("Invalid input")

        #       Split the user_string input into variables - plant_name, plant_cost, color_of_flowers, is_annual
        #       Create a plant or flower object based on the input
        #       Add the object to the my_garden list
        #       Print "Plant added to my garden"




        
        user_string = input()

    # TODO: Call the print_list() function to print my_garden
    Flower.print_list(my_garden)
    