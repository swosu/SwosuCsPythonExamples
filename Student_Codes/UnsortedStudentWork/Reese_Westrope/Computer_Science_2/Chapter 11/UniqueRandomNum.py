

import random

retries = 0

def unique_random_ints(how_many, max_num, seed):
    global retries
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""
    random.seed(seed)
    num_list = []
    for number in range(0, how_many):
        new_num = random.randint(0, max_num)
        if new_num in num_list:
            retries += 1
        else:
            num_list.append(new_num)

    print("The unique numbers were:")
    for num in num_list:  
        print(num)
    print(f"There were {retries} repeating numbers generated.")


if __name__ == '__main__':
    seed = int(input("Enter a seed.\n:"))
    how_many = int(input("How many numbers do you want to generate?\n:"))
    max_num = int(input("What is the max number that should be generated?\n:"))


    unique_random_ints(how_many, max_num, seed)
    