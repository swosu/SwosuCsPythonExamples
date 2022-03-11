class Map_handler:
    def __init__(self, city_count):
        self.data = []
        self.file_name = ''
        self.distance_table = []
        self.city_count = city_count

    def get_path_distance(self, path):
        #print(f'working with path: \n {path}.')
        total_distance = 0
        for index in range(0, self.city_count - 1):
            from_city = path[index]
            to_city = path[index + 1]
            distance_between_cities = self.distance_table[from_city][to_city]
            #print(f'from city {from_city} to city {to_city} is {distance_between_cities}.')
            total_distance = total_distance + distance_between_cities
        return total_distance

    def say_hello(self):
        #self.say_hello()
        print('So that worked...')

    def make_file_name(self):
        file_name = f"spp{self.city_count}.bin"
        return file_name

    def build_map(self, file_name):
        import numpy as np
        import random
        print("We are going to build a distance table for", self.city_count, "cities.")
        rows, cols = (self.city_count, self.city_count)
        self.distance_table = [[0 for i in range(cols)] for j in range(rows)]

        for rowIndex in range(rows):
            for columnIndex in range(cols):
                self.distance_table[rowIndex][columnIndex] = random.randint(10,99)

        print(self.distance_table)
        np.array(self.distance_table).tofile(file_name)

    def load_map(self):
        import os.path
        from os import path
        import numpy as np

        print(f'loading map for {self.city_count} cities.')

        file_name = self.make_file_name()
        print(f'looking for file {file_name}.')
        print("We want to open file:", file_name)
        if(path.exists(file_name)):
            print ("File exists")
            self.distance_table = np.fromfile(file_name,  dtype=np.int, count = -1)
            self.distance_table = \
            np.reshape(self.distance_table,(self.city_count,self.city_count))
            print(self.distance_table)
            #return distance_table
        else:
            print("File does not exist")
            print("Building distance table.")
            self.build_map(file_name)
            self.load_map()
