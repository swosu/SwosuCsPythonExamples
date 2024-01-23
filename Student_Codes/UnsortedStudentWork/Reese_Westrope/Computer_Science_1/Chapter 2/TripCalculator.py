dpg = float(input("Enter your gas prices (in dollars per gallon):"))
mpg = float(input("Enter your vehicle's gas mileage (in miles per gallon):"))

print('Denali, Alaska \nPlaya del Carmen, Mexico \nLos Angeles, California \nDallas, Texas')

destination = input('Choose your destination from the list above:')
if destination == 'Denali, Alaska':
    distance = 3768
elif destination == 'Playa del Carmen, Mexico':
    distance = 2147
elif destination == 'Los Angeles, California':
    distance = 1258
elif destination == 'Dallas, Texas':
    distance = 274
else:
    print("Error Occurred: Please choose a destination from the list above.")

cost = dpg/mpg*distance

def calculate(dpg, mpg):
    print('It will cost you $''{:.2f}'.format(cost),'to travel to',destination,'.')

calculate(dpg,mpg)