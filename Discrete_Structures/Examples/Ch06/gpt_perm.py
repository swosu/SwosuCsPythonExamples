from itertools import permutations
import math

# Loop from n = 1 to n = 5
for n in range(1, 6):
    print(f"Permutations for n = {n}:")
    
    numbers = list(range(1, n + 1))  # Create list [1, 2, ..., n]
    perm_list = list(permutations(numbers))  # Generate all permutations
    
    # Print all permutations
    for perm in perm_list:
        print(" ".join(map(str, perm)))
    
    # Count permutations
    perm_count = len(perm_list)
    factorial_n = math.factorial(n)  # Compute n!
    
    # Display counts
    print(f"Total permutations: {perm_count}")
    print(f"n! = {factorial_n}\n")
