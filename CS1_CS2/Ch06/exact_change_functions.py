import random
import time

def exact_change(change_amount):
    if change_amount <= 0:
        return "no change"
    
    coins = {
        "fifties": 5000,
        "twenties": 2000,
        "five dollar bills": 500,
        "dollar bills": 100,
        "half dollars": 50,
        "quarters": 25,
        "dimes": 10,
        "nickels": 5,
        "pennies": 1
    }
    
    change = []
    
    for coin_name, coin_value in coins.items():
        if change_amount >= coin_value:
            num_coins = change_amount // coin_value
            change_amount -= num_coins * coin_value
            if num_coins > 1:
                coin_name += "s"
            change.append(f"{num_coins} {coin_name}")
    
    return change

def generate_random_bill_total():
    dollars = random.randint(0, 100)
    #print('our random dollar amount is: ', dollars)
    cents = random.randint(0, 99)
    #print('our random cents amount is: ', cents)
    return dollars * 100 + cents

def generate_random_sufficient_payment(total_amount):
    payment_dollars = total_amount + 10 * random.randint(0, 10)
    print('our random dollar amount is: ', payment_dollars)
    payment_cents = random.randint(0, 99)
    print('our random cents amount is: ', payment_cents)
    payment_total = payment_dollars * 100 + payment_cents
    print('our total payment is: ', payment_total)
    return payment_total

def count_back_change(total_bill, amount_paid):
    # calculate change
    # make sure to convert to int to avoid floating point errors
    # if there is a single dollar, it should be singular, 
    # but if there are multiple dollars, it should be plural
    change = amount_paid - total_bill
    print(f"Change: ${change / 100:.2f}")
    print("You should receive:")
    for coin in exact_change(change):
        print(coin)



if __name__ == "__main__":
    # set random seed to get the same results every time
    random.seed(42)
    # set random see to get a random result every time
    # random.seed(time.time())
    #print('Welcome to the Change Calculator')
    #print('first we figure out how much we owe')
    #print('this uses the generate_total function')
    total_bill = generate_random_bill_total()
    print(f"Total bill: ${total_bill / 100:.2f}")

    print('now we figure out how much we paid')
    print('this uses the generate_payment function')
    amount_paid = generate_random_sufficient_payment(total_bill)


    count_back_change(total_bill, amount_paid)