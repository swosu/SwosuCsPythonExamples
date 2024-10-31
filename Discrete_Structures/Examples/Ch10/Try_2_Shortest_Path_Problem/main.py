import random
import os

class ShortestPathProblem:
    def __init__(self, city_count=4, time_limit=0.5):
        self.time_limit = time_limit
        self.city_count = city_count
        self.distance_table = []
        self.distance_table_file_name = f"dt_{self.city_count}.csv"
        self.max_distance_between_cities = 10 * self.city_count

    def build_map(self):
        """Builds the map either by loading from a file or generating a new one."""
        if os.path.isfile(self.distance_table_file_name):
            self._read_distance_table()
        else:
            self._create_distance_table()

    def _read_distance_table(self):
        """Reads the distance table from a CSV file."""
        with open(self.distance_table_file_name, "r") as file:
            self.distance_table = [
                [int(value) for value in line.strip().split(",")] for line in file
            ]
        self._print_distance_table()

    def _create_distance_table(self):
        """Creates a new distance table and saves it to a CSV file."""
        for i in range(self.city_count):
            row = [0 if i == j else random.randint(1, self.max_distance_between_cities)
                   for j in range(self.city_count)]
            self.distance_table.append(row)

        self._print_distance_table()

        with open(self.distance_table_file_name, "w") as file:
            for row in self.distance_table:
                file.write(",".join(map(str, row)) + "\n")

    def _print_distance_table(self):
        """Prints the current distance table."""
        print("Distance Table:")
        for row in self.distance_table:
            print(" ".join(map(str, row)))

    def calculate_distance(self, path):
        """Calculates the total distance for a given path."""
        distance = sum(self.distance_table[path[i] - 1][path[i + 1] - 1] for i in range(len(path) - 1))
        distance += self.distance_table[path[-1] - 1][path[0] - 1]
        return distance


class GuessAndCheckAlgorithm(ShortestPathProblem):
    def __init__(self, city_count=4):
        super().__init__(city_count=city_count)
        self.best_path = []
        self.best_distance = float("inf")

    def run_guess_and_check_algorithm(self):
        """Runs the algorithm to find the shortest path using guess and check."""
        self.build_map()
        self.generate_random_path()
        self.test_distance = self.calculate_distance(self.test_path)
        print("Test Path:", self.test_path)
        print("Total Distance:", self.test_distance)

    def generate_random_path(self):
        """Generates a random path for all cities."""
        self.test_path = random.sample(range(1, self.city_count + 1), self.city_count)
        print("Generated Random Path:", self.test_path)


if __name__ == "__main__":
    random.seed(42)  # Set a seed for reproducibility
    gca = GuessAndCheckAlgorithm()
    gca.run_guess_and_check_algorithm()


# 1 to 4 is 13
# 4 to 2 is 29
# 2 to 3 is 32
# 3 to 1 is 5
# total is 79