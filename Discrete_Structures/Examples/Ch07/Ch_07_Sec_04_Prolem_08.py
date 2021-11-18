print('hello')
import random
random.seed()
import statistics

"""
# check for a 1:
keep_going = True
while(keep_going):
    single_dice_roll = random.randint(1,6)
    if(6 == single_dice_roll):
        print('you rolled', single_dice_roll)
        keep_going = False
"""

def roll_dice():
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_3 = random.randint(1,6)

    sum = dice_1 + dice_2 + dice_3
    return sum


if __name__ == '__main__':
    sum_array = []
    sample_size = 1000000
    for index in range(sample_size):
        sum = roll_dice()
        #print('your sum was:', sum )
        sum_array.append(int(sum))
    x = statistics.mean(sum_array)
    #print('sum array', sum_array)
    print('average was:', x)
