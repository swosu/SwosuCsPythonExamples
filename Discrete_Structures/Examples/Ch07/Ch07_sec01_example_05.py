# https://codepad.co/snippet/python-draw-cards-dictionary-card-deck

import random
from random import randint
from datetime import datetime
random.seed(datetime.now())

suits = {
    0: 'Clubs',
    1: 'Diamonds',
    2: 'Hearts',
    3: 'Spades'
}

#print('here is our suits dictionary.')
#print(suits)
cards = {
    0: 'Ace',
    1: '2',
    2: '3',
    3: '4',
    4: '5',
    5: '6',
    6: '7',
    7: '8',
    8: '9',
    9: '10',
    10: 'Jack',
    11: 'Queen',
    12: 'King'
}

def draw_cards(num_of_cards, list_dealt=[]):
    list_dealt = []
    list_dealt *= 0
    for z in range(num_of_cards):
        x = randint(0,3) #random integer 0 to 3 to pick suit
        y = randint(0,12) #random integer 0 to 12 to pick card
        mycard = "{0} of {1}".format(cards[y],suits[x])
        #print('our next list item')
        #print(mycard)
        if mycard not in list_dealt:
            list_dealt.append(mycard)
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards,list_dealt)

    return list_dealt

number_of_hands = 0
keep_going = True
while(keep_going):
    mydraw = []
    mydraw *= 0
    mydraw = draw_cards(5) #call the function with the number of cards you want.
    number_of_hands += 1
    print('attemp number: ', number_of_hands)
    #print(' my draw ')
    print(mydraw)
    """
    i = 0
    for x in mydraw:
        i += 1
        if i == len(mydraw):
            print("...And your last card is the {0}".format(str(x)))
        else:
            print("You got the {0}".format(str(x)))
    """

    # Building kind counting dictionary
    kind_counting_dictionary = {}
    kind_counting_dictionary.clear()
    for x in mydraw:
        #print(str(x))
        kind_array = str(x).split()
        #print(kind_array)
        kind = kind_array[0]
        #print(kind)
        # https://www.geeksforgeeks.org/python-check-whether-given-key-already-exists-in-a-dictionary/
        if kind in kind_counting_dictionary.keys():
            kind_counting_dictionary[kind] += 1
        else:
            kind_counting_dictionary[kind] = 1

    print(kind_counting_dictionary)

    # did I have a pair?
    # https://www.w3schools.com/python/gloss_python_loop_dictionary_items.asp

    for kind in kind_counting_dictionary:
        if kind_counting_dictionary[kind] >= 3:
            print('WE HAD Three of a kind!')
            keep_going = False

print('odds of getting a three of a kind', (1.0 / number_of_hands)*100, '%')
