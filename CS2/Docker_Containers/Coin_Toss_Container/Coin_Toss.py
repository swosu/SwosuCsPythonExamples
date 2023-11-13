import random

coin_toss_total = 1000
heads_in_a_row_limit = 3
coin_tosses = 0
heads = 0
tails = 0
heads_in_a_row = 0
tails_in_a_row = 0
options = ["heads", "tails"]

while coin_tosses < coin_toss_total:
    
    coin_toss = random.choice(options)
    if coin_toss == "heads":
        heads += 1
        heads_in_a_row += 1
        tails_in_a_row = 0
        if heads_in_a_row > heads_in_a_row_limit:
            break
    else:
        tails += 1
        tails_in_a_row += 1
        heads_in_a_row = 0
    coin_tosses += 1
    #print(coin_toss)
print('out of the loop')
print('Total tosses: '  + str(coin_tosses))
print('Heads: ' + str(heads))
print('Tails: ' + str(tails))
print('Heads in a row: ' + str(heads_in_a_row))
print('number of coin tosses to get ' + str(heads_in_a_row) + ' heads in a row: ' + str(coin_tosses))
print('odds of getting ' + str(heads_in_a_row) + ' heads in a row: ' + str(coin_toss_total/coin_tosses))
    