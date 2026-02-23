import random
from collections import Counter

def compare_rolls(trials=10000000):
    two_dice_results = []
    single_gen_results = []

    for _ in range(trials):
        # Method 1: Two independent 6-sided dice
        roll_1 = random.randint(1, 6)
        roll_2 = random.randint(1, 6)
        two_dice_results.append(roll_1 + roll_2)

        # Method 2: One random call between 2 and 12
        single_gen_results.append(random.randint(2, 12))

    # Count the frequencies
    stats_two_dice = Counter(two_dice_results)
    stats_single_gen = Counter(single_gen_results)

    print(f"{'Value':<8} | {'Two Dice %':<12} | {'Single Gen %':<12}")
    print("-" * 40)
    
    for i in range(2, 13):
        p1 = (stats_two_dice[i] / trials) * 100
        p2 = (stats_single_gen[i] / trials) * 100
        print(f"{i:<8} | {p1:<12.2f} | {p2:<12.2f}")

compare_rolls()