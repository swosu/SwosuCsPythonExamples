import random

def geometric_sequence(start, step):
    sequence = [start]
    for _ in range(5):
        next_term = sequence[-1] * step
        sequence.append(next_term)
    return sequence

def fibonacci_sequence(start, step):
    sequence = [start, start + step]
    for _ in range(3):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

def arithmetic_progression_sequence(start, step):
    sequence = [start]
    for _ in range(5):
        next_term = sequence[-1] + step
        sequence.append(next_term)
    return sequence

def recursive_sequence(start, step):
    sequence = [start]
    for _ in range(5):
        next_term = sequence[-1] + step
        sequence.append(next_term)
        step += 1
    return sequence

def play_game():
    print('welcome to our little game. Try to guess the next number in the sequence.')
    sequence_types = ['geometric', 'fibonacci', 'arithmetic', 'recursive']
    while True:
        sequence_type = random.choice(sequence_types)
        print('our sequence is a', sequence_type, 'sequence.')
        start = random.randint(1, 10)
        step = random.randint(1, 5)
        
        if sequence_type == 'geometric':
            sequence = geometric_sequence(start, step)
        elif sequence_type == 'fibonacci':
            sequence = fibonacci_sequence(start, step)
        elif sequence_type == 'arithmetic':
            sequence = arithmetic_progression_sequence(start, step)
        elif sequence_type == 'recursive':
            sequence = recursive_sequence(start, step)

        print('the correct answer is:', sequence[5])
        

        print("Guess the next number in the sequence: ")
        print(sequence[:5])
        
        guess = int(input("Enter your guess: "))

        
        
        if guess == sequence[5]:
            print("Congratulations! You guessed correctly.")
        else:
            print("Wrong guess. Try again.")
            continue
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() == 'no':
            break

play_game()


# ASCII art of a fish
print('''
   ><(((('>
''')
