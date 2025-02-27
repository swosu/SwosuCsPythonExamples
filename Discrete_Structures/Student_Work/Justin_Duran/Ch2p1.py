import random

def sequence_1():
    # Arithmetic progression example (increment by 2)
    return [2, 4, 6, 8, 10]

def sequence_2():
    # Geometric progression example (each term multiplies by 3)
    return [3, 9, 27, 81, 243]

def sequence_3():
    # Fibonacci-like progression (sum of last two terms to generate next term)
    return [0, 1, 1, 2, 3]

def sequence_4():
    # Custom sequence (a pattern of your choice, e.g., powers of 2)
    return [1, 2, 4, 8, 16]

def get_sequence():
    # Randomly select one of the four sequences
    return random.choice([sequence_1, sequence_2, sequence_3, sequence_4])()

def main():
    # Select a random sequence
    sequence = get_sequence()

    # Display the first five terms of the selected sequence
    print(f"Here are the first five terms of the sequence: {sequence}")
    
    # Ask the user to guess the sixth term
    guess = int(input("What do you think the sixth term is? "))
    
    # Determine the correct sixth term based on the sequence
    if sequence == sequence_1():
        correct = 12  # The sixth term of the arithmetic sequence (10 + 2)
    elif sequence == sequence_2():
        correct = 729  # The sixth term of the geometric sequence (243 * 3)
    elif sequence == sequence_3():
        correct = 5  # The sixth term of the Fibonacci-like sequence (3 + 2)
    elif sequence == sequence_4():
        correct = 32  # The sixth term of the custom sequence (16 * 2)

    # Check if the user's guess is correct
    if guess == correct:
        print("Correct! Well done.")
    else:
        print(f"Incorrect! The correct answer was {correct}.")

if __name__ == "__main__":
    main()
