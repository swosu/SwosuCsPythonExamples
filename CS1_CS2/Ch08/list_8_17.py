place_to_hold_our_numbers = []
while True:
    user_input = input('Enter a number to add to the list or enter q to quit: ')
    if user_input == 'q':
        break
    else:
        user_input = int(user_input)
        if 0 >= user_input:
            place_to_hold_our_numbers.append(user_input)

print('this is after our loop.')
print('our list before sorting::', place_to_hold_our_numbers)

place_to_hold_our_numbers.sort(reverse=True)

print('our list after sorting::', place_to_hold_our_numbers)

for individual_number in place_to_hold_our_numbers:
    print(individual_number, end=' ')