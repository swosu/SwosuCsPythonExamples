

# Setting up a simple combat roll turn based game. going to play around with objects and classes

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.coins = 20
        self.inventory = {}
        self.__level = 1
        self.__exp = 0
        self.__math_exp = 0
        self.__max_hp = 100 + (100 * (self.__level - 1))

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

    def get_coin_count(self):
        return self.coins

    def give_math_experience(self, exp):
        self.__math_exp += exp
        if self.__math_exp >= 100:
            self.__level += 1
            self.__math_exp = 0
            print('Congratulations! You have leveled up.')
            print('You are now level: ', self.__level)

    def reset_hp_to_max(self):
        self.hp = self.__max_hp
    
    def spend_meal_at_home(self):
        self.inventory['meal'] -= 1

    def print_all_data(self):
        print('Name: ', self.name)
        print('Level: ', self.__level)
        print('Experience: ', self.__exp)
        print('Math Experience: ', self.__math_exp)
        print('Health Points: ', self.hp, '/', self.__max_hp)
        print('Coins: ', self.coins)
        print('Inventory: ', self.inventory)

class Home:
    def __init__(self, player):
        self.player = player

    def rest(self):
        if self.player.inventory['meal'] > 0:
            self.player.spend_meal_at_home()
            self.player.reset_hp_to_max()
            print('You have eaten a meal and are fully rested.')
        else:
            print('You do not have a meal to eat. You should go to the store and buy one.')
            self.player.coins += 1
            
class Store:
    def __init__(self, player):
        self.items = {
            'sword': 10,
            'shield': 5,
            'potion': 5,
            'meal': 3
        }
        self.player = player

    def print_shop_menu(self):
        print('Shop Menu:')
        # put an item number, item name, and cost on each line
        
    def print_options(self):
        option_list = ['1: Print shop menu', '2. Check your inventory',
        '3. Equip an item', '4. Unequip an item', '5. Exit shop']
        print('Please enter the numeral for the option of your choice.')
        # print shop option list



    def show_items(self):
        print('you feel your pockets, and quckly add up your stash')
        print('you have ', self.player.get_coin_count(), ' coins in your pocket.')
        print('The shop keeper greets you with a warm smile.')
        print('\"Welcome to the store. Here are the items available for purchase:\"')

        while True:
            self.print_shop_menu()
            self.print_options()
            user_selection = input('Enter the numeral for the option of your choice: ')


        

    def buy_item(self, item):
        # do they have enough coins?
        if self.player.coins < self.items[item]:
            print('You do not have enough coins to buy this item.')
            print('You need to go to work and earn some coins.')
        elif item in self.player.inventory:
            print('You already have this item.')
        elif item in self.items:
            self.player.coins -= self.items[item]
            self.player.inventory[item] = 1
            print('You have purchased a ', item)
        else:
            print('That item is not available for purchase.')

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

    print('now that you have a couple of coins you can go to the store and buy some items.')
    store = Store(player)
    store.show_items()
    store.buy_item('meal')
    player.print_all_data()

    print('now that you have purchased a meal, you can go home to rest')

    home  = Home(player)
    home.rest()
    player.print_all_data()

    print('we need a few more coins to purcase a sword, shield, two potions, and a meal.')
    print('This is 23 coins')

    while 23 >= player.get_coin_count():
        math_quiz.ask_question()

    print('okay, back to the store once more...')
    store.show_items()

    

