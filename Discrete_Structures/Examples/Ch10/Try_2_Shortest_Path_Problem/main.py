import random

import os


class Shortest_Path_Problem():
    def __init__(self):
        self.time_limit = 0.5
        self.distance_table = []
        self.city_count = 4
        self.distance_table_file_name = ""
        self.max_distance_between_cities = 10 * self.city_count 

    def build_map(self):
        self.distance_table_file_name = "dt_" + str(self.city_count) + ".csv"
        self.check_for_file()

    def check_for_file(self):
        # look for the file
        print('checking for file')
        if os.path.isfile(self.distance_table_file_name):
            print('file exists')
            self.read_distance_table()
        else:
            print('file does not exist')
            self.create_distance_table()

    def read_distance_table(self):
        # read the distance table from the file
        file = open(self.distance_table_file_name, "r")
        for line in file:
            row = line.split(",")
            row = [int(x) for x in row]
            self.distance_table.append(row)
        file.close()
        self.print_distance_table()


    def create_distance_table(self):
        # create the distance table first
     
        for row_index in range(self.city_count):
            row = []
            for col_index in range(self.city_count):
                if row_index == col_index:
                    row.append(0)
                else:
                    row.append(random.randint(1, self.max_distance_between_cities))
            self.distance_table.append(row)

        self.print_distance_table()

        # write the distance table to a csv file
        file = open(self.distance_table_file_name, "w")
        for row in self.distance_table:
            row_str = ""
            for col in row:
                row_str += str(col) + ","
            row_str = row_str[:-1]
            file.write(row_str + "\n")
        file.close()
        self.check_for_file()


    def print_distance_table(self):
        for row in self.distance_table:
            print(row)


if __name__ == "__main__":
    sp = Shortest_Path_Problem()
    sp.build_map()