place_to_hold_our_numbers = []

print('our list is::', place_to_hold_our_numbers)

user_input = 0
while True:
    user_input = input('Enter a number to add to the list or enter q to quit: ')
    if user_input == 'q':
        break
    else:
        place_to_hold_our_numbers.append(user_input)

print('this is after our loop.')
print('our list is::', place_to_hold_our_numbers)

# loop through all the numbers and make them floating point numbers
for index in range(len(place_to_hold_our_numbers)):
    print('our index is: ', index)
    initial_number = place_to_hold_our_numbers[index]
    print('intial value in the list: ', initial_number)
    place_to_hold_our_numbers[index] = float(initial_number)
    value_after_conversion = place_to_hold_our_numbers[index]
    print('after conversion, our value is: ' , value_after_conversion)

max_number = max(place_to_hold_our_numbers)
print('our max number was: ', max_number)

sum_of_our_number = sum(place_to_hold_our_numbers)
print('our sum was: ', sum_of_our_number)
how_many_numbers_we_have = len(place_to_hold_our_numbers)
print('we had this many numbers: ', how_many_numbers_we_have)

average_number = sum_of_our_number / how_many_numbers_we_have
print('our average was: ', average_number)