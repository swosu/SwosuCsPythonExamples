import random

def get_user_dice_input():
    print('you are going to give us your dice numbers')
    dice = []
    for value in range(5):
        your_number = input(f'please enter die number {value+1}.')
        print(f'you entered {your_number}.')
        dice.append(int(your_number))
    print(dice)
    return dice

# Find highest score
def find_high_score(values):
    high_score = 0
    score = check_three_of_kind(values)
    if score > high_score:
        high_score = score

    score = check_four_of_kind(values)
    if score > high_score:
        high_score = score

    score = check_five_of_kind(values)
    if score > high_score:
        high_score = score

    score = check_full_house(values)
    if score > high_score:
        high_score = score

    print('checking singles loop')
    for val in range(1, 7):
        print(f'value is {val}.')
        score = check_singles(values, val)
        if score > high_score:
            high_score = score

    score = check_straight(values)
    if score > high_score:
        high_score = score

    return high_score

# Add all occurences of goal value
def check_singles(dice, goal):
    score = 0

    for i in range(len(dice)):
        if dice[i] == goal:
            score += goal

    print(f'score from check two of a kind {score}. \nThis is called a single pair')
    return score

# Check for three of a kind (score = 30)
def check_three_of_kind(dice):
    score = 0

    # Check for three options
    if dice[0] == dice[2]:
        score = 30
    elif dice[1] == dice[3]:
        score = 30
    elif dice[2] == dice[4]:
        score = 30

    print(f'score from check three of a kind {score}.')
    return score

# Check for four of a kind (score = 40)
def check_four_of_kind(dice):
    score = 0

    # Check for two options
    if dice[0] == dice[3] or dice[1] == dice[4]:
        score = 40

    print(f'score from check four of a kind {score}.')
    return score

# Check for five of a kind (score = 50)
def check_five_of_kind(dice):
    score = 0

    # Check for one option
    if dice[0] == dice[4]:
        score = 50

    print(f'score from check five of a kind {score}.')
    return score

# Check for full house (score = 35)
def check_full_house(dice):
    score = 0

    # Check for pattern 2,2,4,4,4
    if dice[0] == dice[1] and dice[2] == dice[4]:
        score = 35;

    # Check for pattern 2,2,2,4,4
    if dice[0] == dice[2] and dice[3] and dice[4]:
        score = 35;

    print(f'score from check full house {score}.')
    return score

# Check for straight (score = 45)
def check_straight(dice):
    score = 0

    # Check first three dice and then last two dice
    if dice[0] + 1 == dice[1] and dice[1] + 1 == dice[2]:
        if dice[2] + 1 == dice[3] and dice[3] + 1 == dice[4]:
            score = 45
    print(f'score from check straight {score}.')
    return score

if __name__ == '__main__':  # Do not modify
    # Fill array with five dice from input
    dice_roll = []
    number_of_dice = 5

    for roll in range(number_of_dice):
        dice_roll.append(random.randint(1, 6))

    print(dice_roll)
    high_score = 0
    #dice = [int(val) for val in input("Input die values").split()]
    dice = get_user_dice_input()
    # Place dice in ascending order
    #dice_roll.sort()
    dice.sort()

    # Find high score and output
    #high_score = find_high_score(dice_roll)
    high_score = find_high_score(dice)

    print("High score:", high_score)
