import random
import time

def generate_distance_table(city_count):
    distance_table = []
    # initilize distance table
    rows, cols = (city_count, city_count)
    distance_table = [[0 for i in range(cols)] for j in range(rows)]

    # fill distance table with random numbers that range from 1 to 10 * city_count
    for row_index in range(city_count):
        for col_index in range(city_count):
            if row_index == col_index:
                distance_table[row_index][col_index] = 0
            else:
                distance_table[row_index][col_index] = random.randint(1, 10 * city_count)
    return distance_table

def print_distance_table(distance_table):
    # print distance table and pad the numbers so they are all the same length and columns line up correctly
    # print off a header row that lists the to cities with an underscore before and after the city number.
    # print off a initial column that lists the from cities with an underscore before and after the city number.
    # print off the distance between the from city and the to city. 
    print("Distance Table")
    print("   ", end=" ")
    for i in range(city_count):
        print("_" + str(i) + "_", end=" ")
    print()
    for i in range(city_count):
        print("_" + str(i) + "_", end=" ")
        for j in range(city_count):
            print(str(distance_table[i][j]).ljust(3), end=" ")
        print()

def find_total_distance(distance_table, path):
    # calculate the total distance of the path
        total_distance = 0
        for i in range(city_count):
            if i == city_count - 1:
                # connect the last city to the first city
                # print the from city, the to city, and the distance between them
                #print(str(path[i]).ljust(3), end=" ")
                #print(str(path[0]).ljust(3), end=" ")
                increment = distance_table[path[i]][path[0]]
                #print(str(increment).ljust(3), end=" ")
                total_distance += increment
                #print()
            else:
                # print the from city, the to city, and the distance between them
                #print(str(path[i]).ljust(3), end=" ")
                #print(str(path[i + 1]).ljust(3), end=" ")
                increment = distance_table[path[i]][path[i + 1]]
                #print(str(increment).ljust(3), end=" ")
                total_distance += increment
                #print()

        # print the path and total distance
        #print("Total Distance: " + str(total_distance))
        return total_distance

def check_for_better_path(distance_table, path, total_distance, best_distance, best_path):
    #print('not first pass')
    # if the current path is better than the best path, set the best path to the current path
    if total_distance < best_distance:
        best_path = path
        best_distance = total_distance  
        print("New Best Path: ", end="")
        for i in range(city_count):
            print(str(best_path[i]).ljust(3), end=" ")
        print("New Best Distance: " + str(best_distance))
    #else:
        #print("No New Best Path")
        #print("No New Best Distance")
    return best_distance, best_path

def run_guess_and_check_algorithm(distance_table, run_time):
    # start a timer
    start_time = time.time()

    first_pass = True

    while (time.time() - start_time) < run_time:
        # make a list of all possible cities to visit
        cities_to_visit = []
        for i in range(city_count):
            cities_to_visit.append(i)

        # print the list of cities to visit
        #print("Cities to visit: ", end="")
        #for i in range(city_count):
        #    print(str(cities_to_visit[i]).ljust(3), end=" ")
        #print()

        # make a random path that visits all the cities exactly once. Example: [0, 2, 1, 3, 4, 5]
        path = []
        for i in range(city_count):
            path.append(cities_to_visit.pop(random.randint(0, len(cities_to_visit) - 1)))

        # print the path
        #print("Path: ", end="")
        #for i in range(city_count):
        #    print(str(path[i]).ljust(3), end=" ")
        #print()

        total_distance = find_total_distance(distance_table, path)

        # if this is the first pass, set the best path and best distance to the first path and first distance
        if first_pass:
            #print('first pass')
            best_path = path
            best_distance = total_distance
            first_pass = False
        else:
            best_distance, best_path = check_for_better_path(distance_table, path, total_distance, best_distance, best_path)

    # after time has passed, print the best path and best distance
    print('GNC after {0} seconds, the best path is {1} with a distance of {2}'.format(run_time, best_path, best_distance))

def run_brute_force_algorithm(distance_table, run_time):
    import itertools

    # start a timer
    start_time = time.time()

    # make a path that visits all the cities exactly once. Example: [0, 2, 1, 3, 4, 5]
    path = []
    for i in range(city_count):
        path.append(i)
        
    total_distance = find_total_distance(distance_table, path)
    best_distance = total_distance
    best_path = path

    # make a list of all possible paths, including the current path

    # add 1 to the city number for every city in path
    for path_index in path:
        path[path_index] += 1
    #print('path after incrament by one is: ', path)
    list_of_possible_path_tuples = list(itertools.permutations(path))
    


    # print off our list of all possible paths
    #print('list of all possible paths')
    #for path in list_of_possible_path_tuples:
        #print('path has the type:', type(path))
        #print(path)

    list_of_path_lists = []
    for path in list_of_possible_path_tuples:
        list_of_path_lists.append(list(path))

    # print off our list of all possible paths
    #print('list of all possible paths')
    #for path in list_of_path_lists:
        #print('path has the type:', type(path))
        #print(path)

    # reduce the city index for each city in each list in the list of path lists
    for path in list_of_path_lists:
        for path_index in range(0, len(path)):
            path[path_index] -= 1

    # print off our list of all possible paths
    #print('list of all possible paths')
    #for path in list_of_path_lists:
        #print('path has the type:', type(path))
        #print(path)

    # remove any path that does not start at city 0

    edited_list_of_path_lists = []
    for path in list_of_path_lists:
        if path[0] == 0:
            edited_list_of_path_lists.append(path)

    # go through all possible paths, find the path distance, and keep track of the best path so far.
    # for each path, print the path and the distance.
    # if the current path is better than the best path, set the best path to the current path

    for path in edited_list_of_path_lists:
        total_distance = find_total_distance(distance_table, path)
        #print('path: ', path, end=" ")
        #print(',  total distance: ', total_distance)

        best_distance, best_path = check_for_better_path(distance_table, path, total_distance, best_distance, best_path)

    stop_time = time.time()
    run_time = stop_time - start_time
    # after time has passed, print the best path and best distance
    print('for brute force, after {0} seconds, the best path is {1} with a distance of {2}'.format(run_time, best_path, best_distance))
    #return [best_path, best_distance]

def run_greedy_algorithm(distance_table, city_count):
    #print('starting greedy algorithm')
    # start a timer
    start_time = time.time()

    # make a path that visits all the cities exactly once. Example: [0, 2, 1, 3, 4, 5]
    list_of_all_cities = []
    for numeric_index in range(city_count):
        list_of_all_cities.append(numeric_index)
    print('start of greedy algo, list of all cities is: ', list_of_all_cities)

        
    total_distance = find_total_distance(distance_table, list_of_all_cities)
    best_distance = total_distance
    best_path = list_of_all_cities
    #print('at the start of the algorithm, we tested path {0} with a distance of {1}'.format(best_path, best_distance))

    # loop through all cities as the starting city and use the greedy algorithm to find the path
    for starting_city in range(city_count):
        #print('starting to build our paths.')
        #print('our starting city is: ', starting_city)

        # make a list of all possible cities to visit
        cities_to_visit = list_of_all_cities.copy()
        #print('after copying list of all cities, the cities to visit are: ', cities_to_visit)
            
        current_path = []
        current_path.append(starting_city)

        #print('after adding starting city, the current path is: ', current_path)

        # remove the starting city from the list of cities to visit
        cities_to_visit.remove(starting_city)
        print('after removing starting city, the cities to visit are: ', cities_to_visit)
        
        for path_addition_index in range(1, city_count - 1):
            print('path addition index is: ', path_addition_index)
            from_city = current_path[path_addition_index - 1]
            # to start the comparison, look at the next city in the list of cities to visit
            closest_city = cities_to_visit[0]
            closest_city_distance = distance_table[from_city][closest_city]
            print('as a place holder before working the greedy algorithm to find the next closest city, the from city is {}, the closest city is {}, and the distance is: {}'.format(from_city, closest_city, closest_city_distance))
            
            for city_to_check in cities_to_visit:
                print('city to check is: ', city_to_check)
                distance_from_starting_city_to_city_to_check = distance_table[starting_city][city_to_check]
                print('distance from {0} to {1} is: {2}'.format(starting_city, city_to_check, distance_from_starting_city_to_city_to_check))
                if distance_from_starting_city_to_city_to_check < closest_city_distance:
                    closest_city = city_to_check
                    closest_city_distance = distance_from_starting_city_to_city_to_check
                    print('closest city is: ', closest_city)
                    print('closest city distance is: ', closest_city_distance)
            current_path.append(closest_city)
            print('current path after checking all cities for the next closest city to {}, which was city {}, is: {}'.format(from_city, closest_city, current_path))
        print('after greedy algorithm for starting city {}, the current path is: {}, and has a distance of {}'.format(starting_city, current_path, find_total_distance(distance_table, current_path)))

if __name__ == "__main__":

    # set random seed to clock time
    #random.seed(time.time())
    random.seed(12)

    # priliminary user interactions
    city_count = 5
    run_time = 0.01
    distance_table = generate_distance_table(city_count)

    #print_distance_table(distance_table)
    
    #run_guess_and_check_algorithm(distance_table, run_time)

    #run_brute_force_algorithm(distance_table, run_time)

    run_greedy_algorithm(distance_table, city_count)




    

    
    

