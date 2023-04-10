'''Find the shortest path a traveling salesperson can take 
to visit each of the 500 cities, visiting each city only 
once and stopping back at the city you began with in less 
than 30 seconds. Measure your own run time.'''

import numpy as np
import random
import math
import time
import multiprocessing as mp

# read distance matrix from Google Sheets
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Distances").sheet1
distances = np.array(sheet.get_all_values()[1:], dtype=np.float)

# convert distance matrix to graph
num_cities = distances.shape[0]
graph = [[distances[i][j] for j in range(num_cities)] for i in range(num_cities)]

# helper function to calculate the total distance traveled in a given path through the cities
def calculate_distance(graph, path):
    distance = 0
    for index in range(len(path)):
        current_city = path[index]
        next_city = path[(index + 1) % len(path)]
        distance += graph[current_city][next_city]
    return distance

# helper function to generate a neighbor state by swapping two cities in the current state
def generate_neighbor(current_state):
    neighbor_state = current_state.copy()
    index1, index2 = random.sample(range(len(current_state)), 2)
    neighbor_state[index1], neighbor_state[index2] = neighbor_state[index2], neighbor_state[index1]
    return neighbor_state

# Simulated Annealing algorithm
def simulated_annealing(graph, T_max=10000, T_min=1, cooling_rate=0.99, max_time=30):
    # initialize current state (random path)
    current_state = random.sample(range(num_cities), num_cities)

    # initialize best state
    best_state = current_state
    best_distance = calculate_distance(graph, best_state)

    # initialize temperature
    T = T_max

    # initialize time
    start_time = time.time()

    # run Simulated Annealing algorithm
    while T > T_min and time.time() - start_time < max_time:
        # generate a random neighbor
        neighbor_state = generate_neighbor(current_state)

        # calculate energy difference between current state and neighbor state
        delta_E = calculate_distance(graph, neighbor_state) - calculate_distance(graph, current_state)

        # if neighbor state is better, move to it
        if delta_E < 0:
            current_state = neighbor_state
        # if neighbor state is worse, move to it with a probability of e^(-delta_E/T)
        elif random.random() < math.exp(-delta_E / T):
            current_state = neighbor_state

        # update best state if necessary
        current_distance = calculate_distance(graph, current_state)
        if current_distance < best_distance:
            best_state = current_state
            best_distance = current_distance

        # decrease temperature
        T *= cooling_rate

    return best_state, best_distance

# function to solve the traveling salesman problem using parallelized simulated annealing
def parallel_simulated_annealing(graph, num_processes=4, T_max=10000, T_min=1, cooling_rate=0.99, max_time=30):
    # divide the cities into subsets for each process
    subset_size = int(num_cities / num_processes)
    subsets = [list(range(i*subset_size, (i+1)*subset_size)) for i in range(num_processes)]
    subsets[-1] += list(range(num_processes*subset_size, num_cities))

    # initialize processes
    processes = []
    for subset in subsets:
        process = mp.Process(target=simulated_annealing, args=(graph, T_max, T_min, cooling_rate, max_time, subset))
        process.start()
        processes.append(process)

    # wait for processes to finish
    for process in processes:
        process.join()

    # combine results from each process
    best_state = None
    best_distance = float('inf')
    for process in processes:
        state, distance = process.result()
        if distance < best_distance:
            best_state = state
            best_distance = distance

    return best_state, best_distance

if __name__ == '__main__':
    # read distance matrix from Google Sheets
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    scope = ["https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Distances").sheet1
    distances = np.array(sheet.get_all_values()[1:], dtype=np.float)

    # convert distance matrix to graph
    num_cities = distances.shape[0]
    graph = [[distances[i][j] for j in range(num_cities)] for i in range(num_cities)]

    # solve the problem using parallel simulated annealing
    num_processes = 4
    best_state, best_distance = parallel_simulated_annealing(graph, num_processes=num_processes, T_max=10000, T_min=1, cooling_rate=0.99, max_time=30)

    # print the best state and distance
    print(f"Best state: {best_state}")
    print(f"Best distance: {best_distance}")
