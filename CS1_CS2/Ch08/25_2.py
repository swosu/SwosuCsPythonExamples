user_input = input('please paste in your list')
user_sentence = user_input.split()

for index in range(len(user_sentence)):
    print('{} {}'.format(user_sentence[index],\
    user_sentence.count(user_sentence[index])))
