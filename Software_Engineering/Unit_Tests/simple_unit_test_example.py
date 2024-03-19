def add_two_numbers(a, b):
    return a - b

# assert add_two_numbers(1, 2) == 3, "1 + 2 should be 3" and print off what it got and what it expected if it fails

assert add_two_numbers(1, 2) == 3, "1 + 2 should be 3, but got " + str(add_two_numbers(1, 2))