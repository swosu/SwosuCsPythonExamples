import csv
import itertools
import math
from multiprocessing import Pool

# Load the CSV file
with open('C:\\Users\\pixel\\git\\SwosuCsPythonExamples\\Discrete_Structures\\Exams\\Ch_10\\500.csv', 'r') as f:
    reader = csv.reader(f)
    distances = [[int(val) for val in row] for row in reader]

n = len(distances)

# Calculate the distance between two cities
def distance(city1, city2):
    return distances[city1][city2]

# Calculate the total distance of a path
def path_distance(path):
    return sum(distance(path[i], path[i + 1]) for i in range(n - 1)) + distance(path[-1], path[0])

# Calculate the optimal path using dynamic programming
def tsp(mask, pos, memo={}):
    if (mask, pos) in memo:
        return memo[(mask, pos)]

    # Base case: when all cities have been visited
    if mask == (1 << n) - 1:
        return distance(pos, 0)

    ans = math.inf
    for city in range(n):
        # Check if the city has already been visited
        if mask & (1 << city):
            continue

        new_mask = mask | (1 << city)
        new_pos = city
        new_dist = distance(pos, city) + tsp(new_mask, new_pos, memo)

        ans = min(ans, new_dist)

    memo[(mask, pos)] = ans
    return ans

# Run TSP for each starting city
def run_tsp(args):
    mask, pos = args
    return tsp(mask, pos)

# Use multiprocessing to run TSP for each starting city in parallel
if __name__ == '__main__':
    pool = Pool()
    results = pool.map(run_tsp, [(1 << i, i) for i in range(n)])
    pool.close()
    pool.join()

    # Get the minimum distance path
    min_path = min(enumerate(results), key=lambda x: x[1])[0]

    # Print the results
    print(f'Minimum distance: {results[min_path]}')
    print(f'Path: {list(itertools.islice(itertools.permutations(range(n)), min_path, min_path+1))[0]}')
