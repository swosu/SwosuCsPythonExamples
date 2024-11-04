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
        self.minimum_path = []
        self.minimum_distance = 0
        self.test_path = []
        self.test_distance = 0
        self.distance = 0
        self.time_limit_seconds = 0

    def run_guess_and_check_algorithm(self):
        print('running the guess and check algorithm.')
        start_time = time.time()
        elapsed_time = 0
        
        self.path = []
        self.path = guess_a_random_path(self.city_count)
        print('here is a random path:', self.path, '\t', end='')
        self.distance = map_handler.calculate_path_distance(self)
        print('distance:', self.distance)
        self.minimum_distance = self.distance
        self.minimum_path = self.path
        while elapsed_time < self.time_limit_seconds:
            self.test_path = []
            self.test_distance = 0
            self.test_path = guess_a_random_path(self.city_count)
            self.test_distance = map_handler.calculate_path_distance(self)
            print('test path:', self.test_path, '\t', 'test distance:', self.test_distance, '\t', end='')
            if self.test_distance < self.minimum_distance:
                self.minimum_distance = self.test_distance
                self.minimum_path = self.test_path
                print('new minimum distance:\t', self.minimum_distance, '\t', "new path:\t", self.minimum_path, end='')
            elapsed_time = time.time() - start_time


def guess_a_random_path(city_count):
    #print('guessing a random path. \t', end='')
    path = []
    possible_cities = []
    for i in range(1, city_count + 1):
        possible_cities.append(i)

    #print('possible cities:', possible_cities)

    for i in range(0, city_count):
        next_possible_city = random.choice(possible_cities)
        possible_cities.remove(next_possible_city)
        path.append(next_possible_city)
    return path


if __name__ == '__main__':
    print('hello from the guess and check and guess and check algo.')

    random.seed(time.time())
    #random.seed(42)
    spp = Shortest_Path_Problem()
    spp.city_count = 4
    spp.map = map_handler.check_if_map_exists(spp)
    map_handler.print_map(spp)

    spp.time_limit_seconds = 0.5

    spp.run_guess_and_check_algorithm()

    print('done.')


