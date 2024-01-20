my_animal1 = input("You get to choose three animals to add to the zoo! Enter your first choice:")
my_animal2 = input("Enter your second choice:")
my_animal3 = input("Choose one more animal:")
my_animals = [my_animal1, my_animal2, my_animal3]
their_animal1 = input("Enter your friend's first choice:")
their_animal2 = input("Enter your friend's second choice:")
lost_animal = input("Enter the last animal your friend chose:")
their_animals = [their_animal1, their_animal2]

our_zoo = my_animals + their_animals
print(our_zoo)
our_zoo.append(lost_animal)
print(our_zoo)
our_zoo[1] = lost_animal
print(our_zoo)
our_zoo.pop(1)
print(our_zoo)
our_zoo.pop(1)
print(our_zoo)

