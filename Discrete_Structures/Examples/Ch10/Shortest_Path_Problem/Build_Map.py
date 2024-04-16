import random
import os
import csv

def print_map(map):
    # print off the map in such a way that the top row is marked to and shows the city we are
    # traveling to and the left column is marked from and shows the city we are traveling from
    # the rest of the map should show the distance between the two cities

    # i want the cities to start counting at 1, not zero.

    #print the top row
    print("to", end="\t")
    for i in range(len(map)):
        print(i + 1, end="\t")
    print()

    #print the rest of the map
    for row in range(len(map)):
        print(row + 1, end="\t")
        for col in range(len(map)):
            print(map[row][col], end="\t")
        print()
        

def build_map(city_count):
    #build a 2d table that represents the map
    # the map should take in a from city and a too city and return the distance between them

    #initialize the map with random distances and label which index is for the row
    # and which for the columnap[path[from_city_index] - 1][path[to_city_index] - 1]
    map = [[0 for x in range(city_count)] for y in range(city_count)]

    # populate the map with random distances that range from 1 to 10 * the city count
    distance_range_between_cities = 20
    for rows in range(city_count):
        for cols in range(city_count):
            map[rows][cols] = random.randint(1, distance_range_between_cities)
    return map
    
def get_distance(path, map):
    # calculate the distance of the path given the map
    # note that the cities I am giving have an offset of one from the map that I built. 
    # Cities come from dice. 
    # The map is zero indexed.

    print(f'the path is {path} and has the data type of {type(path)}')

    distance = 0
    print(f'our first from city should be: {path[0]}')
    print(f'our first to city should be: {path[1]}')
    for from_city_index in range(len(path) - 1):
        to_city_index = from_city_index + 1
        print(f"from_city_index: {from_city_index}, to_city_index: {to_city_index}")
        print(f'our map data at that point')
        next_step = map[path[from_city_index] - 1][path[to_city_index] - 1]
        #print("from", path[from_city_index], "to", path[to_city_index], "has a step distance", next_step)
        distance += int(next_step)
        #print(f"Distance is {distance} at this point.")

    # close the hamilton path and get us back home.
    last_city_index = -1
    first_city_index = 0
    distance += map[path[last_city_index] - 1][path[first_city_index] - 1]
    return distance


    
def check_if_map_exists(city_count):
    print('looking if the map is saved.')
    file_name = f"distance_table_city_count_{city_count}.csv"
    if os.path.exists(file_name):
        print("file exists")

        # read the file and return the map
        map = []
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                map.append(row)

        #print_map(map)
        return map
    else:
        # if the file does not exist, build a new map and return the map
        print("file does not exist")
        map = build_map(city_count)
        #print_map(map)

        # write the map to a csv file with the appropriate file name
        # Writing to CSV file using for loops
        csv_file = f"distance_table_city_count_{city_count}.csv"
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in map:
                writer.writerow(row)

        print("CSV file created successfully.")

        #close the file
        file.close()

        return map
        
            
    



if __name__ == "__main__":
    
    city_count = 8
    map = build_map(city_count)
    #print_map(map)

    path = [8, 2, 5, 4, 6, 1, 7, 3]

    distance = get_distance(path, map)
    print(f"the path: {path} has a distance of {distance}.")

    print('checking for a map file.')

    map = check_if_map_exists(city_count)
    print('map should be done now.')

    print_map(map)