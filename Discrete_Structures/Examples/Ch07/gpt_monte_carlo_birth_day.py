import random
import matplotlib.pyplot as plt

def monte_carlo_birthday_problem(num_people, num_trials=10000):
    """Simulates the birthday problem using Monte Carlo method for a given number of people."""
    shared_count = 0
    
    for _ in range(num_trials):
        birthdays = [random.randint(1, 366) for _ in range(num_people)]  # Assign random months (1-12)
        if len(birthdays) > len(set(birthdays)):  # Check if any month repeats
            shared_count += 1
    
    return (shared_count / num_trials) * 100  # Convert to percentage

# Simulation settings
num_trials = 100000  # Number of trials per group size
min_people = 2
max_people = 367

# Run simulation for different room sizes
results = {}
for people in range(min_people, max_people + 1):
    prob = monte_carlo_birthday_problem(people, num_trials)
    results[people] = prob

# Print results in table format
print("| People in Room | Probability (%) |")
print("|---------------|----------------|")
for people, prob in results.items():
    print(f"| {people:<15} | {prob:.2f}% |")

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(list(results.keys()), list(results.values()), marker='o', linestyle='-', color='b', label="Monte Carlo Simulation")
plt.xlabel("Number of People in the Room")
plt.ylabel("Probability of Shared Birthday (%)")
plt.title("Monte Carlo Simulation of Birthday Problem (by Month)")
plt.xticks(range(min_people, max_people + 1))
plt.yticks(range(0, 101, 10))
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
