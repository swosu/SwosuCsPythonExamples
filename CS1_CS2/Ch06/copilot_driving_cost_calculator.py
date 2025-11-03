import random 

def what_is_the_cost_of_gas():
    #gas_price = input('What is the cost of gas? ')
    gas_price = 5.00
    gas_price = float(gas_price)
    return gas_price

def how_far_do_we_have_to_go():
    #distance = input('How far do we have to go? ')
    distance = 100
    distance = float(distance)
    return distance

def how_many_miles_per_gallon():
    #miles_per_gallon = input('How many miles per gallon? ')
    miles_per_gallon = 10
    miles_per_gallon = float(miles_per_gallon)
    return miles_per_gallon

def how_many_gallons_needed(distance, miles_per_gallon):
    gallons_needed = distance / miles_per_gallon
    return gallons_needed

def how_much_will_the_trip_cost(gas_price, gallons_needed):
    cost_of_trip = gas_price * gallons_needed
    return cost_of_trip

if __name__ == '__main__':
    gas_price = what_is_the_cost_of_gas()
    print(f'Gas price is: ${gas_price} per gallon.')

    distance = how_far_do_we_have_to_go()
    print(f'Distance is: {distance} miles.')

    miles_per_gallon = how_many_miles_per_gallon()
    print(f'Miles per gallon is: {miles_per_gallon}')

    gallons_needed = how_many_gallons_needed(distance, miles_per_gallon)
    print(f'Gallons needed is: {gallons_needed}')

    cost_of_trip = how_much_will_the_trip_cost(gas_price, gallons_needed)
    print(f'Cost of trip is: {cost_of_trip}')
