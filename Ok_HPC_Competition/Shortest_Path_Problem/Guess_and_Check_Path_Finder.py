class Guess_and_Check_Path_Finder:
    def __init__(self, city_count):
        self.data = []
        self.city_count = city_count
        self.cities_to_visit = []
        self.file_name = ''
        self.distance_table = []
        self.path = []

    def run_guess_and_check_algorithm(self, map_handler_object, time_limit_in_seconds):
        import time
        self.path = []
        self.find_path()
        min_path_distance = map_handler_object.get_path_distance(self.path)
        min_path = list(self.path)
        print(f'current min {min_path_distance}. {min_path}')
        tic = time.perf_counter()
        toc = time.perf_counter()
        while time_limit_in_seconds > (toc - tic):
            self.path = []
            self.find_path()
            current_path_distance = map_handler_object.get_path_distance(self.path)
            if current_path_distance < min_path_distance :
                min_path_distance = current_path_distance
                min_path = list(self.path)
                print(f'new min {min_path_distance}. {min_path}')
            toc = time.perf_counter()



    def say_hello(self):
        #self.say_hello()
        print('So that worked...')

    def get_path(self):
        return self.path

    def find_path(self):
        import random
        self.get_cities_to_visit_list()
        for index in range(0, self.city_count):
            #print(f'our index is {index}.')
            next_city = random.choice(self.cities_to_visit)
            #print(f'our next city is: {next_city}.')
            self.path.append(next_city)
            #print(f'our current path is: {self.path}.')
            self.cities_to_visit.remove(next_city)
            #print(f'remaining cities to visit: {self.cities_to_visit}.')
        #print(f'our guess and check path is:\n {self.path}.')

    def get_cities_to_visit_list(self):
        for index in range(0, self.city_count):
            #print(f'our index is {index}.')
            self.cities_to_visit.append(index)
        #print(f'possible cites to visit are: {self.cities_to_visit}.')
