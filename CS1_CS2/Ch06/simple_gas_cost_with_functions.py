#shaewashere


def ask_user_cost_per_gallon():
    print('how much does a gallon of gas cost?')
    cost_per_gallon = float(input(' enter your answer in dollars and cents and then press enter: '))
    return cost_per_gallon

def ask_user_vehicle_miles_per_gallon():
    #print('how many miles per gallon do you get with that hog?')
    miles_per_gallon = 20
    return miles_per_gallon

def ask_user_distance_in_miles():
    distance_driven = 100
    return distance_driven

def calculate_gallons_of_gas(miles, mpg):
    gallons = miles / mpg
    return gallons

def calculate_cost_for_the_trip(gallons_of_gas, cost_per_gallon):
    gas_cost = gallons_of_gas * cost_per_gallon
    return gas_cost

def now_print_results(cost_for_the_trip, miles_driven, vehicle_miles_per_gallon, cost_per_gallon):
    print('The trip cost $', cost_for_the_trip, ' for ', 
          miles_driven, ' miles at ', vehicle_miles_per_gallon, 
          ' miles per gallon and a cost of ', cost_per_gallon, ' per gallon')
if __name__ == "__main__":

    # How much does gas cost?

    cost_per_gallon = ask_user_cost_per_gallon()
    #print('a gallon of gas costs: ', cost_per_gallon)

    # What kind of gas mileage do you get?
    vehicle_miles_per_gallon = ask_user_vehicle_miles_per_gallon()
    #print('vehicle miles per gallon', vehicle_miles_per_gallon)

    # how far are you going to go?
    miles_driven = ask_user_distance_in_miles()
    #print('the trip distance in miles is: ', miles_driven)

    # How many gallons of gas is that?
    gallons_of_gas = calculate_gallons_of_gas(miles_driven, vehicle_miles_per_gallon)
    #print('that trip will take: ', gallons_of_gas, ' gallons of gas')

    # how much is that going to cost?
    cost_for_the_trip = calculate_cost_for_the_trip(gallons_of_gas, cost_per_gallon)
    #print('the calculated cost was: ', cost_for_the_trip)

    # print the results
    now_print_results(cost_for_the_trip, miles_driven, vehicle_miles_per_gallon, cost_per_gallon)