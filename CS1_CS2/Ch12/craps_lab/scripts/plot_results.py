import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/craps_games.csv")

df["num_rolls"].hist(bins=20)

plt.title("Distribution of Rolls Per Game")
plt.xlabel("Rolls")
plt.ylabel("Frequency")

plt.show()