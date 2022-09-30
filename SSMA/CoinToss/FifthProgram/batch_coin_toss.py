import single_coin_toss

def batch_toss_coins(batch_size):
    heads_count = 0
    for i in range(batch_size):
        heads = single_coin_toss.toss_coin()
        if heads:
            heads_count = heads_count + 1

    return heads_count