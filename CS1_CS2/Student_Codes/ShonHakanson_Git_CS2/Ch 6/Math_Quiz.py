#Math quiz designed to ask a specified number of questions about simple math operations involving addition, subtraction, multiplication, and 
#division involving numbers between 1 and 10. It will keep track of how many questions you got write and give a score at the end.
import random

def math_quiz():
    print("Welcome to the Math Quiz!")
    num_questions = int(input("How many questions would you like to answer? "))
    score = 0

    for _ in range(num_questions):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '-', '*', '/'])

        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        elif operation == '*':
            correct_answer = num1 * num2
        elif operation == '/':
            # Ensure no division by zero and result is an integer
            num1 = num1 * num2
            correct_answer = num1 // num2

        user_answer = float(input(f"What is {num1} {operation} {num2}? "))

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer was {correct_answer}.")

    print(f"You got {score} out of {num_questions} questions correct.")
    print(f"Your score: {(score / num_questions) * 100:.2f}%")

if __name__ == "__main__":
    math_quiz()

