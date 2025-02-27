import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_trials, num_dice=1, sides=20):
    """
    Simulate rolling multiple dice.
    
    Args:
        num_trials (int): Number of trials to simulate.
        num_dice (int): Number of dice to roll in each trial.
        sides (int): Number of sides on each die.
    
    Returns:
        np.ndarray: Array containing results of dice rolls.
    """
    return np.random.randint(1, sides + 1, size=(num_trials, num_dice))

def analyze_and_print_dice_rolls(rolls):
    """
    Analyze and print the results of dice rolls.
    
    Args:
        rolls (np.ndarray): Array containing results of dice rolls.
    """
    # Calculate average roll
    average_roll = np.mean(rolls)
    
    # Count the number of natural 20s and critical fails
    num_nat_20s = np.sum(rolls == 20)
    num_crit_fails = np.sum(rolls == 1)
    
    # Calculate the percentage of rolls that are 10 or above and 15 or above
    num_10_or_above = np.sum(rolls >= 10)
    num_15_or_above = np.sum(rolls >= 15)
    
    total_rolls = rolls.size

    # Print the analysis
    print("Average Roll:", average_roll)
    print(f"Number of Natural 20s: {num_nat_20s} out of {total_rolls} ({num_nat_20s / total_rolls * 100:.2f}%)")
    print(f"Number of Critical Fails: {num_crit_fails} out of {total_rolls} ({num_crit_fails / total_rolls * 100:.2f}%)")
    print(f"Percentage of Rolls 10 or Above: {num_10_or_above} out of {total_rolls} ({num_10_or_above / total_rolls * 100:.2f}%)")
    print(f"Percentage of Rolls 15 or Above: {num_15_or_above} out of {total_rolls} ({num_15_or_above / total_rolls * 100:.2f}%)")

def plot_dice_roll_distribution(rolls):
    """
    Plot the distribution of dice rolls.
    
    Args:
        rolls (np.ndarray): Array containing results of dice rolls.
    """
    plt.hist(rolls.flatten(), bins=np.arange(1, 22), align='left', rwidth=0.8)
    plt.title('Distribution of Dice Rolls')
    plt.xlabel('Result')
    plt.ylabel('Frequency')
    plt.xticks(np.arange(1, 21))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def print_dice_roll_distribution(rolls):
    # Create a dictionary to store the count of each roll
    roll_counts = {i: 0 for i in range(1, 21)}

    # Count the occurrences of each roll
    for roll in rolls.flatten():
        roll_counts[roll] += 1

    # Print the distribution
    for roll, count in roll_counts.items():
        print(f'Roll {roll}: {count} times')


if __name__ == "__main__":

    # Set the number of trials
    num_trials = 1000000

    # Simulate rolling a D20 die a million times
    rolls = simulate_dice_rolls(num_trials)

    # Analyze and print the results of dice rolls
    analyze_and_print_dice_rolls(rolls)

    # Plot the distribution of dice rolls
    plot_dice_roll_distribution(rolls)

    # Call the function with the rolls
    print_dice_roll_distribution(rolls)
