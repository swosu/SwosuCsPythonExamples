import random

def generate_distance_table(n):
    distance_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            # Generating random distances between 1 and 10*n
            distance = random.randint(1, 10 * n)
            
            # Assigning the same distance for both directions since it's an undirected graph
            distance_table[i][j] = distance
            distance_table[j][i] = distance

    return distance_table

def print_distance_table(distance_table):
    n = len(distance_table)
    
    # Printing the distance table
    for i in range(n):
        for j in range(n):
            print(f"{distance_table[i][j]:4}", end=" ")
        print()

if __name__ == "__main__":

    # Example: Generate a distance table for 5 cities
    n_cities = 5
    distance_table = generate_distance_table(n_cities)

    # Print the generated distance table
    print("Distance Table:")
    print_distance_table(distance_table)
