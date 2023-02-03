#take an amount of cash, return the change options.
amount_due =  float(input("Enter amount due: "))
amount_given = float(input("Enter amount recieved: "))
cash = round(amount_given - amount_due,2)

#ai assited code, I defined the dictionary, the ai created the for loop and the if statement.
def change(amount_due):
    # Denominations of coins and bills
    denominations = [
        ("Hundred(s)", 100),
        ("Fifty(s)", 50),
        ("Twenty(s)", 20),
        ("Ten(s)", 10),
        ("Five(s)", 5),
        ("One(s)", 1),
        ("Quarter(s)", 0.25),
        ("Dime(s)", 0.1),
        ("Nickel(s)", 0.05),
        ("Penny(s)", 0.01)
    ]
    change = {}

    for denom_name, denom_value in denominations:
        if amount_due >= denom_value:
            count = int(amount_due / denom_value)
            amount_due -= count * denom_value
            amount_due = round(amount_due, 2) # rounding to 2 decimal places
            change[denom_name] = count
    
    return change
if __name__ == '__main__':
    print(f"\nChange owed: {cash}\nGive customer: {change(cash)}")
  
#Sources: https://www.toppr.com/guides/python-guide/examples/python-examples/functions/number-divisible/python-program-find-numbers-divisible-another-number/
#https://www.youtube.com/watch?v=9-Cpi3hGjrY
#https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/
#https://chat.openai.com/chat