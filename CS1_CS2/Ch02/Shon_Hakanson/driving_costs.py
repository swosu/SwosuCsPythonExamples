miles_per_gallon = 10
cost_per_gallon = 1
miles = 100

def calculate_total_driving_cost(miles_per_gallon, miles):
    gallons_used = miles / miles_per_gallon
    return gallons_used

gallons_used = calculate_total_driving_cost(miles_per_gallon, miles)
total_cost = gallons_used * cost_per_gallon

print("Total cost of driving:", total_cost)