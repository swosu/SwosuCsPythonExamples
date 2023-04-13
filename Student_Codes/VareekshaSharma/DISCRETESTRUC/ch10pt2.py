'''Find the shortest path a traveling salesperson can take 
to visit each of the 500 cities, visiting each city only 
once and stopping back at the city you began with in less 
than 30 seconds. Measure your own run time.'''

import numpy as np
import pandas as pd
import random
import math

# Read the distances from the file
df = pd.read_excel('cities.xlsx', index_col=0)

# Create the distance matrix
num_cities = len(df)
distance_matrix = np.zeros((num_cities, num_cities))
for row in range(num_cities):
    for col in range(num_cities):
        distance_matrix[row, col] = df.iloc[row, col]

# Define a function to calculate the total distance of a path
def calculate_distance(path):
    distance = 0
    for city_idx in range(len(path)-1):
        current_city = path[city_idx]
        next_city = path[city_idx+1]
        distance += distance_matrix[current_city][next_city]
    distance += distance_matrix[path[-1]][path[0]]
    return distance

# Define the initial temperature and cooling rate
initial_temperature = 1000
cooling_rate = 0.003

# Define the current and best path
current_path = list(range(num_cities))
best_path = current_path

# Define the current and best distance
current_distance = calculate_distance(current_path)
best_distance = current_distance

# Iterate until the temperature has cooled to 1
while initial_temperature > 1:
    # Create a new path by swapping two random cities
    new_path = current_path.copy()
    city_a, city_b = random.sample(range(num_cities), 2)
    new_path[city_a], new_path[city_b] = new_path[city_b], new_path[city_a]
    
    # Calculate the new distance
    new_distance = calculate_distance(new_path)
    
    # If the new distance is better, accept the new path
    if new_distance < current_distance:
        current_path = new_path
        current_distance = new_distance
        
        # If the new distance is better than the best distance, update the best path
        if new_distance < best_distance:
            best_path = new_path
            best_distance = new_distance
    # If the new distance is worse, accept the new path with a probability based on the temperature
    else:
        delta = new_distance - current_distance
        acceptance_probability = math.exp(-delta / initial_temperature)
        if random.uniform(0, 1) < acceptance_probability:
            current_path = new_path
            current_distance = new_distance
    
    # Cool the temperature
    initial_temperature *= 1 - cooling_rate

# Print the best path and distance
print("The shortest path is:", best_path)
print("The shortest distance is:", best_distance)
