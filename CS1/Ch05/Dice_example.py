# use a for loop to roll two dice multiple times
# and count the number of times either a total of 6 or 7 are rolled

import random
import time

start_time = time.time()
# set random seed to 15
#random.seed(15)
random.seed(time.time())

total_rolls = 10_000_000
winning_total = 0

for roll_index in range(total_rolls):

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    if total == 6 or total == 7:
        winning_total += 1
    
    #print(f"Roll {roll_index + 1}: {die1} + {die2} = {total}, winning_total = {winning_total}")  

#calculate odds of rolling a 6 or 7
odds = float(winning_total) / float(total_rolls)
stop_time = time.time()
print(f"Odds of rolling a 6 or 7: {odds} for {total_rolls} rolls and took {stop_time - start_time} seconds")