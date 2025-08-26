# USER INSTRUCTIONS:
# When you run the program, enter your total without the decimal point.
# For example, if you have $1.25, you would enter 125.

def cashier_alg(Total):
    Dollar, Quarter, Dime, Nickel, Penny = 0, 0, 0, 0, 0
    if Total < 0:
        print("Invalid amount of money")
        exit()
    if Total == 0:
        print("No change needed")
        exit()
    while Total > 0:
        if Total >= 100:
            Dollar += 1
            Total -= 100
        elif Total >= 25:
            Quarter += 1
            Total -= 25
        elif Total >= 10:
            Dime += 1
            Total -= 10
        elif Total >= 5:
            Nickel += 1
            Total -= 5
        elif Total >= 1:
            Penny += 1
            Total -= 1
    
    return Dollar, Quarter, Dime, Nickel, Penny


Total = int(input("Enter your total amount of money: "))
Dollar, Quarter, Dime, Nickel, Penny = cashier_alg(Total)
print(f'Dollar: {Dollar}, Quarter: {Quarter}, Dime: {Dime}, Nickel: {Nickel}, Penny: {Penny}')
