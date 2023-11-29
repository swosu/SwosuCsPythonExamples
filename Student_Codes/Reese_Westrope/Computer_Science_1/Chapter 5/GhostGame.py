#name = input("Hello strange traveller, what is your name?\n")

start = input('Welcome. Your fate lies within your own hands from now on.\nLook at that blue glimmer, would you like to check it out? (y/n)\n')

while start == 'n':
    start = input("Here's another chance to chase the blue light. (y/n)")

delivery_truck = ''
minivan = ''
farm_truck = ''

stranded = True

if start == 'y':
    print("You wake up and look around. There's nothing but grass and a highway. The sun is so hot. You have to find a way to find people. \n You stick out a thumb in hopes that some kind bypasser will give you a ride into the city, but you are met with nothing but the wind caused by cars and trucks speeding past you.")
    while stranded == True:
        delivery_truck = input("Here comes a delivery truck slowing down to take an exit, would you like to try to jump on and hitch a ride? (y/n)\n")

        if delivery_truck == 'n':
            minivan = input("A minivan full of kids is pulling over to change their tire. While the exasperated father is changing the tire, you have a chance to sneak into the luggage-filled trunk. Do you take it? (y/n)\n")
            if minivan == 'n':
                farm_truck = input("A farm truck is passing by, and it's moving pretty slowly. Will you try to jump into the trunk to hitch a ride? (y/n)\n")

        if delivery_truck == 'y':
            stranded = False
        elif minivan == 'y':
            stranded = False
        elif farm_truck == 'y':
            stranded = False
    
    if delivery_truck == 'y':
        print("You squeeze in between two packages as the truck drives down the highway. After what seems like an eternity, it slows to a stop and you sneak out of the truck, only to turn and see the truck driver staring straight at you! He doesn't seem fazed... You look down at your hand, and see only a shimmering transparency. You stand in shock as it begins to dawn on you. You're a ghost!")
        from GhostGameEnid import *
        Enid_adventure()

    elif minivan == 'y':
        print("You're in Dallas now")
        from GhostGameDallas import *
    
    elif farm_truck == 'y':
        print("You're on the farm")