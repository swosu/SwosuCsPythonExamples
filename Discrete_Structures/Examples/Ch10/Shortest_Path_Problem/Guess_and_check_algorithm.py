# Description: This file contains the code for the guess and check algorithm.
#import the Build_Map.py file
import Build_Map as map_handler

import random # for random number generation

def run_guess_and_check_algorithm(city_count):
    print('running the guess and check algorithm.')
    path = []
    while len(path) < city_count:
        possible_next_city = int(random.randint(1, city_count))
        if possible_next_city not in path:
            path.append(possible_next_city)
    return path


if __name__ == '__main__':
    print('hello from the guess and check and guess and check algo.')
    city_count = 8
    map = map_handler.check_if_map_exists(city_count)
    map_handler.print_map(map)

    path = run_guess_and_check_algorithm(city_count)
    print(f'path from gnc algorithm: {path}')
    print(f'the variable path has a length of {len(path)} and data type of {type(path)}')

    distance = map_handler.get_distance(path, map )

    print(f"the path: {path} has a distance of {distance}.")
