import random
import csv
import os

def generate_directed_distance_table(n):
    distance_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                distance = random.randint(1, 10 * n)
                distance_table[i][j] = distance

    return distance_table

def write_distance_table_to_csv(distance_table, city_count):
    csv_filename = f"distance_table_{city_count}_cities.csv"

    # Check if the file already exists
    if os.path.exists(csv_filename):
        print(f"File '{csv_filename}' already exists. Not creating a new file.")
    else:
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in distance_table:
                csv_writer.writerow(row)
        print(f"Distance table written to {csv_filename}")

    return csv_filename

def print_distance_table(distance_table):
    n = len(distance_table)
    for i in range(n):
        for j in range(n):
            print(f"{distance_table[i][j]:4}", end=" ")
        print()

if __name__ == "__main__":
    n_cities = 5
    directed_distance_table = generate_directed_distance_table(n_cities)

    print("Directed Distance Table:")
    print_distance_table(directed_distance_table)

    # Write the distance table to a CSV file with the city count in the filename
    csv_filename = write_distance_table_to_csv(directed_distance_table, n_cities)

    print(f"\nDistance table written to {csv_filename}")
