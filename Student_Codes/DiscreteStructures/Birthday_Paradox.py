def calculate_probability(n):
    probability = 1.0
    for i in range(n):
        probability *= (365 - i) / 365
    return 1 - probability

def find_min_people(target_probability):
    n = 1
    while True:
        if calculate_probability(n) >= target_probability:
            return n
        n += 1

# Target probabilities
probabilities = [0.70, 0.80, 0.90, 0.95, 0.99]

# Calculate the minimum number of people for each target probability
results = {p: find_min_people(p) for p in probabilities}

# Print the results
for p, n in results.items():
    print(f"To ensure at least {p*100}% probability, you need at least {n} people.")
  
