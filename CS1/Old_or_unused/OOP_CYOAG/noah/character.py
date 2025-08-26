import random
class Character:
    def __init__(self, identifier) -> None:
        #https://stackoverflow.com/questions/64933298/why-should-we-use-in-def-init-self-n-none
        self.identifier = identifier
        self.name = "Character"
        self.hp = 100
        self.attack = 10
        self.attack_range = 20
        self.hair_color = "black"
        self.speed = 10
        self.alive = True

    def print_name(self):
        #print('name before capitalize: ', self.name)
        self.name = self.name.title()
        #print('name after capitalize: ', self.name)
        print(self.name)

    def print_hp(self):
        print(self.hp)

    def calculate_attack(self):
        self.attack = random.randint(1, self.attack_range)

    def calculate_wound(self, attack):
        self.hp = self.hp - self.attack



player_1 = Character("Player 1")

print('our identifier is: ', player_1.identifier)
player_1.name = "bob"
print('our name is: ', end = '')
player_1.print_name()

our_name = 'steve the great'
our_name.capitalize()
print('our name is: ', our_name)

print('afere playing with the name function')
print(player_1.name)

player_2 = Character("Player 2")
print('our identifier is: ', player_2.identifier)

player_2.name = "joe"
print('our name is: ', end = '')
player_2.print_name()

#lets make joe and bob fight each other
#we will use the attack variable
#we will use the hp variable
#we will use the speed variable

while player_1.alive & player_2.alive:
    print('BATTLE')

    player_1.calculate_attack()
    player_2.calculate_attack()

    if random.random() > 0.5:
        player_1.calculate_wound(player_2.attack)

    else:
        player_2.calculate_wound(player_1.attack)

    if player_1.hp <= 0:
        player_1.alive = False
    
    if player_2.hp <= 0:
        player_2.alive = False

    # print off health for both players
    print('player 1 hp: ', player_1.hp)
    print('player 2 hp: ', player_2.hp)


if player_1.alive:
    print('player 1 wins')
elif player_2.alive:
    print('player 2 wins')
else:
    print('tie')