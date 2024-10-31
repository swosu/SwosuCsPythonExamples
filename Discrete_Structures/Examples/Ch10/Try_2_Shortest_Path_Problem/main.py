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

    def calculate_distance(self, path):
        distance = 0
        for i in range(len(path) - 1):
            from_city = path[i] - 1
            to_city = path[i + 1] - 1
            distance += self.distance_table[from_city][to_city]
        # add the distance from the last city back to the first city
        from_city = path[len(path) - 1] - 1
        to_city = path[0] - 1
        distance += self.distance_table[from_city][to_city]
        return distance


# create a new class called guess and check algorithm that allows us to use what is in the Shortest_Path_Problem class 
# to solve the shortest path problem
class Guess_And_Check_Algorithm(Shortest_Path_Problem):
    def __init__(self):
        super().__init__()
        self.best_path = []
        self.best_distance = -1
        self.test_path = []
        self.test_distance = -1

    def run_guess_and_check_algorithm(self):
        self.best_path = []
        self.best_distance = -1
        self.test_path = []
        self.test_distance = -1

        self.generate_random_path()
        self.print_test_path()
        # from 1 to 2 is 11
        # from 2 to 4 is 13
        # from 4 to 3 is 31
        # from 3 to 1 is 5
        # total distance is 60
    
        # now we want to pass the test_path from guess 
        # and check back to the Shortest_Path_Problem class and calculate the distance
        self.test_distance = self.calculate_distance(self.test_path)
        print('test distance:', self.test_distance)

    def generate_random_path(self):
        # generate a random path
        self.test_path = []
        # make a list of the possible cities, with the first city being 1
        cities = [x for x in range(1, self.city_count + 1)]
        
        # print off the possible cities to visit
        print('possible cities to visit:', cities)

        # randomly select a city from the list of possible cities
        for i in range(self.city_count):
            city = random.choice(cities)
            self.test_path.append(city)
            cities.remove(city)
        

    def print_test_path(self):
        print('test path:', self.test_path)


if __name__ == "__main__":
    random.seed(42) 
    sp = Shortest_Path_Problem()
    sp.build_map()

    gca = Guess_And_Check_Algorithm()
    gca.run_guess_and_check_algorithm()