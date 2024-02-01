"""
as a seasoned python developer, make a text based dice game where two different fighting styles are competing. 
One is a faster, lighter attacker that can get in more hits per round. 
The other is a slower, but powerful attacker that has more damage when it does land a hit. 
Use D20 and D6 dice. 
Do a best of five battles to the death. Print off player stats after every hit. 
Use Object Oriented Code. 
Ask for two player names, one for each combatant. 
Ask each player to answer simple math questions to increase power of attacks. 
Let each player choose if they want to do speed attacks or power attacks. 
Speed attacks should be 10 of the D6 dice. Power attacks should be 3 of the D20 dice.
"""

"""
This implementation defines a Player class with attributes for the player's name, health, speed, and power. 
The attack method calculates the damage done by the player's attack, based on the attack type (speed or power)
 and the dice rolls. The answer_math_question method asks the player 
 a simple math question to increase their attack power.

The DiceGame class initializes two Player objects with their names, and then plays a best-of-five battle between
"""

import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.speed = 0
        self.power = 0
        
    def attack(self, opponent, is_speed_attack):
        if is_speed_attack:
            damage = sum([random.randint(1, 6) for _ in range(10)]) + self.speed
        else:
            damage = sum([random.randint(1, 20) for _ in range(3)]) + self.power
        opponent.health -= damage
        return damage
    
    def answer_math_question(self):
        # Ask the player a simple math question to increase their attack power
        # You can replace this with more challenging math questions if you like
        answer = input(f"{self.name}, what is 5+5? ")
        if answer == "10":
            self.speed += 2
            self.power += 5
            print(f"{self.name}'s attack power increased!")
        else:
            print(f"Sorry {self.name}, the answer is incorrect. Try again next round.")
            

class DiceGame:
    def __init__(self):
        self.player1 = Player(input("Enter player 1 name: "))
        self.player2 = Player(input("Enter player 2 name: "))
        
    def play(self):
        print("Let the battle begin!")
        for i in range(5):
            print(f"Round {i+1} - Fight!")
            p1_attack_type = self.get_attack_type(self.player1)
            p2_attack_type = self.get_attack_type(self.player2)
            p1_damage = self.player1.attack(self.player2, p1_attack_type == "speed")
            p2_damage = self.player2.attack(self.player1, p2_attack_type == "speed")
            self.print_player_stats(self.player1, p1_damage)
            self.print_player_stats(self.player2, p2_damage)
            if self.player1.health <= 0:
                print(f"{self.player1.name} has been defeated! {self.player2.name} is the winner!")
                return
            elif self.player2.health <= 0:
                print(f"{self.player2.name} has been defeated! {self.player1.name} is the winner!")
                return
        print("The battle is over, but both fighters are still standing! It's a tie!")
        

    def play attack_sounds(self):
        print("Bam! Pow! Wham!")


    def get_attack_type(self, player):
        attack_type = input(f"{player.name}, do you want to do a speed attack or a power attack? ")
        while attack_type.lower() not in ["speed", "power"]:
            attack_type = input(f"Invalid input. {player.name}, do you want to do a speed attack or a power attack? ")
        return attack_type.lower()
    
    def print_player_stats(self, player, damage):
        print(f"{player.name} attacked for {damage} damage!")
        print(f"{player.name} - health: {player.health}, speed: {player.speed}, power: {player.power}")
        

# Let's play the game!
game = DiceGame()
game.play()
