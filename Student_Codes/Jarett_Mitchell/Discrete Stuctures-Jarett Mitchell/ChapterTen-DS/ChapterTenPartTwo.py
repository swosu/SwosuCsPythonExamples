import pandas as pd
import time

# read in the distance matrix from the CSV file
data = pd.read_csv('C:\\Users\\pixel\\git\\SwosuCsPythonExamples\\Discrete_Structures\\Exams\\Ch_10\\500.csv', header=None)

# define a function to find the nearest neighbor of a given city
def nearest_neighbor(city, visited):
    min_distance = float('inf')
    nearest_city = None
    for i in range(len(data)):
        if i not in visited and data.iloc[city, i] < min_distance:
            min_distance = data.iloc[city, i]
            nearest_city = i
    return nearest_city, min_distance

# initialize variables
visited = set()
path = [0]
total_distance = 0

# start the timer
start_time = time.time()

# iterate over all cities and find the nearest neighbor
for i in range(len(data)-1):
    city, distance = nearest_neighbor(path[-1], visited)
    path.append(city)
    visited.add(city)
    total_distance += distance

# add the distance from the last city back to the starting city
total_distance += data.iloc[path[-1], 0]

# stop the timer and print the results
end_time = time.time()
print("Shortest path:", path)
print("Total distance:", total_distance)
print("Runtime:", end_time - start_time, "seconds")
