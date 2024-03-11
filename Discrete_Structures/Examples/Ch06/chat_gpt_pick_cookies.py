from itertools import combinations_with_replacement

# https://discrete.openmathbooks.org/dmoi2/ch_counting.html 
# https://discrete.openmathbooks.org/dmoi2/sec_stars-and-bars.html

# Define the types of cookies available
#cookie_types = ["chocolate chip"]
#cookie_types = ["chocolate chip", "peanut butter"]
#cookie_types = ["chocolate chip", "peanut butter", "sugar"]
#cookie_types = ["chocolate chip", "peanut butter", "sugar", "fig newton"]
cookie_types = []

nubmber_of_cookie_types = 4
for index in range(nubmber_of_cookie_types):
    cookie_types.append(str(index + 1))

# Print the types of cookies available
print("Types of cookies available:", cookie_types)



# Define the number of cookies to pick
num_cookies_to_pick = 6

# Use itertools to generate all combinations with replacement
cookie_combinations = list(combinations_with_replacement(cookie_types, num_cookies_to_pick))

# Print the count of all possible combinations
print("Total number of possible combinations:", len(cookie_combinations))

# Print all possible combinations
for combination in cookie_combinations:
    print(combination)

print("\nTotal number of possible combinations:", len(cookie_combinations))