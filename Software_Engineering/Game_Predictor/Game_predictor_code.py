import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import tensorflow as tf

if __name__ == '__main__':
    

    # Load the data
    # https://projects.fivethirtyeight.com/2021-nfl-predictions/games/
    df = pd.read_csv('https://projects.fivethirtyeight.com/2021-nfl-predictions/games/games.csv')

    # print off the first 5 rows of the data
    print(df.head())
