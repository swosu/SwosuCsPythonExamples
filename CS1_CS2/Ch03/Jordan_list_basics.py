my_flower_1 = input('please enter my flower 1 of 3: ')
my_flower_2 = input('please enter my flower 2 of 3: ')
my_flower_3 = input('please enter my flower 3 of 3: ')
print(f'you entered my flowers: {my_flower_1} {my_flower_2} {my_flower_3}.')

your_flower_1 = input('please enter your flower 1 of 2: ')
your_flower_2 = input('please enter your flower 2 of 2: ')
print(f'you entered your flowers: {your_flower_1} {your_flower_2}.')

their_flower_1 = input('please enter their flower 1 of 1: ')

print(f'you entered their flower: {their_flower_1}.')
my_list=[my_flower_1, my_flower_2, my_flower_3]
print(my_list)
your_list=[your_flower_1, your_flower_2]
print(your_list)
our_list=my_list + your_list
print(our_list)
our_list.append(their_flower_1)
print(our_list)
our_list.remove(my_flower_2)
print(our_list)
our_list.append(their_flower_1)
print(our_list)
