import csv
import os
import random
import Make_CSV_files as csv_tool

def load_distance_table_from_csv(filename):
    distance_table = []
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            distance_table.append([int(distance) for distance in row])
    return distance_table

def guess_and_check_hamiltonian_path(distance_table):
    n = len(distance_table)
    cities = list(range(n))
    
    
    # Shuffle the cities to create a random order for the guess
    random.shuffle(cities)
    
    # Check for a Hamiltonian path
    for i in range(n):
        if distance_table[cities[i-1]][cities[i]] == 0:
            return None  # Invalid path, retry with a new guess
    
    # Create a closed loop Hamiltonian path
    return cities + [cities[0]]

if __name__ == "__main__":
    # Ask the user for the number of cities
    num_cities = int(input("Enter the number of cities: "))
    
    #Check if the CSV file already exists
    csv_filename = f"distance_table_{num_cities}_cities.csv"
    # Check if the file already exists
    if os.path.exists(csv_filename):
        print(f"File '{csv_filename}' already exists. Not creating a new file.")
         # Load the distance table from CSV
        loaded_distance_table = load_distance_table_from_csv(csv_filename)
        # print("Distance Table:")
        print('loaded gnc distance table:')
        csv_tool.print_distance_table(loaded_distance_table)
    else:
        distance_table = csv_tool.create_distance_table(num_cities)
        with open(csv_filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            for row in distance_table:
                csv_writer.writerow(row)
        print(f"Distance table written to {csv_filename}")

   

    # Guess and check a Hamiltonian path
    hamiltonian_path = guess_and_check_hamiltonian_path(loaded_distance_table)

    if hamiltonian_path:
        print(f"Found Hamiltonian path: {hamiltonian_path}")
    else:
        print("No Hamiltonian path found. Please try again.")
