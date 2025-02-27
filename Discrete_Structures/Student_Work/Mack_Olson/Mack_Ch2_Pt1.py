import random

def arithmetic_sequence():
    print("Arithmetic sequence")
    a, d = random.randint(1, 10), random.randint(2, 5)
    return [a + i * d for i in range(6)]

def geometric_sequence():
    print("Geometric sequence")
    a, r = random.randint(1, 5), random.randint(2, 4)
    return [a * (r ** i) for i in range(6)]

def fibonacci_sequence():
    print("Fibonacci sequence")
    a, b = random.randint(1, 5), random.randint(1, 5)
    seq = [a, b]
    for _ in range(4):
        seq.append(seq[-1] + seq[-2])
    return seq

def square_numbers():
    print("Square numbers")
    start = random.randint(1, 5)
    return [(start + i) ** 2 for i in range(6)]

sequences = [arithmetic_sequence, geometric_sequence, fibonacci_sequence, square_numbers]

chosen_sequence = random.choice(sequences)()
first_five, correct_answer = chosen_sequence[:5], chosen_sequence[5]

print("Here are the first five terms of the sequence:", first_five)
guess = int(input("What is the sixth term? "))

if guess == correct_answer:
    print("Correct! Well done!")
else:
    print(f"Incorrect. The correct answer was {correct_answer}.")
