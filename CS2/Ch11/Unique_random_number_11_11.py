import random

def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""
    
    global retries                        # A global statement is needed here because
    retries = 0                           # the value of retries is used in main

    nums = list()

    while len(nums) < how_many:
        next_rand = random.randint(0, 2
        )
        if next_rand not in nums:
            nums.append(next_rand)
        else:
            retries += 1

    return nums

if __name__ == '__main__':
    seed = int(input('What seed do you want to use?'))
    how_many = int(input('How many random numbers do you want?'))
    max_num = int(input('What is the maximum number allowed?'))

    random.seed(seed)

    random_nums = unique_random_ints(how_many, max_num)
    random_num_strings = [str(num) for num in random_nums]

    # The value of retries is assigned in unique_random_ints
    print(f'{" ".join(random_num_strings)} retries={retries}')
