# 2.14 LAB: Driving costs
# Read gas mileage (miles per gallon) and gas cost (dollars per gallon),
# then compute gas cost for driving 20, 75, and 500 miles.

gas_mileage_mpg = float(input("Enter gas mileage (miles per gallon): "))
gas_price_per_gallon = float(input("Enter gas price (dollars per gallon): "))

miles_20 = 20.0
miles_75 = 75.0
miles_500 = 500.0

gallons_for_20_miles = miles_20 / gas_mileage_mpg
gallons_for_75_miles = miles_75 / gas_mileage_mpg
gallons_for_500_miles = miles_500 / gas_mileage_mpg

cost_for_20_miles = gallons_for_20_miles * gas_price_per_gallon
cost_for_75_miles = gallons_for_75_miles * gas_price_per_gallon
cost_for_500_miles = gallons_for_500_miles * gas_price_per_gallon

print(f'{cost_for_20_miles:.2f} {cost_for_75_miles:.2f} {cost_for_500_miles:.2f}')
