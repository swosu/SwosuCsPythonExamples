#print('Hello.')
from Map_handler import Map_handler
from Guess_and_Check_Path_Finder import Guess_and_Check_Path_Finder

city_count = 500
time_limit_in_seconds = 300

map_handler_object = Map_handler(city_count)
map_handler_object.load_map()

guess_and_check_path_finder = Guess_and_Check_Path_Finder(city_count)

guess_and_check_path_finder.run_guess_and_check_algorithm(map_handler_object, time_limit_in_seconds)
