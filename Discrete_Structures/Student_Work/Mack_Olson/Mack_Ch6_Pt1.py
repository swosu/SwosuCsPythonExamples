from math import comb

def count_cookie_combinations(total_cookies, cookie_types):
    return comb(total_cookies + cookie_types - 1, cookie_types - 1)

# Given problem parameters
total_cookies = int(input("Enter the total number of cookies: "))
cookie_types = int(input("Enter the number of cookie types: "))

# Compute and print the result
result = count_cookie_combinations(total_cookies, cookie_types)
print(f"The number of different ways to choose {total_cookies} cookies from {cookie_types} types is: {result}")
