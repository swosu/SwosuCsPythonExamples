import time
import random

def num_enemies():
    enemies = random.randint(0,20)
    print(enemies)

def exit_screen():
    print("hello player, this is the exit screen. You chose to end the game. \nOr, you met an untimely and rather unfortunate death. \nGood bye, hope you enjoyed playing. :)")

def welcome_screen():
    print("Welcome to Phion")
    time.sleep(2)
    print("Surviving this planet will not be easy, there are many challenges you will face along your journey.")
    time.sleep(2)
    answer = input("Are you ready for the challenge? \nYes/No \n: ")
    if answer == "yes":
        print('Perfect, we will now ask a few questions.')
    time.sleep(2)
    Name = input("Firstly, what is your name? ")
    print(f'Hello {Name}, it is nice to have you on the ship.')
    time.sleep(2)
    answer = input('Now shall we begin the journey? \nYes/No \n: ')
    if answer == "yes":
        print('let us begin')
    elif answer == "No":
        print("okay, maybe some other time")
        exit_screen()

def game_start():
    global planet_quest
    time.sleep(2)
    print('we are approaching a newly found planet named Phion, would you like to see it?')
    planet_quest = input('yes/no/later \n: ')
    if planet_quest == "yes":
        print('you begin walking towards the deck of the transport ship, there are people everywhere and most of them, \njust like you, have decided they want to see this new planet as well.\n')
    elif planet_quest == "later":
        print('We ask that you begin making your way towards the mess-hall then.')
    elif planet_quest == "no":
        print('Maybe next time.')
        exit_screen()

def look_outside():
    print("You approach the mass of bodies clustered towards the ship's thick windows. \nFrom there, you can see the slight hue and slope of a blueish atmoshphere. \nUnder that, you can see a large green ocean, bordered with a faint outline of \nsandy brown, which you assume to be a desert. Suddenly, the ship's alarms \nblare throughout the corridors, causing people to fly into a panic. \nYou look back out of the window and find the the planet seems to be \ngetting closer at an alarmingly fast rate.")
    player_choice = input("What do you do? \nfind a drop-pod / stay in place \n: ")
    if player_choice == "find a drop-pod":
        print("You run out of the observasion deck, swerving your way through the halls and people. You find the large room with the drop-pods, each of which contains a survival kit, space-suit, and a sprouting plant. Except, there was only one drop-pod left as the re")
        drop_pod()
    elif player_choice == "stay in place":
        print("You remain rooted to the spot, unsure of what to do. Eventually, with the amount of people running out of the observation deck, you are pushed to the ground, where you meet your untimely demise.")

def mess_hall():
    print("boo")

def drop_pod():
    print("You strap yourself into the seat, and take a deep breath. the pod faces so the \nseat and window allow you to look around the pod-room. As you set the co-ordinates to the area the transport \nship was supposed to land, you look up to see a group of people run into the room. ")

if __name__ == "__main__":
    welcome_screen()
    game_start()
    if planet_quest == "yes":
        look_outside()
    # num_enemies()