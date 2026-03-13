import csv
from src.simulator import simulate_games

games = simulate_games(10000)

with open("data/raw/craps_games.csv","w",newline="") as f:

    writer = csv.DictWriter(
        f,
        fieldnames=["game_id","outcome","num_rolls","sequence"]
    )

    writer.writeheader()

    for g in games:
        writer.writerow(g)