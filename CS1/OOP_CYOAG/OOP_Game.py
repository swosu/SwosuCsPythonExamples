import random

class Player:
  
    def __init__(self):
        self.__health = 100
        self.__damage = 10
        self.__name = ''
        self.__chance = 0

    def establish_name(self, player_number):
        self.__name = input(f'what is your name? {player_number}? ')

    def get_health(self):
        return self.__health

    def set_updated_health(self, damage):
        self.__health = self.__health - damage
    
    def calculate__random_attack(self):
        if 3 <= self.__chance:
            inflicted_damage = random.randint(0, 5 * self.__damage)
            print(f'{self.__name} yells, \"By the power of castle gray skull!!!\"')
            self.__chance = 0
        else:
            inflicted_damage = random.randint(0, self.__damage)

        if 3 >= inflicted_damage:
            print(f'{self.__name}, you suck, damage was {inflicted_damage}.')
        elif 8 < inflicted_damage :
            print(f'{self.__name}, good hit, damage was {inflicted_damage}.')
            self.__chance += 1
        else:
            print(f'{self.__name}, meh, damage was {inflicted_damage}.')
        return inflicted_damage

    def print_status(self):
        print(f'for player {self.__name}, health is {self.__health}.')

if __name__ == '__main__':
    one_object = Player()
    one_object.establish_name('player one')
    two_object = Player()
    two_object.establish_name('player two')

    while 0 < one_object.get_health() and 0 < two_object.get_health():

        one_object.set_updated_health(two_object.calculate__random_attack())
        two_object.set_updated_health(one_object.calculate__random_attack())
        one_object.print_status()
        two_object.print_status()

    print('the battle is over.')
    if one_object.get_health() > two_object.get_health():
        print('player one won')
    else:
        print('player two won.')



