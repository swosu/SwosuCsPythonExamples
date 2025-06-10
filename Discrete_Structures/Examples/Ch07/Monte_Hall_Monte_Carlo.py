import random
import matplotlib.pyplot as plt

# Function to simulate one round of the Monty Hall problem
def monty_hall(simulations):
    verbose_print_statements = True
    outcomes = {
        "Stay and win": 0,
        "Stay and lose": 0,
        "Change and win": 0,
        "Change and lose": 0,
        "Switch Count": 0
    }
    
    for _ in range(simulations):
        doors = [0, 1, 2]  # Three doors
        prize_door = random.choice(doors)  # The prize is behind one random door
        player_choice = random.choice(doors)  # Player randomly picks one door
        
        # Monty opens a losing door that's not the player's choice
        remaining_doors = []
        for door_to_open in doors:
            if door_to_open != player_choice and door_to_open != prize_door:
                remaining_doors.append(door_to_open)
        monty_opens = random.choice(remaining_doors)
        
        # Remaining door to switch to
        switch_choice = None
        for switch_option in doors:
            if switch_option != player_choice and switch_option != monty_opens:
                switch_choice = switch_option
        

        # decide to switch or not
        if random.choice([True, False]):  # Randomly decide whether to switch
            player_choice = switch_choice
            outcomes["Switch Count"] += 1
            # Determine outcomes for changing
            if player_choice == prize_door:
                outcomes["Change and win"] += 1
            else:
                outcomes["Change and lose"] += 1
        
        else:
            player_choice = player_choice
            
            # Determine outcomes for staying
            if player_choice == prize_door:
                outcomes["Stay and win"] += 1
            else:
                outcomes["Stay and lose"] += 1
        
        
        if verbose_print_statements:
            print(f"Prize door: {prize_door}, Player choice: {player_choice}, Monty opens: {monty_opens}, Switch choice: {switch_choice}, Switch count: {outcomes['Switch Count']}")
            print(f'Stay and win, \t Stay and lose, \t Change and win, \t Change and lose, \t Switch Count')
            print(f"{outcomes['Stay and win']}, \t\t {outcomes['Stay and lose']}, \t\t\t {outcomes['Change and win']}, \t\t\t {outcomes['Change and lose']}\t\t\t {outcomes['Switch Count']}")
    return outcomes

# Number of simulation trials
simulations = 5
results = monty_hall(simulations)

# Plotting the results
labels = list(results.keys())
values = list(results.values())

plt.figure(figsize=(8, 6))
plt.bar(labels, values, color=['blue', 'red', 'green', 'orange'])
plt.title(f'Monty Hall Simulation Results (out of {simulations} trials)')
plt.ylabel('Number of Outcomes')
plt.xlabel('Outcome')
plt.show()
