import time
import random

def run_guess_and_check(city_count, run_time, distance_table):
    print('running gnc')

    print('city_count: {}'.format(city_count))
    print('run_time: {}'.format(run_time))
    print('distance_table: {}'.format(distance_table))

    # start the timer
    start_time = time.time()

    while True:
        print('looping')
        
        #print('load a list of all possible paths')
        possible_path = []
        for index in range(city_count):
            possible_path.append(index)

        #print('possible path:')
        #print(possible_path)

        # randomly select a path
        #print('randomly select a path')
        current_path = []
        for index in range(city_count):
            #print('index: {}'.format(index))
            # print the possible paths
            #print('possible_path: {}'.format(possible_path))
            next_city = random.choice(possible_path)
            #print('next_city: {}'.format(next_city))
            possible_path.remove(next_city)
            current_path.append(next_city)

        print('distance table:')
        print(distance_table)

        print('current_path: {}'.format(current_path))

        # calculate the distance of the path
        total_distance = 0

        for index in range(city_count - 1):
            from_city = current_path[index]
            print('from city: {}'.format(from_city))
            to_city = current_path[index + 1]
            print('to city: {}'.format(to_city))
            print('so far we have traveled this far: {}'.format(total_distance))
            current_distance = distance_table[from_city][to_city]
            print('our current distance for this city pair is: {}'.format(current_distance))

            print('adding current distance to total distance')
            total_distance += current_distance
            print('total distance is now: {}'.format(total_distance))



        

        current_time = time.time()
        if current_time - start_time >= run_time:
            print('time is up')
            break




    