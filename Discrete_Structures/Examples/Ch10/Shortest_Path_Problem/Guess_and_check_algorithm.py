# Description: This file contains the code for the guess and check algorithm.
#import the Build_Map.py file
import Build_Map as map_handler

import random # for random number generation

import time # for time keeping

class Shortest_Path_Problem:
    def __init__(self):
        self.city_count = 0
        self.map = []
        self.path = []
        self.distance = 0
        self.time_limit_seconds = 0

    def run_guess_and_check_algorithm(self):
        print('running the guess and check algorithm.')
        start_time = time.time()
        elapsed_time = 0
        
        path = []
        path = guess_a_random_path(self.city_count)
        print('path:', path)
        distance = map_handler.calculate_path_distance(self)
        print('distance:', distance)
        minimum_distance = distance
        minimum_path = path
        while elapsed_time < self.time_limit_seconds:
            


            elapsed_time = time.time() - start_time


def guess_a_random_path(city_count):
    print('running the guess and check algorithm.')
    path = []
    while len(path) < city_count:
        possible_next_city = int(random.randint(1, city_count))
        if possible_next_city not in path:
            path.append(possible_next_city)
    return path


if __name__ == '__main__':
    print('hello from the guess and check and guess and check algo.')

    spp = Shortest_Path_Problem()
    spp.city_count = 4
    spp.map = map_handler.check_if_map_exists(spp)
    map_handler.print_map(spp)

    spp.time_limit_seconds = 2

    spp.run_guess_and_check_algorithm()

    print('done.')


