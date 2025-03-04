from math import comb

def count_cookie_combinations(total_cookies, cookie_types):
    """
    This function calculates the number of ways to choose total_cookies from cookie_types
    using the "stars and bars" combinatorial method.
    
    Parameters:
    total_cookies (int): Total number of cookies to be chosen.
    cookie_types (int): Number of different cookie types.
    
    Returns:
    int: The number of ways to distribute the cookies.
    """
    return comb(total_cookies + cookie_types - 1, cookie_types - 1)

# Given problem parameters
total_cookies = int(input("Enter the total number of cookies: "))
cookie_types = int(input("Enter the number of cookie types: "))

# Compute and print the result
result = count_cookie_combinations(total_cookies, cookie_types)
print(f"The number of different ways to choose {total_cookies} cookies from {cookie_types} types is: {result}")
