import random

def geometric_sequence():
    a = random.randint(1, 10)      
    r = random.randint(2, 5)       
    seq = [a]
    for i in range(1, 5):
        seq.append(seq[i-1] * r)
    print("Sequence:", seq)
    return seq[-1] * r             

def arithmetic_sequence():
    a = random.randint(1, 10)
    d = random.randint(1, 10)
    seq = [a]
    for i in range(1, 5):
        seq.append(seq[i-1] + d)
    print("Sequence:", seq)
    return seq[-1] + d

def fibonacci_sequence():
    f1, f2 = random.randint(1, 10), random.randint(1, 10)
    seq = [f1, f2]
    for i in range(2, 5):
        seq.append(seq[i-1] + seq[i-2])
    print("Sequence:", seq)
    return seq[-1] + seq[-2]

def constant_sequence():
    c = random.randint(1, 10)
    seq = [c] * 5
    print("Sequence:", seq)
    return c

def main():
    print("Welcome to the Guess the Sequence Game!")
    print("You will see 5 terms, and you must guess the 6th.")

    seq_type = random.choice([
        geometric_sequence,
        arithmetic_sequence,
        fibonacci_sequence,
        constant_sequence
    ])
    correct_answer = seq_type()
    guess = int(input("What is the 6th term? "))

    if guess == correct_answer:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect. The 6th term is {correct_answer}.")

if __name__ == "__main__":
    main()
