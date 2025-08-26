import numpy as np

distances = np.loadtxt('500.csv', delimiter=',')

def path_distance(path):
    distance = sum([distances[path[i], path[i+1]] for i in range(len(path)-1)]) + distances[path[-1], path[0]]
    return distance

population_size = 20
population = [np.random.permutation(500) for _ in range(population_size)]

def selection(population, fitness, num_parents):
    parents_idx = np.random.choice(len(population), num_parents, replace=False, p=fitness/fitness.sum())
    return [population[idx] for idx in parents_idx]

def crossover(parents):
    child = [-1] * len(parents[0])
    start, end = sorted(np.random.choice(len(child), 2, replace=False))
    child[start:end] = parents[0][start:end]
    for p in parents[1]:
        if p not in child:
            for i in range(len(child)):
                if child[i] == -1:
                    child[i] = p
                    break
    return child

def mutation(path, mutation_rate):
    if np.random.rand() < mutation_rate:
        idx1, idx2 = np.random.choice(len(path), 2, replace=False)
        path[idx1], path[idx2] = path[idx2], path[idx1]
    return path

num_generations = 50
mutation_rate = 0.01
num_parents = 2

for i in range(num_generations):
    fitness = np.array([1/path_distance(p) for p in population])
    fittest_idx = np.argsort(fitness)[::-1]
    fittest = [population[idx] for idx in fittest_idx[:num_parents]]
    new_population = [crossover(selection(population, fitness, num_parents)) for _ in range(population_size-num_parents)]
    new_population = [mutation(p, mutation_rate) for p in new_population]
    population = fittest + new_population

best_path = population[np.argmax([1/path_distance(p) for p in population])]
print("Shortest distance found:", path_distance(best_path))

