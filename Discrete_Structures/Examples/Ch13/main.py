import random
import time

if __name__ == "__main__":

    # set random seed to clock time
    random.seed(time.time())

    # priliminary user interactions
    city_count = 6
    run_time = 2
    distance_table = []
    # initilize distance table
    rows, cols = (city_count, city_count)
    distance_table = [[0 for i in range(cols)] for j in range(rows)]

    # fill distance table with random numbers that range from 1 to 10 * city_count
    for i in range(city_count):
        for j in range(city_count):
            if i == j:
                distance_table[i][j] = 0
            else:
                distance_table[i][j] = random.randint(1, 10 * city_count)

    # print distance table and pad the numbers so they are all the same length and columns line up correctly
    print("Distance Table:")
    for i in range(city_count):
        for j in range(city_count):
            print(str(distance_table[i][j]).ljust(3), end=" ")
        print() 

    # start a timer
    start_time = time.time()

    while (time.time() - start_time) < run_time:
        # make a list of all possible cities to visit
        cities_to_visit = []
        for i in range(city_count):
            cities_to_visit.append(i)

        # print the list of cities to visit
        print("Cities to visit: ", end="")
        for i in range(city_count):
            print(str(cities_to_visit[i]).ljust(3), end=" ")
        print()



    

    
    

