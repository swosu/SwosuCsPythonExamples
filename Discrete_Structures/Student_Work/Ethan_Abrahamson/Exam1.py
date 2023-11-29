import random

def generate_sequence(start, rule):
    # Generate a sequence of 5 terms using the 
    # given rule and starting point
    sequence = [start]
    for i in range(4):
        sequence.append(rule(sequence[i]))
    return sequence

def rule1(x):
    # Add 1 to the previous term
    return x + 1

def rule2(x):
    # Double the previous term
    return 2 * x

def rule3(x):
    # Subtract 2 from the previous term
    return x - 2

def rule4(x):
    # Square the previous term
    return x ** 2

# Create a list of the four rules
rules = [rule1, rule2, rule3, rule4]

# Randomly select a rule and a starting point
rule = random.choice(rules)
start = random.randint(1, 10)

# Generate the sequence using the selected rule and starting point
sequence = generate_sequence(start, rule)

# Display the first four terms and ask the user to guess the fifth term
print(f"The sequence is: {sequence[0]}, {sequence[1]}, {sequence[2]}, {sequence[3]}, ...")
guess = int(input("What is the fifth term? "))

# Check if the user's guess is correct and give feedback
if guess == sequence[4]:
    print("Correct!")
else:
    print(f"Incorrect. The fifth term is {sequence[4]}.")
