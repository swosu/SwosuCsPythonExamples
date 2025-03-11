import random

def monty_hall_simulation(num_trials=10000, switch=True):
    """Simulates the Monty Hall problem and returns the number of wins."""
    wins = 0
    
    for _ in range(num_trials):
        doors = [0, 0, 1]  # Two losing doors (0) and one winning door (1)
        random.shuffle(doors)
        
        # Contestant makes an initial choice
        chosen_index = random.randint(0, 2)
        
        # Host reveals a losing door
        remaining_indices = [i for i in range(3) if i != chosen_index and doors[i] == 0]
        door_revealed = random.choice(remaining_indices)
        
        # If the contestant switches, choose the remaining door
        if switch:
            chosen_index = next(i for i in range(3) if i != chosen_index and i != door_revealed)
        
        # Check if the contestant won
        if doors[chosen_index] == 1:
            wins += 1
    
    return wins / num_trials  # Return win probability

# Run simulations
num_trials = 10000
stay_win_rate = monty_hall_simulation(num_trials, switch=False)
switch_win_rate = monty_hall_simulation(num_trials, switch=True)

# Print results
print(f"Staying with original choice win rate: {stay_win_rate:.2%}")
print(f"Switching choice win rate: {switch_win_rate:.2%}")
