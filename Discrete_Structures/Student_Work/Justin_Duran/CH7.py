def birthday_probability(n):
    days_in_year = 365
    probability_no_shared = 1.0

    # Calculate the probability that no two people share a birthday
    for i in range(n):
        probability_no_shared *= (days_in_year - i) / days_in_year
    
    # The probability that at least two people share a birthday
    return 1 - probability_no_shared

def find_minimum_people(threshold):
    n = 1
    while birthday_probability(n) < threshold:
        n += 1
    return n

# Define the thresholds
thresholds = [0.70, 0.80, 0.90, 0.95, 0.99]

# Find and print the number of people for each threshold
for threshold in thresholds:
    people = find_minimum_people(threshold)
    print(f"At least {people} people are needed for a {threshold*100}% probability.")
