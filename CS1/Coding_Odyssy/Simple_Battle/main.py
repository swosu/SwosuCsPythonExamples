

# Setting up a simple combat roll turn based game. going to play around with objects and classes

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.coins = 5
        self.inventory = []
        self.__level = 1
        self.__exp = 0
        self.__math_exp = 0

    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.__level

    def pay_coin_charge(self, charge):
        if self.coins < charge:
            print('You do not have enough coins to play the math quiz.')
            print('You need to go to work and earn some coins.')
            self.coins = 1
        else:
            self.coins -= charge

    def give_math_experience(self, exp):
        self.__math_exp += exp
        if self.__math_exp >= 100:
            self.__level += 1
            self.__math_exp = 0
            print('Congratulations! You have leveled up.')
            print('You are now level: ', self.__level)

    def print_all_data(self):
        print('Name: ', self.name)
        print('Level: ', self.__level)
        print('Experience: ', self.__exp)
        print('Coins: ', self.coins)
        print('Inventory: ', self.inventory)


class Math_Quiz:
    def __init__(self, player):
        self.data = []
        self.player = player

    def ask_question(self):
        level = self.player.get_level()
        self.player.pay_coin_charge(1)

        print('player level is: ', level)
        print('player coins: ', self.player.coins)
        
        num1 = random.randint(1, 10*level)
        num2 = random.randint(1, 10*level)

        answer = num1 + num2

        question = f'What is {num1} + {num2}?'
        print(question)
        response = int(input('Enter your answer: '))
        if response == answer:
            print('Correct! You have earned 5 coins.')
            self.player.coins += (5*level)
            self.player.give_math_experience(1)
        else:
            print('Incorrect. The correct answer is: ', answer)

    

    

if __name__ == '__main__':
    
    
    
    #print('Well met, traveler! Welcome to a simple adventure.')
    #print('Let us begin...')
    #print('How should we address you?')
    #name = input('Enter your name and please press enter: ')

    name = 'Player1'
        

    # Create a player object
    player = Player(name)

    """
    print(f'Welcome, {player.get_name()}! Let us begin our journey.')
    print('because this is for school, we are going to have a way to use your brain.')
    print('you can go to work and earn money.')
    print('you get money when you get a correct answer')
    print('it costs one coin to play the math quiz')
    print('a correct answer will give you 5 coins')
    """
    
    math_quiz = Math_Quiz(player)

    math_quiz.ask_question()

    player.print_all_data()

    

