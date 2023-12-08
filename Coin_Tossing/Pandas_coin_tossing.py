
# import our libraries
import pandas as pd
import random
import time
import csv

# make a CSV file to keep track of our batch results
# append to the bottom of the file if it exsits, otherwise create it
summary_of_batch_results_csv = open('summary_of_batch_results.csv', 'a')


# main body of code

# set up a coin toss batch CSV file to write our batch results to
# write over the file if it exsits, otherwise create it
coin_toss_batch_csv = open('coin_toss_batch_results.csv', 'w')

# write the header row to the CSV file
# for each row:
# write the batch number of total batches
# write the number of flips per batch
# write the max consecutive match count goal
# write the max consecutive match count
# write whether or not we have a winner
csv.writer(coin_toss_batch_csv).writerow(['BatchNumber', 'TotalBatches', 'FlipsPerBatch', 'MaxConsecutiveMatchCountGoal', 'MaxConsecutiveMatchCount', 'Winner'])

#random.seed(time.time()) # Seed the random number generator with the current system time (to ensure randomness
random.seed(1) # Seed the random number generator with a fixed number (to ensure reproducibility)

total_number_of_batches = 100  # Replace with the desired number of batches
total_flips = 100  # Replace with the desired number of coin flips

consecutive_match_count_goal = 2
# start timer
start_time = time.time()

for batch_number in range(1, total_number_of_batches + 1):

    consecutive_match_count = 0
    # set up a clean data frame to hold our results
    single_batch_df = pd.DataFrame(columns=['FlipNumber', 'Outcome', 'ConsecutiveMatchCount'])

    for flip_number in range(1, total_flips + 1):
        # Simulate a coin flip (0 for heads, 1 for tails)
        outcome = random.choice(['Heads', 'Tails'])

        # Update consecutive match count
        if flip_number > 1 and outcome == single_batch_df['Outcome'].iloc[-1]:
            consecutive_match_count += 1
        else:
            consecutive_match_count = 1

        #print('for that round, our results to add to the data frame are flip_number: ', flip_number, 'outcome: ', outcome, 'consecutive_match_count: ', consecutive_match_count)
        # Append the results to the DataFrame
        single_batch_df = single_batch_df.append({'FlipNumber': flip_number, 'Outcome': outcome, 'ConsecutiveMatchCount': consecutive_match_count}, ignore_index=True)

    # Print the DataFrame
    #print('for batch number: ', batch_number, 'our results are: ')
    #print(single_batch_df)

    # Print the number of matches
    #print('Max number of matches: ', single_batch_df['ConsecutiveMatchCount'].max())

    # check if our max consecutive match count is greater than or equal to our goal
    this_batch_max_consecutive_match_count = single_batch_df['ConsecutiveMatchCount'].max()
    if this_batch_max_consecutive_match_count >= consecutive_match_count_goal:
        #print('We have a winner!')
        sufficient_consecutive_matches = True
    else:
        #print('No winner this time.')
        sufficient_consecutive_matches = False

    # Write to the CSV file
    # for each row:
    # write the batch number of total batches
    # write the number of flips per batch
    # write the max consecutive match count goal
    # write the max consecutive match count
    # write whether or not we have a winner
    csv.writer(coin_toss_batch_csv).writerow([batch_number, total_number_of_batches, total_flips, consecutive_match_count_goal, this_batch_max_consecutive_match_count, sufficient_consecutive_matches])

# close the CSV file
coin_toss_batch_csv.close()

# read the results from the CSV file into a data frame for results analysis
coin_toss_batch_results_df = pd.read_csv('coin_toss_batch_results.csv')

# Print the DataFrame
#print('our batch results are: ')
#print(coin_toss_batch_results_df)

# for that set of batches, how many winners did we have?
total_winning_batches = coin_toss_batch_results_df['Winner'].sum()
print('for {} batches, we had {} winners'.format(total_number_of_batches, total_winning_batches))
print('flipping a coin {} times per batch, we had a {}% success rate when we were looking for {} consecutive matches'.format(total_flips, (total_winning_batches / total_number_of_batches) * 100, consecutive_match_count_goal))

# stop timer
end_time = time.time()
print('the total seconds to run this simulation was: ', end_time - start_time)
