#geometric progression

def geometric_progression(constant, base, n):
    return constant * (base ** (n ))


# Write a program: 
# Write a program that gives the first five terms of a sequence 
# and asks the user to guess the sixth. 
# The program should be able to choose between four sequences


import random

def main():
    constant = random.randint(1, 10) # from the book example, this is a
    base = random.randint(1, 10) # from the book example, this is r
    n_lower_limit = 0
    n_upper_limit = 5

    sequence = []
    for term_index in range(n_lower_limit, n_upper_limit):
        term = geometric_progression(constant, base, term_index)
        sequence.append(term)
    # print off what my constant, base, and upper and lower limits are
    print("The constant is: ", constant)
    print("The base is: ", base)
    print("The lower limit is: ", n_lower_limit)

    print("The first five terms of the sequence are: ", sequence)
    guess = int(input("What is the sixth term of the sequence? "))
    if guess == geometric_progression(constant, base, n_upper_limit):
        print("Correct!")
    else:
        print("Incorrect. The sixth term is ", geometric_progression(constant, base, n_upper_limit))

main()
