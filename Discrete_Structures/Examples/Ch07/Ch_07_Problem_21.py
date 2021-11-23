print('hello.')

import random
import time
random.seed(time.time())
fail_count = 0
attempt_max = 50000000
for attempt in range(attempt_max):
    fail = False
    for x in range(6):
        posiblle_results = [1, 2, 3, 4, 5, 6]
        result = random.choice(posiblle_results)
        #print(x, ": Result of dice rolling is : " + str(result))
        if(0 == result % 2 ):
            fail = True
            #print('we had an even. Fail.')

    if(fail):
        #print('There was at least one even.')
        fail_count += 1
    #else:
        #print('!!!!!ALL ODD DICE!!!!')

percent_wins = (1 - fail_count/attempt_max) * 100

print('observed percentage was', percent_wins)
