class Greedy_Shortest_Path():
    import pandas as pd
    import numpy as np
    import itertools
    import time
    import sys
    import os
    import math
    import random

    def __init__(self):
        self.city_count = 0
        self.df = pd.DataFrame()
        self.file_name = ''
        self.start_time = 0
        self.end_time = 0
        self.time_limit = 0
        self.path = []
        self.path_cost = 0
        self.best_path = []
        self.best_path_cost = 0
        self.best_path_found = False

    def run_guess_and_check(self, time_limit):
        self.start_time = time.time()
        while self.end_time - self.start_time < time_limit:
            self.end_time = time.time()
            self.guess_and_check()
            if self.best_path_found:
                break

    def guess_and_check(self):
        # build a random path
        self.build_random_path()
        # calculate the cost of the path
        self.calculate_path_cost()
        # check to see if the path is better than the best path
        self.check_best_path()
    
    def build_random_path(self):
        self.path = []
        for i in range(self.city_count):
            self.path.append(i)
        random.shuffle(self.path)
        self.path.append(self.path[0])
    
    def calculate_path_cost(self):
        self.path_cost = 0
        for i in range(self.city_count):
            self.path_cost += self.df.iloc[self.path[i], self.path[i+1]]

    def check_best_path(self):
        if self.best_path_found:
            if self.path_cost < self.best_path_cost:
                self.best_path = self.path
                self.best_path_cost = self.path_cost
        else:
            self.best_path = self.path
            self.best_path_cost = self.path_cost
            self.best_path_found = True