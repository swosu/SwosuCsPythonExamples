while True:
    print('enter q to quit.')
    user_input = input('Enter a string: ')
    if 'q' in user_input:
        break
    else:
        #print reversed user input
        #print('reversed string: ' + user_input[::-1])
        print('reversed string: ' + ''.join(reversed(user_input)))