import itertools
import random

def generate_random_distance():
    # Generate a random distance between 1 and 10 times the number of cities
    return random.uniform(1, 10)

def generate_distance_table(cities):
    n = len(cities)
    distance_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            distance = generate_random_distance()
            distance_table[i][j] = distance
            distance_table[j][i] = generate_random_distance()  # Generate a different distance for the reverse direction

    return distance_table

# Rest of the code remains the same...
import itertools
import random

def generate_random_distance():
    # Generate a random distance between 1 and 10 times the number of cities
    return random.uniform(1, 10)

def generate_distance_table(cities):
    n = len(cities)
    distance_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            distance = generate_random_distance()
            distance_table[i][j] = distance
            distance_table[j][i] = generate_random_distance()  # Generate a different distance for the reverse direction

    return distance_table

# Rest of the code remains the same...
