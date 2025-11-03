import random

def unique_random_ints(how_many, max_num):
    """Return a list of how_many unique randomly generated numbers from
    0 to max_num (inclusive) using seed to initialize the random module"""

    #Given integer inputs seed, how_many, and max_num, generate a list of how_many unique random integers from 0 to max_num (inclusive).

#Complete function unique_random_ints(how_many, max_num):
#Generate a list of how_many random integers from 0 to max_num (inclusive).
#When a random number exists in the list, a new random number must be generated; use a global variable, retries, to count the number of times an existing number is generated.
#Return the list.
    global retries

    random.seed(seed)
    unique_numbers = []
    retries = 0
    while len(unique_numbers) < how_many:
        num = random.randint(0, max_num)
        if num not in unique_numbers:
            unique_numbers.append(num)
        else:
            retries += 1

    print(*unique_numbers, f"retries = {retries}")
    


if __name__ == '__main__':

#Complete __main__:
#Initialize the random module with the seed value.
#Call unique_random_ints() to get a list of random integers.
#Output the list of random integers and the value of retries, according to the output format shown in the example below.

    seed = int(input())
    how_many = int(input())
    max_num = int(input())

    unique_random_ints(how_many, max_num)
    retries = 0

    # Type your code here. #