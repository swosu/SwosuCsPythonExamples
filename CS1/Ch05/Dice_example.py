# use a for loop to roll two dice multiple times
# and count the number of times either a total of 6 or 7 are rolled

import random

# set random seed to 15
random.seed(15)

total_rolls = 100000000
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
print(f"Odds of rolling a 6 or 7: {odds}")