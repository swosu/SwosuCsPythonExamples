import random

def unique_random_ints(how_many, max_num):
    #Return a list of how_many unique randomly generated numbers from
    #0 to max_num (inclusive) using seed to initialize the random module
    # Type your code here. #
    list = []
    retries = 0
    while len(list) < how_many:
        num = random.randint(0,max_num) 
        if num not in list:
            list.append(num)
        else:
            retries += 1
    for x in list:
        print(f"{x} ", end = "")
    print("retries=", retries)