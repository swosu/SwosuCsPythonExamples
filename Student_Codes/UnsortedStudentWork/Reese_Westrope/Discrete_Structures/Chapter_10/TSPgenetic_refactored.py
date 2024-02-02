import numpy as np
import time
import multiprocessing as mp

#this is where we load in the csv data
distances = np.loadtxt('500.csv', delimiter=',')

population_size = 50
population = [np.random.permutation(500) for _ in range(population_size)]

num_generations = 60
mutation_rate = 0.03
num_parents = 2

def path_distance(path):
    # Initialize the total distance to zero
    total_distance = 0

    # Calculate the distance between each pair of consecutive cities in the path
    for index in range(len(path) - 1):
        current_city = path[index]
        next_city = path[index + 1]
        distance = distances[current_city, next_city]
        total_distance += distance

    # Add the distance from the last city back to the first city to complete the loop
    first_city = path[0]
    last_city = path[-1]
    distance = distances[last_city, first_city]
    total_distance += distance

    # Return the total distance
    return total_distance

def selection(population, fitness, num_parents):
    # Calculate the probabilities of each individual being selected as a parent
    parent_probabilities = fitness / fitness.sum()

    # Choose the parent indices based on their probabilities
    parent_indices = np.random.choice(len(population), size=num_parents, replace=False, p=parent_probabilities)

    # Retrieve the selected parents from the population
    parents = [population[idx] for idx in parent_indices]

    # Return the selected parents
    return parents

def crossover(parents):
    # Initialize a child with a placeholder value (-1) for each city
    child = [-1] * len(parents[0])

    # Choose two random indices to slice the parents' paths and swap them
    start, end = sorted(np.random.choice(len(child), size=2, replace=False))
    child[start:end] = parents[0][start:end]

    # Fill in the remaining cities in the child's path with the other parent's cities
    for p in parents[1]:
        if p not in child:
            # Find the first empty slot in the child's path and fill it with the parent's city
            for i in range(len(child)):
                if child[i] == -1:
                    child[i] = p
                    break

    # Return the child's path
    return child

def mutation(path, mutation_rate):
    # Randomly decide if mutation should occur based on mutation rate
    if np.random.rand() < mutation_rate:
        # Randomly choose two distinct indices
        index1, index2 = np.random.choice(len(path), 2, replace=False)
        # Swap the values at the chosen indices
        path[index1], path[index2] = path[index2], path[index1]
    # Return the mutated path
    return path

start_time = time.time()

for i in range(num_generations):
    fitness = np.array([1/path_distance(p) for p in population])
    fittest_idx = np.argsort(fitness)[::-1]
    fittest = [population[idx] for idx in fittest_idx[:num_parents]]
    new_population = [crossover(selection(population, fitness, num_parents)) for _ in range(population_size-num_parents)]
    new_population = [mutation(p, mutation_rate) for p in new_population]
    population = fittest + new_population




#argmax returns the maximum, so when you divide one by the path length, the largest result will correspond with the smallest path length
best_path = population[np.argmax([1/path_distance(p) for p in population])]
print("Shortest distance found:", path_distance(best_path))
print("--- %s seconds ---" % (time.time() - start_time))