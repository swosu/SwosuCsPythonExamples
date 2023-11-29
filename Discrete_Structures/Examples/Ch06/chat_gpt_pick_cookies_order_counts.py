from itertools import permutations

# Define the types of cookies available
cookie_types = ["chocolate chip", "peanut butter", "sugar", "fig newton"]

# Define the number of cookies to pick
num_cookies_to_pick = 6

# Use itertools to generate all permutations
cookie_permutations = list(permutations(cookie_types, num_cookies_to_pick))

# Print the count of all possible permutations
print("Total number of possible permutations:", len(cookie_permutations))

# Print all possible permutations
for permutation in cookie_permutations:
    print(permutation)
