"""
Write a program that takes in a line of text as input, 
and outputs that line of text in reverse. 
The program repeats, 
ending when the user enters "Done", "done", or "d" for the line of text.
"""
message_1 = 'Please enter a line of text and press enter.'
message_2 = 'Please enter "Done", "done", or "d" to end the program.'
list_of_user_text = []
while True:
    print(message_1, '\n', message_2)
    line_of_text = input('\n: ')
    print('you entered: ', line_of_text)
    if line_of_text == 'Done' or line_of_text == 'done' or line_of_text == 'd':
        print('So this is how it ends...')
        break
    else:
        list_of_user_text.append(line_of_text)
        print('our list of text now contains: ', list_of_user_text)

print('now we reverse the text and print it off.')

"""
for item in list_of_user_text:
    print(item[::-1])
    print('')
"""

for index in range(len(list_of_user_text)):
    print(list_of_user_text[index][::-1])
    print('')