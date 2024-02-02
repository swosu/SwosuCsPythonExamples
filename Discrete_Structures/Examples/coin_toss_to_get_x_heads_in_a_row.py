import random
import csv
# I would like to answer this question.
''' If I want to get x heads in a row, how many times do I need to toss a coin? '''

# create a dictionary to keep track of the number of coin tosses it took to get x heads in a row.
results = {}

for i in range(1, 101):
    print(f'you want to have {i} heads in a row')
    heads_in_a_row = 0
    toss_count = 0
    while True:
        toss_count += 1
        heads = random.randint(0, 1)
        if heads == 1:
            heads_in_a_row += 1
        else:
            heads_in_a_row = 0
        
        if heads_in_a_row == i:
            print(f'heads_in_a_row = {heads_in_a_row}, toss_count = {toss_count}')
            break
    results[i] = toss_count
    toss_count = 0
    heads_in_a_row = 0
    #print('reset and ready for the next round')
    
# save the results to a file called coin_toss_results_x_heads_in_a_row.csv

# open the file
f = open('coin_toss_results_x_heads_in_a_row.csv', 'w')

# create a csv writer object
writer = csv.writer(f)
for key, value in results.items():
    writer.writerow([key, value])

# close the file
f.close()

# email the file to myself
