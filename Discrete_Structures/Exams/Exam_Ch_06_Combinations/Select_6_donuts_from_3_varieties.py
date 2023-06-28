from itertools import combinations_with_replacement 
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/



# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement([1, 2, 3], 2) 

# Print the obtained combinations 
for i in list(comb): 
    print (i) 

print('now we pick 3 with replacement')
# Get all combinations of [1, 2, 3] and length 3 
comb = combinations_with_replacement([1, 2, 3], 3) 

# Print the obtained combinations 
for i in list(comb): 
    print (i) 

#varieties = ['plain', 'chocolate', 'strawberry']


print(f'our varieties are: {varieties}')

# pick 6 donuts from 3 varieties with replacement.
donut_combinations = combinations_with_replacement(varieties, 6)

# Print the obtained combinations 
index = 0
for i in list(donut_combinations): 
    index += 1
    print(f'# {index}: ', end = '')
    print (i) 