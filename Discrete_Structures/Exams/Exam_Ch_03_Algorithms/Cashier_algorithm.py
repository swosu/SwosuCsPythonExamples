'''Programming Exam:
Use the cashier's algorithm.
Develop a program that randomly selects
a total charge.

Then randomly select a payment in dollars and cents
that exceeds that charge.

Then have the program calculate the
change in pennies, nickels, dimes,
quarters, ones, fives, and twenties.

Bonus points for anyone who writes a
program that can "Count change back."
'''
import random
print('hello.')

total_charge_dollars = random.randint(1,100)
print(f'the total dollars were: {total_charge_dollars}.')
total_charge_cents = random.randint(1,100)
print(f'the total cents were: {total_charge_cents}.')

print(f'the total charge was ${total_charge_dollars}.{total_charge_cents}.')

total_charge = float(str(total_charge_dollars) + '.' + str(total_charge_cents))
print(f'the total charge was ${total_charge}.')

user_payment = 105
user_payment_formated = "{:.2f}".format(user_payment)
print(f'the user paid in :${user_payment_formated}')

customer_change = user_payment - total_charge
print(f'the customer should get back ${customer_change}.')

working_change_value = customer_change
# Benjermens
if 100 <= working_change_value:
    print('you can give back a hundred dollars.')
    working_change_value = working_change_value -  100
    print(f'you still owe the customer: ${working_change_value}.')

if 50 <= working_change_value:
    print('you can give back a $50')
    working_change_value = working_change_value -  50
    print(f'you still owe the customer: ${working_change_value}.')

if 20 <= working_change_value:
    print('you can give back a $20')
    working_change_value = working_change_value -  20
    print(f'you still owe the customer: ${working_change_value}.')


if 20 <= working_change_value:
    print('you can give back a $20')
    working_change_value = working_change_value -  20
    print(f'you still owe the customer: ${working_change_value}.')


if 10 <= working_change_value:
    print('you can give back a $10')
    working_change_value = working_change_value -  10
    print(f'you still owe the customer: ${working_change_value}.')


if 5 <= working_change_value:
    print('you can give back a $5')
    working_change_value = working_change_value -  5
    print(f'you still owe the customer: ${working_change_value}.')


if 1 <= working_change_value:
    print('you can give back a $1')
    working_change_value = working_change_value -  1
    print(f'you still owe the customer: ${working_change_value}.')

if 1 <= working_change_value:
    print('you can give back a $1')
    working_change_value = working_change_value -  1
    print(f'you still owe the customer: ${working_change_value}.')

if 1 <= working_change_value:
    print('you can give back a $1')
    working_change_value = working_change_value -  1
    print(f'you still owe the customer: ${working_change_value}.')

if 1 <= working_change_value:
    print('you can give back a $1')
    working_change_value = working_change_value -  1
    print(f'you still owe the customer: ${working_change_value}.')

if 0.25 <= working_change_value:
    print('you can give back a quarter')
    working_change_value = working_change_value -  0.25
    print(f'you still owe the customer: ${working_change_value}.')

if 0.25 <= working_change_value:
    print('you can give back a quarter')
    working_change_value = working_change_value -  0.25
    print(f'you still owe the customer: ${working_change_value}.')

if 0.25 <= working_change_value:
    print('you can give back a quarter')
    working_change_value = working_change_value -  0.25
    print(f'you still owe the customer: ${working_change_value}.')

if 0.10 <= working_change_value:
    print('you can give back a dime')
    working_change_value = working_change_value -  0.10
    print(f'you still owe the customer: ${working_change_value}.')

if 0.10 <= working_change_value:
    print('you can give back a dime')
    working_change_value = working_change_value -  0.10
    print(f'you still owe the customer: ${working_change_value}.')

if 0.05 <= working_change_value:
    print('you can give back a nickel')
    working_change_value = working_change_value -  0.05
    print(f'you still owe the customer: ${working_change_value}.')

if 0.01 <= working_change_value:
    print('you can give back a penny')
    working_change_value = working_change_value -  0.01
    print(f'you still owe the customer: ${working_change_value}.')

if 0.01 <= working_change_value:
    print('you can give back a penny')
    working_change_value = working_change_value -  0.01
    print(f'you still owe the customer: ${working_change_value}.')

if 0.01 <= working_change_value:
    print('you can give back a penny')
    working_change_value = working_change_value -  0.01
    print(f'you still owe the customer: ${working_change_value}.')

if 0.01 <= working_change_value:
    print('you can give back a penny')
    working_change_value = working_change_value -  0.01
    print(f'you still owe the customer: ${working_change_value}.')

if 0.01 <= working_change_value:
    print('you can give back a penny')
    working_change_value = working_change_value -  0.01
    print(f'you still owe the customer: ${working_change_value}.')

    
