'''As a player, I want to see the rules so that I can refresh my memory or learn how to play the game
As a Yahtzee player, I want to have five dice to play the game. 
As a player, I want to choose which dice to keep so I can keep my score, and be able to reroll only certain die, so I can be strategic in my turns.
I want the ability to roll any of the dice up to 3 times
'''

import random

def rulesDisplay():
    print("Welcome to Yahtzee! \nHow to play: \nOn each turn, roll the dice up to 3 times to achieve the highest scoring combo. After you \nfinish rolling, you must put a score in for one of the 13 categories. The game ends when \nall players have filled in their scorecard. To decide who goes first, each player in \nturn rolls all 5 dice. the player with the highest combined score goes first, and the play \npasses to the left. The player with the highest total score wins! \nEnjoy!!")

def rollDice(diceNum):
    return [random.randint(1, 6) for _ in range(diceNum)]

def displayDice(dice):
    print(f'current dice:{dice}')

def diceToKeep(dice):
    displayDice(dice)
    keepInput = input("enter the indices of the dice to keep (separated by spaces): ")
    keepIndex = [int(inp) - 1 for inp in keepInput.split()]
    diceKept = [dice[index] for index in keepIndex]
    return diceKept

# print(rollDice(5))
# print(diceToKeep())

# example scoring definitions
def calcThreeofaKind(dice):
    decendingDice = sorted(dice, reverse=True)

    for die in range(len(decendingDice) - 2):
        if decendingDice[die] == decendingDice[die + 1] == decendingDice[die + 2]:
            return sum(decendingDice[die:die + 3])
    return 0

def yahtzee():
    rulesDisplay()

    totalScore = 0
    numRounds = 13

    for numRound in range(1, numRounds+1):
        print(f'Round number {numRound}')

        dice = rollDice(5)
        for rollNum in range(1, 4):
            keepDice = diceToKeep(dice)
            if rollNum < 3:
                rerollIndices = [index for index in range(5) if index not in keepDice]
                newDice = rollDice(len(rerollIndices))
                for value, index in enumerate(keepDice):
                    dice[index] = newDice[value]
                    #getting a little confused here on what i was doing lol
            else:
                print("Final roll.")
        
        roundScore = calcThreeofaKind(dice)

        print(f'round score for {numRound}: {roundScore}')
        totalScore += roundScore
    print(f'Game over! Total Score: {totalScore}')