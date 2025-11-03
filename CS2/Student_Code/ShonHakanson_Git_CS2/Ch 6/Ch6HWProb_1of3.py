#Problem 6.19 in Chapter 6 Comp Sci 2 HW, Shon Hakanson
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    return (miles_driven / miles_per_gallon) * dollars_per_gallon

if __name__ == '__main__':
    miles_per_gallon = float(input("Enter the car's miles per gallon: "))
    dollars_per_gallon = float(input("Enter the price of gas in dollars per gallon: "))

    driving_cost_10 = driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)
    print(f'{driving_cost_10:.2f}')

    driving_cost_50 = driving_cost(miles_per_gallon, dollars_per_gallon, 50.0)
    print(f'{driving_cost_50:.2f}')

    driving_cost_400 = driving_cost(miles_per_gallon, dollars_per_gallon, 400.0)
    print(f'{driving_cost_400:.2f}')
