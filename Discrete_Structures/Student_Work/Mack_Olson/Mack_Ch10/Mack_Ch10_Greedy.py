import pandas as pd
import random
import time
import csv

class GreedyShortestPath:
    def __init__(self, file_path: str, time_limit: int = 5):
        self.file_path = file_path
        self.time_limit = time_limit

        # Load CSV and treat first column as index
        self.df = pd.read_csv(file_path)
        self.df.set_index(self.df.columns[0], inplace=True)

        # Convert all to numeric to prevent errors
        self.df = self.df.apply(pd.to_numeric, errors='coerce').fillna(float('inf'))

        self.city_ids = list(self.df.index)
        self.city_count = len(self.city_ids)
        self.best_path = []
        self.best_path_cost = float('inf')
        self.start_time = 0

    def run(self):
        self.start_time = time.time()
        while time.time() - self.start_time < self.time_limit:
            self.greedy_search()
        self.export_results()

    def greedy_search(self):
        unvisited = set(range(self.city_count))
        current_idx = random.choice(list(unvisited))
        path = [current_idx]
        unvisited.remove(current_idx)
        cost = 0

        while unvisited:
            next_idx = min(unvisited, key=lambda i: self.df.iloc[current_idx, i])
            cost += self.df.iloc[current_idx, next_idx]
            current_idx = next_idx
            path.append(current_idx)
            unvisited.remove(current_idx)

        cost += self.df.iloc[current_idx, path[0]]
        path.append(path[0])

        if cost < self.best_path_cost:
            self.best_path = path
            self.best_path_cost = cost

    def export_results(self):
        city_path = [self.city_ids[i] for i in self.best_path]
        output_file = self.file_path.replace(".csv", "_shortest_path.csv")
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Path"] + city_path)
            writer.writerow(["Total Cost", self.best_path_cost])
        print(f"✅ Shortest path saved to: {output_file}")


# === RUN SCRIPT BELOW ===

if __name__ == "__main__":
    file_path = "C:/Users/kenzi/SwosuCsPythonExamples/Discrete_Structures/Student_Work/Mack_Olson/Mack_Ch10/500.csv"
    gsp = GreedyShortestPath(file_path, time_limit=10)
    gsp.run()
