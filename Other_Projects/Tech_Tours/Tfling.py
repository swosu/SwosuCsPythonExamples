print ('hello world')

# Ask for user's name
name = input("What is your name? ")
print("Hello, " + name + "! Let's play T-Fling!")

print('Here are your possible attacks: ')

attacks = ['T', 'Whirlpool', 'Splash', 'Fireball', 'Tsunami', 'Thunderbold']

# give the attack and give it an index number
for i in range(len(attacks)):
    print(i, attacks[i])

# ask the user to choose an attack
attack = input("Choose an attack: ")



# give the user a choice of attacks.