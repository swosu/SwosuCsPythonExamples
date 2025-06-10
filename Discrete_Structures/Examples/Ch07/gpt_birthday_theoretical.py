import matplotlib.pyplot as plt

def birthday_probability(n):
    """Computes probability of at least two people sharing a birthday using the complement method."""
    if n > 366:
        return 100.0  # More than 366 people guarantees a shared birthday
    prob_unique = 1.0
    total_days = 366  # Leap year included

    for i in range(n):
        prob_unique *= (total_days - i) / total_days  # Compute complement

    return (1 - prob_unique) * 100  # Convert to percentage

# Define range of people
min_people = 2
max_people = 90
people_range = list(range(min_people, max_people + 1))

# Compute probabilities
probabilities = [birthday_probability(n) for n in people_range]

# Print results in table format
print("| People in Room | Probability (%) |")
print("|---------------|----------------|")
for people, prob in zip(people_range, probabilities):
    print(f"| {people:<15} | {prob:.2f}% |")

# Plot results
plt.figure(figsize=(8, 5))
plt.plot(people_range, probabilities, marker='o', linestyle='-', color='r', label="Theoretical Probability")
plt.xlabel("Number of People in the Room")
plt.ylabel("Probability of Shared Birthday (%)")
plt.title("Probability of at Least Two People Sharing a Birthday")
plt.xticks(people_range)
plt.yticks(range(0, 101, 10))
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()
