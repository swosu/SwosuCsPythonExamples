from math import comb

# Stars and bars formula to calculate the number of ways to choose r cookies from n types
def ways_to_choose_cookies(n, r):
    return comb(n + r - 1, r)

# Number of types of cookies
n = 4
# Number of cookies to be chosen
r = 6

# Calculate the number of ways to choose the cookies
result = ways_to_choose_cookies(n, r)
print(f"The number of ways to choose {r} cookies from {n} types is: {result}")
