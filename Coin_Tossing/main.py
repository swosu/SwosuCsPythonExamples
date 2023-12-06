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

    number_of_sets = 5
    number_of_coins = 2
    number_of_same_kind = 2
    

    for set_index in range(number_of_sets):
        coin_toss_results = []
        for position_index in range(number_of_coins):
            coin_toss_results.append(coin_toss())
        print('for that set, we got {}'.format(coin_toss_results))
        heads_up = coin_toss_results.count('heads')
        tails_up = coin_toss_results.count('tails')
        if heads_up == number_of_coins or tails_up == number_of_coins:
            number_of_same_kind += 1

    print('out of {} sets, {} had the same kind of coin'.format(number_of_sets, number_of_same_kind))
    print('The probability of getting the same kind of coin was {}%'.format(number_of_same_kind / number_of_sets * 100))