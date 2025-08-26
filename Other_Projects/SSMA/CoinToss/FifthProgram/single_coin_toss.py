import random

def toss_coin():    # Toss a single coin and see if it comes up heads or tails.
    our_number = random.random()

    if our_number < 0.5 :
        heads = True
    else:
        heads = False
    
    return heads
