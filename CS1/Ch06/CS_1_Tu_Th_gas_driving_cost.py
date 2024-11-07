def say_hello():
    print('hello')

def ask_user_for_car_miles_per_gallon():
    car_mpg = float(input('please input the car miles per gallon and press enter: '))
    return car_mpg

def ask_user_the_cost_per_gallon_of_gas():
    print('please input the cost of gas in dollars ')
    money_per_gallon = float(input('per gallon and then press enter: '))
    return money_per_gallon

def ask_user_how_far_they_want_to_go_in_miles():
    return float(input('please input how many miles you want to drive then press enter: '))

def calculate_total_gallons_used(miles_driven, vehicle_mpg):
    total_gallons_used = miles_driven / vehicle_mpg
    return total_gallons_used

def calculate_total_gas_cost(total_gallons_used, dollars_per_gallon):
    total_gas_cost = total_gallons_used * dollars_per_gallon
    return total_gas_cost

def print_off_driving_cost_results(mpg, dol_per_gal, distance,
                                   gallons, total_for_gas):
    print('Driving ', distance, ' miles in a car that gets ', mpg, ' miles per gallon')
    print('Will use ', gallons, ' gallons of gas.')
    print('If gas is $', dol_per_gal, " per gallon,")
    print('The trip should cost, $', total_for_gas,'.')

if __name__ == '__main__':

    vehicle_mpg = ask_user_for_car_miles_per_gallon()

    dollars_per_gallon = ask_user_the_cost_per_gallon_of_gas()

    miles_driven = ask_user_how_far_they_want_to_go_in_miles()

    total_gallons_used = calculate_total_gallons_used(miles_driven, vehicle_mpg)

    total_gas_cost = calculate_total_gas_cost(total_gallons_used, dollars_per_gallon)

    print_off_driving_cost_results(vehicle_mpg, dollars_per_gallon, miles_driven,
                                   total_gallons_used, total_gas_cost)