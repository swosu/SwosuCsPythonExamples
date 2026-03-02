import numpy as np
import random

# Probability of the coin landing on its side
p_side = 0.00001  # 0.001%
def calculate_required_flips(confidence_level, num_simulations=10000):
    """
    Calculate the number of flips needed to achieve the given confidence level.
    
    Parameters:
    confidence_level (float): Desired confidence level (e.g., 0.5 for 50%)
    num_simulations (int): Number of Monte Carlo simulations per n
    
    Returns:
    int: The number of flips needed
    """
    # Initialize variables
    n = 1
    success_count = 0
    
    # Iterate until we reach the confidence level
    while True:
        # Simulate num_simulations trials with n flips
        successes = 0
        for _ in range(num_simulations):
            flips = [random.random() for _ in range(n)]
            if any(f < p_side for f in flips):
                successes += 1
        
        # Calculate the success rate
        success_rate = successes / num_simulations
        
        # Check if the success rate meets the confidence level
        if success_rate >= confidence_level - 0.0001:  # Allow for small tolerance
            return n
        
        # Increment n for the next iteration
        n += 1

# Define confidence levels
confidence_levels = [0.5, 0.75, 0.9, 0.95, 0.99]

# Number of Monte Carlo simulations per n
num_simulations = 10000

# Calculate required flips for each confidence level
results = {}
for level in confidence_levels:
    print(f"Calculating required flips for {level*100}% confidence level...")
    required_flips = calculate_required_flips(level, num_simulations)
    results[level] = required_flips
    print(f"Required flips: {required_flips}")
