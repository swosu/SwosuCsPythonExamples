def get_the_cars_miles_per_gallon():
    miles_per_gallon = input('please enter the car miles per gallon:\n')
    return miles_per_gallon

def get_the_dollars_per_gallon():
    dollars_per_gallon = input('please enter the dollars per gallon:\n')
    return dollars_per_gallon

def calculate_gas_cost(miles_per_gallon, dollars_per_gallon, trip_length):
    gas_cost =(float(trip_length) / float(miles_per_gallon)) * \
        float(dollars_per_gallon)
    return gas_cost

#Driving is expensive.
#Write a program with a car's
#   miles/gallon and
#   gas dollars/gallon (both floats) as input,
#and output the gas cost for
#   10 miles,
#   50 miles, and
#   400 miles.

#Output each floating-point value with two digits after the decimal point,
# which can be achieved as follows:
# print('{:.2f}'.format(your_value))

# Define your function here.

print('get car Miles per Gallon.')
miles_per_gallon = get_the_cars_miles_per_gallon()
print('you entered ', str(miles_per_gallon), ' miles per gallon')

print('get car Dollars per Gallon.')
dollars_per_gallon = get_the_dollars_per_gallon()
print('you entered ', str(dollars_per_gallon), ' dollars per gallon')

trip_length = [10, 50, 400]
index = 0
gas_cost = calculate_gas_cost(miles_per_gallon, dollars_per_gallon, trip_length[index])
print('a trip that is ', trip_length[index], 'miles long will cost ${:.2f}.'.format(gas_cost))


index = 1
gas_cost = calculate_gas_cost(miles_per_gallon, dollars_per_gallon, trip_length[index])
print('a trip that is ', trip_length[index], 'miles long will cost ${:.2f}.'.format(gas_cost))


index = 2
gas_cost = calculate_gas_cost(miles_per_gallon, dollars_per_gallon, trip_length[index])
print('a trip that is ', trip_length[index], 'miles long will cost ${:.2f}.'.format(gas_cost))
