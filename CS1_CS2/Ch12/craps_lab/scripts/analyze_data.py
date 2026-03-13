import pandas as pd

df = pd.read_csv("data/raw/craps_games.csv")

print(df.head())

print("\nWin Rate:")
print(df["outcome"].value_counts(normalize=True))