from itertools import combinations_with_replacement 
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/
# Append-adds at last

import time
start_time = time.time()
number_of_donuts_to_pick_out = 10
file1 = open(f"Donuts Pick {number_of_donuts_to_pick_out} from 21 varieties.txt", "a")  # append mode


#varieties = ['plain', 'chocolate', 'strawberry']

varieties = ['plain', 'chocolate', 'strawberry', 'blueberry', 'chocolate with sprinkles'\
        'plain with sprinkles', 'powdered sugar', 'maple glaze', 'chocolate long john'\
        'raspberry filled maple long john', 'cream filled maple long john', 'twist',\
        'coconut donut', 'cinnamon twist', 'Cruller', 'old fashioned', 'Jelly Donut',\
        'Boston Cream Pie', 'Bear Claw', 'Pine Cone',\
        'German Chocolate Cake Donut', 'Cream Cheese Donut', 'Apricot filled donut']


flavor_index = 0
for flavor in varieties:
    flavor_index += 1
    print(f'# {flavor_index}: {flavor}')

#print(f'our varieties are: {varieties}')

donut_combinations = combinations_with_replacement(varieties, number_of_donuts_to_pick_out)

# Print the obtained combinations 
index = 0
for i in list(donut_combinations): 
    index += 1
    file1.write(f'# {index}:\t')
    #print(f'# {index}: ', end = '')
    #print (i) 
    file1.write(f'{i} \n')

stop_time = time.time()
elapsed_time = stop_time - start_time
file1.write(f'elapsed time in second: {elapsed_time}.\n')
file1.close() 