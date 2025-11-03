import random
from load_quiz import load_quiz_from_file

quiz_dict = load_quiz_from_file('quiz.txt')

questions_list = list(quiz_dict.items())
random.shuffle(questions_list)
score = 0
incorrct_answers = 0
runtime = True

for question, answer in questions_list:

    print(question)
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == answer.strip().lower():
        print("Correct!\n")
        score += 1
        if score == 15:
            print("Congratulations! You've reached the end of the quiz!")
            break
                
    elif user_answer.strip().lower() != answer.strip().lower():
        print(f"Incorrect! The correct answer is: {answer}\n")
        incorrct_answers += 1
        if incorrct_answers == 5:
            print("You've reached the maximum number of incorrect answers. Game over!")
            break
        