def calculate_points(rolls):
    points = 0
    die1, die2 = rolls
    
    if die1 == die2:
        # doubles
        points += 5
        if die1 == 1:
            # special penalty for snake eyes
            points -= 10
    elif die1 + die2 >= 8:
        # high roll bonus
        points += 3

    return points
