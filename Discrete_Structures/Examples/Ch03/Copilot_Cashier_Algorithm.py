import random
import time

import math

# I want to reset the random number generator seed to a fixed value
random.seed(0)

# I want the random number generator seed to be set to the current time
#random.seed(time.time())

#I want to work the cashier algorithm in python



number_of_retuned_items_greedy = 0
number_of_retuned_items_guess_and_check = 0

def calculate_customer_total():
    customer_dollar_total = random.randint(0, 6)
    customer_cents_total = random.randint(0, 99)

    customer_total = customer_dollar_total + (customer_cents_total / 100)

    return customer_total

def tell_customer_what_the_total_was(customer_total):
    print("Your total is: $", customer_total)

def figure_out_how_much_the_customer_gave_you(customer_total):
    
    minimum_dollars = int(customer_total) + 1
    customer_payment = random.randint(minimum_dollars, 10)
    customer_payment_cents = random.randint(0, 99)
    customer_payment = customer_payment + (customer_payment_cents / 100)

    return customer_payment


def tell_customer_what_we_think_they_gave_us(customer_payment):
    print("You gave me: $", customer_payment)

def calculate_change_due(customer_total, customer_payment):
    change_due_to_customer = customer_payment - customer_total

    #round this up to the nearest penny
    change_due_to_customer = math.ceil(change_due_to_customer * 100) / 100

    return change_due_to_customer

def tell_customer_what_their_change_is(change_due_to_customer):
    #tell customer what the dollars and cents they are due back is
    print(f"Your change is: $ {change_due_to_customer:.2f}")

def gather_change_greedy(change_due_to_customer, currency_list):
    list_of_currency_to_return = []
    for currency in currency_list:
        while change_due_to_customer >= currency:
            list_of_currency_to_return.append(currency)
            change_due_to_customer -= currency
    check_total = 0
    for currency in list_of_currency_to_return:
        check_total += currency
    if check_total != change_due_to_customer:
        list_of_currency_to_return.append(0.01)
    return list_of_currency_to_return

def gather_change_guess_and_check(change_due_to_customer, currency_list):
    list_of_currency_to_return = []
    remaining_change = change_due_to_customer
    while remaining_change > 0.01:
        currency = random.choice(currency_list)
        if currency <= remaining_change:
            list_of_currency_to_return.append(currency)
            remaining_change -= currency
    return list_of_currency_to_return

def count_change_back_to_customer(customer_total, list_of_currency_to_return):
    print("Here is your change: ")
    print("your total was: {customer_total}")
    for currency in list_of_currency_to_return:
        print(currency)

if __name__ == '__main__':

    customer_total = calculate_customer_total()

    tell_customer_what_the_total_was(customer_total)

    customer_payment = figure_out_how_much_the_customer_gave_you(customer_total)

    tell_customer_what_we_think_they_gave_us(customer_payment)

    change_due_to_customer = calculate_change_due(customer_total, customer_payment) 

    tell_customer_what_their_change_is(change_due_to_customer)

    currency_list = [100, 50, 20, 10, 5, 2, 1, .5, .25, .10, 0.05, 0.01]

    list_of_currency_to_return_greedy = gather_change_greedy(change_due_to_customer, currency_list)

    print('do this again for the greedy method')
    count_change_back_to_customer(customer_total, list_of_currency_to_return_greedy)

    list_of_currency_to_return_guess_and_check = gather_change_guess_and_check(change_due_to_customer, currency_list)

    print('do this again for the guess and check method')
    count_change_back_to_customer(customer_total, list_of_currency_to_return_guess_and_check)

    print(f"Greedy method returned {len(list_of_currency_to_return_greedy)} items")
    print(f"Guess and check method returned {len(list_of_currency_to_return_guess_and_check)} items")

