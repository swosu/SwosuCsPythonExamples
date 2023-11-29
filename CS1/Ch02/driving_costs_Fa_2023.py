print('hello')

# ask user name
user_name = input('What is your name? ')
print('hello', user_name)

# ask users miles per gallon for their vehicle
miles_per_gallon = int(input('What is your vehicle\'s miles per gallon? '))

if miles_per_gallon < 10:
    print('ouch, that\'s a gas guzzler')
elif miles_per_gallon > 30:
    print('nice, that\'s a fuel efficient car')
else:
    print('that\'s a good car')

# ask user gas price per gallon
gas_price_per_gallon = int(input('What is the price of gas per gallon? '))

if gas_price_per_gallon > 4:
    print("ouch, that\'s expensive gas")

# ask user if they want to go to Walmart, Target in Yukon, or drive to Sante Fe NM

destination = int(input('Where do you want to go? 1 for Walmart, 2 for Target, 3 for Santa Fe NM'))

if destination == 1:
    print('you are going to Walmart')
    disance = 5
elif destination == 2:
    print('you are going to Target')
    distance = 50
elif destination == 3:
    print('you are going to Santa Fe NM')
    distance = 500
else:
    print('you are going to the moon')
    distance = 238900

# calculate cost of trip
cost_of_trip = distance / miles_per_gallon * gas_price_per_gallon

# print cost of trip
print('The cost of your trip is $', cost_of_trip)