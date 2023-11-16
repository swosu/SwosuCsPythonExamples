import random
import csv

def generate_directed_distance_table(n):
    distance_table = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j:
                distance = random.randint(1, 10 * n)
                distance_table[i][j] = distance

    return distance_table

def write_distance_table_to_csv(distance_table, filename):
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in distance_table:
            csv_writer.writerow(row)

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

    # Specify the filename for the CSV file
    csv_filename = "distance_table.csv"

    # Write the distance table to a CSV file
    write_distance_table_to_csv(directed_distance_table, csv_filename)

    print(f"\nDistance table written to {csv_filename}")
