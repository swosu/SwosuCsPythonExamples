

import random
import time

def coin_toss():
    our_random_number = random.uniform(0, 1)

    if our_random_number < 0.5:
        return 'heads'
    else:
        return 'tails'

def test_if_coin_tossing_is_fair():
    heads = True

    number_of_tosses = 1000000
    head_count = 0
    tail_count = 0
    for toss_index in range(number_of_tosses):
        if coin_toss() == 'heads':
            heads = False
            tail_count += 1
        else:
            heads = True
            head_count += 1

    
    print('out of {} tosses, there were {} heads and {} tails'.format(number_of_tosses, head_count, tail_count))
    print('The probability of heads was {}%'.format(head_count / number_of_tosses * 100))
    print('The probability of tails was {}%'.format(tail_count / number_of_tosses * 100))
    print('Thanks for playing.')

if __name__ == '__main__':
    print('Welcome to the coin tossing game.')

    # set the random seed to the current time
    #random.seed(time.time())
    random.seed(42)
    test_if_coin_tossing_is_fair()

    # lets flip 2 coins at a time and keep track of how many sets have 2 of the same kind in a row.

    number_of_sets = 1000000
    number_of_coins = 2
    number_of_same_kind = 0
    for set_index in range(number_of_sets):
        coin_1 = coin_toss()
        coin_2 = coin_toss()
        if coin_1 == coin_2:
            number_of_same_kind += 1
        #print('set {} was {} and {}'.format(set_index, coin_1, coin_2))

    print('out of {} sets, {} had the same kind of coin'.format(number_of_sets, number_of_same_kind))
    print('The probability of getting the same kind of coin was {}%'.format(number_of_same_kind / number_of_sets * 100))