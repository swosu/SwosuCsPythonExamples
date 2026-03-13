from src.simulator import simulate_games

games = simulate_games(10000)

print("First few games:")

for g in games[:5]:
    print(g)