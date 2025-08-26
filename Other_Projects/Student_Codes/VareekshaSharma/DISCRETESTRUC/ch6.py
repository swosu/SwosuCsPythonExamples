"""Write a program to answer this question. Look at Example 4 in chapter 6.5. 
Suppose a cookie shop has four different kinds of cookies. How many different ways can six 
cookies be chosen? Assume the type of cookie and not the individual cookies or the order in 
which they are chosen matters."""

import math

cookie_types = int(input("how many types of cookies are there? "))
num_cookies = int(input("how many cookies are you wanting to choose? "))

combos = math.comb(cookie_types + num_cookies - 1, num_cookies)

print(f"there are {combos} ways to choose {num_cookies} cookies given {cookie_types} cookie types.")
