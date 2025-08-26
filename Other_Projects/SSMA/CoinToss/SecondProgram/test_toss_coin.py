import tossSingleCoin

heads_count = 0
total_flips = 1000000

for i in range(total_flips):
    heads = tossSingleCoin.toss_coin()
    if heads:
        heads_count = heads_count + 1

percentage_heads = heads_count/total_flips
print('Our heads count was', heads_count, 'out of', total_flips, 'total flips')
print(f'Our coin comes up heads, {percentage_heads: 0.2f}%')
