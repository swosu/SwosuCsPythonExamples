"""
Write a program with total change amount as an integer
input, and output the change using the fewest coins,
one coin type per line.
The coin types are Dollars, Quarters, Dimes, Nickels,
and Pennies.

Bouns: Use singular and plural coin names as appropriate,
like 1 Penny vs. 2 Pennies.
"""

cents_due = 0
customer_paid_cents = 6
change_back = customer_paid_cents - cents_due

if 5 <= change_back:
    print('we might use a nickel.')
    print("1 Nickel")
    change_back = change_back - 5

if 0 == change_back:
    print('No change')

elif 1 == change_back:
    print('1 Penny')

elif 2 == change_back:
    print('2 Pennies')
