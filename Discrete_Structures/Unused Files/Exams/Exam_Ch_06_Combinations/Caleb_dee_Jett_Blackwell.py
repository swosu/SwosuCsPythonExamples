from itertools import combinations

# Define the number of types of cookies and the number to choose

num_types = 4

num_to_choose = 6

# Calculate the number of ways to choose cookies

num_ways = 0

list = combinations(range(num_types), num_to_choose)

for comb in combinations(range(num_types), num_to_choose):

    num_ways += 1

# Print the result

print(f"There are {num_ways} ways to choose {num_to_choose} cookies from {num_types} types.")