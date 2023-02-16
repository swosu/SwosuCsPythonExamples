




# ask user name
name = input("What is your name? ")

print("Hello, " + name + "!")

if 3 == len(name):
    print("Your name is 3 letters long!")
    pet_choice = input("What is your favorite pet? Do you like cats or dogs? ")
    alien_choice = input("Do you believe in aliens? ")
    donut_count = input("How many donuts can you eat? ")
    parent_choice = input("Do you favor your mom or dad more? ")
    print(f'Hello {name}! ', end='')
    print(f'thank you for taking the time to answer my questions. ')
    print(f'I am happy to hear that you like {pet_choice}')
    print(f'I was suprised what you said about aliens. \" {alien_choice} \".')
    print(f'You can eat {donut_count} donuts? That is a lot of donuts!')
    print(f'You favor your {parent_choice} more? That is interesting.')
    print(f'{name} I hope you have a great day!')
    
    print("Your name is " + name + ", your favorite pet is " + pet_choice + 
          ", you believe in aliens, you can eat " + donut_count + 
          " donuts, and you favor your " + parent_choice + " more.")