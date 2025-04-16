"""Guess and check code to find a shortest hammalton path through a graph."""

import pandas as pd
import numpy as np
import itertools
import time
import sys
import os
import math
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import rc
from matplotlib import rcParams
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

import Data_Loader
import Greedy_Shortest_Path








if __name__ == '__main__':

    print('welcome to the shortest path problem code')

    # load the data
    our_data = Data_Loader.Data_Loader()
    our_data.city_count = 4
    our_data.load_data()
    print(f'file name is {our_data.file_name}')
    print(our_data.df.to_string(index=False))

    # build a guess and check algorithm object based on a different class and run it for 30 seconds

    greedy = Greedy_Shortest_Path.Greedy_Shortest_Path()
    greedy.city_count = our_data.city_count
    greedy.df = our_data.df
    greedy.run_guess_and_check(30)