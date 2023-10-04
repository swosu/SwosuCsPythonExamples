print('hello')

while True:
    print('inside the while loop.')
    print('enter q to quit.')
    user_input = input('Enter a string: ')
    print('you entered: ', user_input)

    if 'q' in user_input:
        break
    # reverse the string
    reverse_string = ''
    for our_string_position in range(len(user_input)-1, -1, -1):
        reverse_string += user_input[our_string_position]
    else: 
        print('done with the for loop')
    print('reverse string: ', reverse_string)

print('goodbye')