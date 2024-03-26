import random
import pandas as pd

def monte_carlo_simulation(num_people, num_simulations):
    match_counts = []
    for _ in range(num_simulations):
        # Assign random birth months to people in the room
        birth_months = [random.randint(1, 12) for _ in range(num_people)]
        # Check if two or more people have the same birth month
        if len(birth_months) != len(set(birth_months)):
            match_counts.append(1)
        else:
            match_counts.append(0)
    # Calculate the average number of rooms with matching birth months
    avg_match_count = sum(match_counts) / num_simulations
    return avg_match_count

# Run the Monte Carlo simulation for different numbers of people
results = []
for num_people in range(1, 14):
    avg_match_count = monte_carlo_simulation(num_people, 100000)  # 10,000 simulations
    results.append((num_people, avg_match_count))

# Convert the results to a DataFrame and print
df = pd.DataFrame(results, columns=['Number of People', 'Average Match Count'])
print(df)