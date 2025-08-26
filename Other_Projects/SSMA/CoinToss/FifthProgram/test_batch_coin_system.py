import batch_coin_toss
import csv
import math
import time

print('start of csv code')
with open('eggs10K.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    #spamwriter = csv.writer(csvfile, delimiter=' ',
    #                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #spamwriter.writerow(['batch size,','percentage,','time in seconds'])
    spamwriter.writerow(['batch size','balanced head count','possible outcomes',
    'possible balanced outcomes','calculated percentage','observed percentage,',
    'percentage error','time in seconds'])

for batch_size in range(2,252,2):
    repeat_count = 10000
    balanced_head_count = batch_size / 2
    possible_outcomes_count = pow(2, batch_size)
    balanced_outcomes_count_part_1 = math.factorial(batch_size)
    balanced_outcomes_count_part_2 = math.factorial(balanced_head_count)
    balanced_outcomes_count_part_3 = math.factorial(batch_size - balanced_head_count)
    balanced_outcomes_count = balanced_outcomes_count_part_1 / (balanced_outcomes_count_part_2 * balanced_outcomes_count_part_3)
    calculated_portion_balanced_sets = balanced_outcomes_count / possible_outcomes_count
    balanced_count = 0


    start_time = time.time()
    for i in range(repeat_count):
        head_count = batch_coin_toss.batch_toss_coins(batch_size)
        if(head_count == balanced_head_count):
            balanced_count = balanced_count + 1

    end_time = time.time()
    elapsed_time = end_time - start_time
    percentage_balanced_sets = balanced_count/repeat_count
    print(f'batch size, {batch_size: d}',
    f' balanced head count {balanced_head_count: 0.0f}'
    f' possible outcomes {possible_outcomes_count: d}'
    f' possible balanced outcomes {balanced_outcomes_count: 0.0f}'
    f' calculated percentage {100*calculated_portion_balanced_sets: 0.2f}%'
    f' percentage {100*percentage_balanced_sets: 0.2f}%'
    f' error percentage {100*(abs(percentage_balanced_sets - calculated_portion_balanced_sets )): 0.2f}%'
    f' time in {elapsed_time: f} seconds.')
    print_data_1 = f'{batch_size: d}'
    print_data_2 = f'{balanced_head_count: 0.0f}'
    print_data_3 = f'{possible_outcomes_count: d}'
    print_data_4 = f'{balanced_outcomes_count: 0.0f}'
    print_data_5 = f'{100*calculated_portion_balanced_sets: 0.2f}%'
    print_data_6 = f'{100*percentage_balanced_sets: 0.2f}%'
    print_data_7 = f'{100*(abs(percentage_balanced_sets - calculated_portion_balanced_sets )): 0.2f}%'
    print_data_8 = f'{elapsed_time: f}'
    with open('eggs10K.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([print_data_1, print_data_2,print_data_3,
        print_data_4,print_data_5,print_data_6,print_data_7,print_data_8])








print('End of the program. Take care!')
