print('hello')

import random

def geometric_sequence():
    first_number = random.randint(1, 10)
    ratio = random.randint(2, 10)
    sequence = [first_number]
    for generation_index in range(1, 5):
        sequence.append(sequence[generation_index - 1] * ratio)

    for print_index in range(5):
        print(sequence[print_index], end=' ')

    next_number = sequence[4] * ratio 
    return next_number

def arithmetic_progression_sequence():
    initial_term = random.randint(1, 10)
    common_difference = random.randint(1, 10)
    sequence = [initial_term]
    for generation_index in range(1, 5):
        sequence.append(sequence[generation_index - 1] + common_difference)

    for print_index in range(5):
        print(sequence[print_index], end=' ')

    next_number = sequence[4] + common_difference
    return next_number

def fibonacci_sequence():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    sequence = [first_number, second_number]
    for generation_index in range(2, 5):
        sequence.append(sequence[generation_index - 1] + sequence[generation_index - 2])

    for print_index in range(5):
        print(sequence[print_index], end=' ')

    next_number = sequence[4] + sequence[3]
    return next_number

def constant_sequence():
    constant = random.randint(1, 10)
    sequence = [constant] * 5
    for print_index in range(5):
        print(sequence[print_index], end=' ')
    return constant


if __name__ == '__main__':
    print('welcome to the guess the sequence game')
    print('you will be given a sequence of numbers and you have to guess the next number in the sequence')
    print('you will be given 3 chances to guess the next number')
    print('good luck')

    

    user_score = 0

    for sequence_index in range(1, 5):
        print(f'sequence {sequence_index}')

        if 1 == sequence_index:
            next_number = geometric_sequence()
        elif 2 == sequence_index:
            next_number = arithmetic_progression_sequence()
        elif 3 == sequence_index:
            next_number = fibonacci_sequence()
        elif 4 == sequence_index:
            next_number = constant_sequence()
        else:
            print('1 2 3 4')
            next_number = 5

        while True:
            try:
                user_guess = int(input('enter your guess: '))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

        if user_guess == next_number:
            print('correct')
            user_score += 1
        else:
            print(f'incorrect. the correct answer is {next_number}')
    print(f'your score is {user_score}') 



     