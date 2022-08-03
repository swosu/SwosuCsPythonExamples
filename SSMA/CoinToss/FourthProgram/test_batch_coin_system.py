import batch_coin_toss
import time

for batch_size in range(2,14,2):
    repeat_count = 1000000
    balanced_head_count = batch_size / 2
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
    f' percentage {100*percentage_balanced_sets: 0.2f}%'
    f' time in {elapsed_time: f} seconds.')



print('End of the program. Take care!')
