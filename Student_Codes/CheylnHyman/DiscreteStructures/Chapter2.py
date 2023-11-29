# the goal is to guess the number at the end of the sequence

sequences = [
[2,4,6,8,10,12],
[3,6,9,12,15,18],
[1, 2, 3, 4],
[10,20,30,40,50,60]
]

def game(list):
    guess = 0
    temp_list = list[0:5]
    target = list[5]

    while guess != target:
        print(temp_list)
        guess = int(input('Please enter a number at end of sequence: '))
        if guess == target:
            print('You got it!')
            exit()
        else:
            print('You missed it!')
            game(list)


choice = int(input('please enter a number between 1 and 4: '))

game(sequences[choice-1])




