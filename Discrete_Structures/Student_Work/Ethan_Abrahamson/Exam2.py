import random

# Generate a random total charge between $1 and $10
total_charge = round(random.uniform(1, 10), 2)

# Generate a random payment greater than the total charge
payment = round(total_charge + random.uniform(0.01, 10), 2)

# Calculate the change in pennies
change = int((payment - total_charge) * 100)

# Calculate the number of each denomination to return
twenties = change // 2000
change %= 2000

tens = change // 1000
change %= 1000

fives = change // 500
change %= 500

ones = change // 100
change %= 100

quarters = change // 25
change %= 25

dimes = change // 10
change %= 10

nickels = change // 5
change %= 5

pennies = change

# Count change back using a while loop
print(f"Total Charge: ${total_charge:.2f}")
print(f"Payment: ${payment:.2f}")
print("Now we will try to count change back...")

sub_total = 0
sub_total += total_charge

print(f"The total was: ${total_charge:.2f}")
if pennies:
    sub_total += pennies / 100
    print(f"{pennies} pennies makes: ${sub_total:.2f} ")

if nickels:
    sub_total += nickels / 20
    print(f"{nickels} nickels makes: ${sub_total:.2f} ")

if dimes:
    sub_total += dimes / 10
    print(f"{dimes} dimes makes: ${sub_total:.2f} ")

if quarters:
    sub_total += quarters / 4
    print(f"{quarters} quarters makes: ${sub_total:.2f} ")

if ones:
    sub_total += ones 
    print(f"{ones} ones makes: ${sub_total:.2f} ")

if fives:
    sub_total += fives *5
    print(f"{fives} fives makes: ${sub_total:.2f} ")

if tens:
    sub_total += tens * 10
    print(f"{tens} tens makes: ${sub_total:.2f} ")

if twenties:
    sub_total += twenties * 10
    print(f"{twenties} twenties makes: ${sub_total:.2f} ")


