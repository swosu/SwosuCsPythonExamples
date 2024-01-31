'''As a player, I want to see the rules so that I can refresh my memory or learn how to play the game
As a Yahtzee player, I want to have five dice to play the game. 
As a player, I want to choose which dice to keep so I can keep my score, and be able to reroll only certain die, so I can be strategic in my turns.
I want the ability to roll any of the dice up to 3 times
'''

import random

def rulesDisplay():
    print("Welcome to Yahtzee! \nHow to play: \nOn each turn, roll the dice up to 3 times to achieve the highest scoring combo. After you \nfinish rolling, you must put a score in for one of the 13 categories. The game ends when all players have filled in their scorecard. \nTo decide who goes first, each player in turn rolls all 5 dice. the player with the highest combined score goes first, and the play passes \nto the left. The player with the highest total score wins! \nEnjoy!!")

def rollDice(diceNum):
    return [random.randint(1, 6) for num in range(diceNum)]

def displayDice(dice):
    print(f'current dice:{dice}')

def diceToKeep(dice):
    displayDice(dice)
    keepInput = input("enter the index of the dice to keep: ")
    keepIndex = [int(inp) - 1 for inp in keepInput]
    diceKept = [dice[index] for index in keepIndex]
    return diceKept

def yahtzee():
    rulesDisplay()

    score = 0
    numRounds = 13

    for numRound in range(1, numRounds+1):
        print(f'Round number {numRound}')

        dice = rollDice(5)
        for rollNum in range(1, 4):
            keepDice = diceToKeep(dice)
            if rollNum < 3:
                reroll = [die for index, die in enumerate(dice) if index not in keepDice]
                newDice = rollDice(len(reroll))
                for value, index in enumerate(keepDice):
                    dice[index] = newDice[value]
                    #getting a little confused here on what i was doing lol
                    
            else:
                print("Final roll.")
        
        print(f'Final Dice: {dice}')

