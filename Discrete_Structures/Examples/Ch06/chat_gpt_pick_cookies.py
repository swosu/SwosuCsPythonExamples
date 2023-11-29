from itertools import combinations_with_replacement

# Define the types of cookies available
cookie_types = ["chocolate chip", "peanut butter", "sugar", "fig newton"]

# Define the number of cookies to pick
num_cookies_to_pick = 6

# Use itertools to generate all combinations with replacement
cookie_combinations = list(combinations_with_replacement(cookie_types, num_cookies_to_pick))

# Print the count of all possible combinations
print("Total number of possible combinations:", len(cookie_combinations))

# Print all possible combinations
for combination in cookie_combinations:
    print(combination)
