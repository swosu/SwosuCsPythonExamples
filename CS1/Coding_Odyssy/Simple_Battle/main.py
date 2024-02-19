

# Setting up a simple combat roll turn based game. going to play around with objects and classes
DEBUG = True

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack = 10
        self.defense = 5
        self.money = 5
        self.inventory = []
        self.level = 0

    def get_name(self):
        return self.name




if __name__ == '__main__':
    
    
    if DEBUG:
        name = 'Player1'
    else:
        print('Well met, traveler! Welcome to a simple adventure.')
        print('Let us begin...')
        print('How should we address you?')
        name = input('Enter your name and please press enter: ')

    # Create a player object
    player = Player(name)

    print(f'Welcome, {player.get_name()}! Let us begin our journey.')

    

