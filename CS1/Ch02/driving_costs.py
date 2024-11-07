"""
Driving is expensive. 
Write a program with a car's miles/gallon and 
gas dollars/gallon (both floats) as input, 
and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, 
which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))

Ex: If the input is:

20.0
3.1599
Then the output is:

3.16 11.85 79.00

"""
print('welcome to our driving cost calculator.')

# https://www.geeksforgeeks.org/taking-input-in-python/
car_miles_per_gallon = float(input('What is your car miles per gallon? ') )
print(f'our car mpg was {car_miles_per_gallon:.2f} miles per gallon.')

dollars_per_gallon = float(input('What is your dollars per gallon? ') )
print(f'fuel cost is ${dollars_per_gallon:.2f} dollars per gallon.')

trip_length = 20
gallos_per_trip = trip_length / car_miles_per_gallon
print(f'a trip {trip_length} miles long in a car that gets\n'\
f'{car_miles_per_gallon:.2f} mpg will use {gallos_per_trip:.2f} gallons of fuel.')

gallos_per_trip = trip_length / car_miles_per_gallon
print(f'a trip {trip_length} miles long in a car that gets\n'\
f'{car_miles_per_gallon:.2f} mpg will use {gallos_per_trip:.2f} gallons of fuel.')