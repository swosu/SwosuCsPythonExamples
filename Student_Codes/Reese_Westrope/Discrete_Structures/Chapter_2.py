import random

Sequence1 = [1, 2, 3, 4, 5]
Sequence2 = [5, 10, 15, 20, 25]
Sequence3 = [4, 9, 16, 25, 36]
Sequence4 = [42, 36, 30, 24, 18]

answer1 = 6
answer2 = 30
answer3 = 49
answer4 = 12

play_game = True

def SelectSequence():
    global TestSequence, answer
    sequence = random.randint(1,4)
    if sequence == 1:
        TestSequence = Sequence1
        answer = answer1
    elif sequence == 2:
        TestSequence = Sequence2
        answer = answer2
    elif sequence == 3:
        TestSequence = Sequence3
        answer = answer3
    elif sequence == 4:
        TestSequence = Sequence4
        answer = answer4
    return TestSequence, answer

def GetUserAnswer():
    global user_answer
    print("The following is a sequence of numbers that follows a pattern.")
    for integer in TestSequence:
        print(integer)
    print("Based on the integers above, what do you think the next integer will be?")
    user_answer = int(input(":"))
    return user_answer

def TestUserAnswer():
    if user_answer == answer:
        print("Congratulations! You are correct!")
    else:
        print("Sorry, that's not right. Better luck next time.")

def PlayAgain():
    global play_game
    print("Would you like to play again?")
    play_again = input(":")
    if play_again in ("yes","Yes","y","Y"):
        play_game = True
    elif play_again in ("no","No","n","N"):
        play_game = False
        print("Alright, see you next time!")
    return play_game


if __name__ == "__main__":

    while play_game == True:
        SelectSequence()
        GetUserAnswer()
        TestUserAnswer()
        PlayAgain()
