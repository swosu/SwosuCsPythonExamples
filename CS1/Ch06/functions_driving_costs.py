"""
6.19 LAB: Driving costs - functions
Visible to students
editEdit labLinks to an external site.noteNote
Write a function driving_cost()
with input parameters
miles_per_gallon,
dollars_per_gallon, and
miles_driven,

that returns the dollar cost to drive those miles.

All items are of type float.
The function called with arguments (20.0, 3.1599, 50.0)
returns 7.89975.

Define that function in a program whose inputs are
the car's miles per gallon and the price of gas in
dollars per gallon (both float).
Output the gas cost for 10 miles, 50 miles, and 400 miles,
by calling your driving_cost() function three times.

Output each floating-point value with two digits after the decimal point,
which can be achieved as follows:
print(f'{your_value:.2f}')

Ex: If the input is:

20.0
3.1599
the output is:

1.58
7.90
63.20
Your program must define and call a function:

"""


def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    print(f'your car mpg is: {car_mpg}.')
    print(f'gas is up to: {gas_dollars_per_gallon}.')
    print(f'you are going to drive {trip_miles_driven}.')

    gallons_used = trip_miles_driven / car_mpg
    print(f'gallons used: {gallons_used}.')

    trip_cost = gallons_used * dollars_per_gallon
    return trip_cost

if __name__ == '__main__':
    car_mpg = float(input('what is your mpg?'))
    gas_dollars_per_gallon = float(input('how much is gas today?'))
    trip_miles_driven = float(input('how far you going?'))

    #driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    trip_cost = driving_cost(car_mpg, gas_dollars_per_gallon, trip_miles_driven)

    print(f'trip costs: {trip_cost}.')
    #distance_traveled = [10, 50, 500]
