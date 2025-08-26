import random
import time

def coin_toss():
    our_random_number = random.uniform(0, 1)

    if our_random_number < 0.5:
        return 'heads'
    else:
        return 'tails'

def test_if_coin_tossing_is_fair():
    number_of_tosses = 1000000
    head_count = 0
    tail_count = 0
    for toss_index in range(number_of_tosses):
        if coin_toss() == 'heads':
            tail_count += 1
        else:
            head_count += 1

    print('out of {} tosses, there were {} heads and {} tails'.format(number_of_tosses, head_count, tail_count))
    #print('The probability of heads was {}%'.format(head_count / number_of_tosses * 100))
    #print('The probability of tails was {}%'.format(tail_count / number_of_tosses * 100))
    #print('Thanks for playing.')

if __name__ == '__main__':
    print('Welcome to the coin tossing game.')

    # set the random seed to the current time
    #random.seed(time.time())
    random.seed(42)
    test_if_coin_tossing_is_fair()

    # lets flip multiple coins at a time and keep track of how many sets have multiples of the same kind in a row.

    # set the run parameters
    number_of_sets = 1_000_000
    number_of_coins = 14
    winning_set_count = 0
    target_number_of_same_kind = 8
    
    #print('looking for {} sets of {} coins in a row'.format(number_of_sets, number_of_coins))
    for set_index in range(number_of_sets):
        coin_toss_results = []
        for position_index in range(number_of_coins):
            coin_toss_results.append(coin_toss())
        #print('for that set, we got {}'.format(coin_toss_results))
        heads_up = coin_toss_results.count('heads')
        tails_up = coin_toss_results.count('tails')
        #print('heads up: {}'.format(heads_up))
        #print('tails up: {}'.format(tails_up))
        
        if heads_up >= target_number_of_same_kind or tails_up >= target_number_of_same_kind:
            winning_set_count += 1
        #print('number of same kind so far: {}'.format(winning_set_count))

    print('out of {} sets, {} had the number of matching heads or tails.'.format(number_of_sets, winning_set_count))
    print('The probability of getting the same kind of coin was {}%'.format(winning_set_count / number_of_sets * 100))