import random

print('Welcome to the coin flip game!')

# how many times do you need to flip a coin before you get 3 heads in a row?
# write a while loop to simulate flipping a coin until you get 3 heads in a row
# hint: use the random module
import random
import statistics
# repeat the experiment enough times to make the results statistically significant
# hint: use the statistics module to compute the mean and standard deviation
# of your results

# print the mean and standard deviation of your results

times_to_repeat_experiment = 1000

results = []

for i in range(times_to_repeat_experiment):
    flips = 0
    heads_in_a_row = 0
    while heads_in_a_row < 3:
        if random.randint(0, 1) == 0:
            heads_in_a_row += 1
        else:
            heads_in_a_row = 0
        flips += 1
    results.append(flips)

print('Mean:', statistics.mean(results))
print('Standard deviation:', statistics.stdev(results))

print('All done with the coin flip game!')