from itertools import combinations_with_replacement

if __name__ == '__main__':
    print("Hello, welcome to our donut picker")
    #https://www.geeksforgeeks.org/permutation-and-combination-in-python/

    #comb = combinations_with_replacement(['glazed', 'chocolate', 'maple'], 6)
    comb = combinations_with_replacement(['glazed', 'chocolate', 'maple', \
    'maple nut',  'blueberry', 'cherry', 'strawlberry', 'hurts donut',  \
    'bear claw', 'bavarian', 'apracot filled', 'cherry filled', \
    'chocolate filled', 'twist', 'donut holes', 'chocolate sprinkled maples',\
     'pink with white sprinkles', 'white with pink srpinkles', \
     'chocolate with white sprinkles', 'old fashioned', 'cinnamon'], 12)

    # Print the obtained combinations
    count = 0
    for i in list(comb):
        #print (i)
        count += 1

    print(f'number of choices is: {count}.')
