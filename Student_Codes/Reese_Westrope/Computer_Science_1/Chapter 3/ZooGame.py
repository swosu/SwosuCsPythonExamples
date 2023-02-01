#refactor code using functions

import random
start = input("Would you like to start a zoo with your friend? (y/n):")
if start == 'y':

    my_animal1 = input("You get to choose three animals to add to the zoo! Enter your first choice:")
    my_animal2 = input("Enter your second choice:")
    my_animal3 = input("Choose one more animal:")

    their_animal1 = input("Enter your friend's first choice:")
    their_animal2 = input("Enter your friend's second choice:")
    lost_animal = input("Enter the last animal your friend chose:")

    location = random.randint(1,3)
    location2 = random.randint(1,3)

    print("Oh no! The ",lost_animal," escaped while you were unloading!")
    lost_animal_toggle = 'lost'
    my_animal2_toggle = 'found'

    while lost_animal_toggle == 'lost':
        while my_animal2_toggle == 'lost':
                print("You need to find the ",my_animal2,".")
                print("Choose the number of the location you want to search from the following list:")
                print('(1)',lost_animal,"cage \n(2) concession stand \n(3) storage shed")
                search2 = int(input(":"))
                if search2 == location2:
                    my_animal2_toggle = 'found'
                    print("Congratulations! You found the ",my_animal2,"! Now, get back to searching for the ",lost_animal)
                elif search2 == 1:
                    print("Searching...")
                    print("Looks like the",my_animal2,"isn't here, try again!")
                elif search2 == 2:
                    print('Searching...')
                    print("Uh oh, looks like the",my_animal2," isn't here, don't give up!")
                elif search2 == 3:
                    print("Searching...")
                    print("Sorry, the ",my_animal2," isn't here, keep looking!")
        print("Choose the number of the location you want to search from the following list")
        print("(1)",my_animal2,"cage\n(2) concession stand \n(3) storage shed")
        search = int(input(':'))
        
        if search == location:
            lost_animal_toggle = 'found'
            print("Congratulations! You found the ",lost_animal,"! Your zoo is saved!")

       
        elif search == 1:
            escape = random.randint(1,2)
            if escape == 2:
                my_animal2_toggle = 'lost'
                print("Searching...")
                print("Oh no! The ",my_animal2,"escaped while you were searching! Maybe this zoo isn't such a great idea...")
            else:
                print("Searching...")
                print("Looks like the ",lost_animal,"isn't here, don't give up!")

        
        elif search == 2:
            print("Searching...")
            print("Looks like the", lost_animal," isn't here, try somewhere else!")

        elif search == 3:
            print("Searching...")
            print("Sorry, the ",lost_animal,"isn't here, keep looking!")


else:
    print("You're no fun, I hope you change your mind!")