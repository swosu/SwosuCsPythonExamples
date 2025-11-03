"""
#1) 2.13 LAB: Driving costs

Driving is expensive.
Write a program with a car's miles/gallon and gas dollars/gallon
(both floats) as input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))

Ex: If the input is:

20.0
3.1599
Then the output is:

3.16 11.85 79.00
"""

miles_per_gallon = float(input("How many MPGs that baby get???"))

print(f"NO WAY!! That thing gets {miles_per_gallon} MPGs?")

dollars_per_gallon = float(input("What is gas up to these days??"))

print(f"Figures. ${dollars_per_gallon} that is more than I make an hour...")

twenty_mile_road_trip_cost = ( 20.0 / miles_per_gallon ) * dollars_per_gallon

print('For a 20 mile road trip, the cost is ${:.2f}'\
.format(twenty_mile_road_trip_cost))
