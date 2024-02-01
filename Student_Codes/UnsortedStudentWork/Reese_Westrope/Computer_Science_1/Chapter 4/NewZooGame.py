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

    lost_animal_toggle = [lost_animal, 'lost']
    my_animal2_toggle = [my_animal2, 'found']

    def missing_lost(toggle, toggle2):
        while toggle[1] == 'lost':
            print("You need to find the ",toggle[0],".")
            print("Choose the number of the location you want to search from the following list:")
            print('(1)',toggle2[0],"cage \n(2) concession stand \n(3) storage shed")
            search = int(input(':'))
            if search == location:
                toggle[1] = 'found'
                print("Congratulations! You found the ",toggle[0],"! Your zoo is saved!")
        
            elif search == 1:
                escape = random.randint(1,2)
                if escape == 2:
                    toggle2[1] = 'lost'
                    print("Searching...")
                    print("Oh no! The ",toggle2[0],"escaped while you were searching! Maybe this zoo isn't such a great idea...")
                    while toggle2[1] == 'lost':
                        missing_mine(toggle2)
                else:
                    print("Searching...")
                    print("Looks like the ",toggle[0],"isn't here, don't give up!")
        
            elif search == 2:
                print("Searching...")
                print("Looks like the", toggle[0]," isn't here, try somewhere else!")

            elif search == 3:
                print("Searching...")
                print("Sorry, the ",toggle[0],"isn't here, keep looking!")

    def missing_mine(toggle2):
        print("You need to find the ",toggle2[0],".")
        print("Choose the number of the location you want to search from the following list:")
        print('(1)',lost_animal,"cage \n(2) concession stand \n(3) storage shed")
        search2 = int(input(":"))
        if search2 == location2:
            toggle2[1] = 'found'
            print("Congratulations! You found the ",toggle2[0],"! Now, get back to searching for the ",lost_animal)
        elif search2 == 1:
            print("Searching...")
            print("Looks like the",toggle2[0],"isn't here, try again!")
        elif search2 == 2:
            print('Searching...')
            print("Uh oh, looks like the",toggle2[0]," isn't here, don't give up!")
        elif search2 == 3:
            print("Searching...")
            print("Sorry, the ",toggle2[0]," isn't here, keep looking!")
        

    print("Oh no! The ",lost_animal," escaped while you were unloading!")
    missing_lost(lost_animal_toggle, my_animal2_toggle)   
 
else:
    print("You're no fun, I hope you change your mind!")


