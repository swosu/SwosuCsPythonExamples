# Ask user how many cities they want to have
city_count = input('how many cities do you want to have? ')

print('you want to have ' + city_count + ' cities')

# look for a csv file that matches that city count. 
# if it doesn't exist, create it.
# if it does exist, read it in and use it.

import os
csv_filename = 'cities_' + city_count + '.csv'
if os.path.isfile(csv_filename):
    print('file exists')
    #load the distance table
    distance_table = []
    with open(csv_filename, 'r') as f:
        for line in f:
            distance_table.append(line.strip().split(','))

    # print distance table

    for row in distance_table:
        print(row)
    
    #print this was loaded from the file.
    print('this was loaded from the file ' + csv_filename)

else:
    print('no file exists called ' + csv_filename)
    #create the distance table
    # distances should range from 1 to 10*city_count
    import random
    distance_table = []
    for i in range(0, int(city_count)):
        distance_table.append([])
        for j in range(0, int(city_count)):
            distance_table[i].append(random.randint(1, 10*int(city_count)))
    # overwrite the distance 0 to values along the diagonal so that the distance from 
    # a city to itself is 0
    for i in range(0, int(city_count)):
        distance_table[i][i] = 0
    # print distance table in such a way that all the columns of numbers line up straight.
    # This should involve adding spaces before single digit numbers
    for row in distance_table:
        print(row)
    
    # save the distance table
    with open(csv_filename, 'w') as f:
        for row in distance_table:
            f.write(','.join(str(x) for x in row) + '\n')


# use a brute force method to check every hamilton path through the
# distance table and find the shortest one.

# start with a path that visits the cities in order
current_path = []
for city in range(0, int(city_count)):
    current_path.append(city)

# print the current path
print('current path: ' + str(current_path))

# calculate the total distance of the current path
# be sure to include the distance going from the last city to the first city

total_distance = 0
for i in range(0, int(city_count)):
    total_distance += int(distance_table[current_path[i-1]][current_path[i]])
total_distance += int(distance_table[current_path[-1]][current_path[0]])

# print the total distance
print('total distance: ' + str(total_distance))

# loop through all the permutations of the current path
# and find the shortest one

# generate a list of all the permutations of each path
import itertools
all_paths = list(itertools.permutations(current_path))

# remove all the repeats where it is the same path, but starting at a different city
# this is the same as removing all the paths that start with a city other than 0
# and end with a city other than 0
# so remove all the paths that start with a city other than 0

# loop through all the paths
for path in all_paths:
    # if the path starts with a city other than 0
    if path[0] != 0:
        # remove the path
        all_paths.remove(path)

# print all the paths
for path in all_paths:
    print(path)

# loop through all the paths and calculate the total distance of each one
# print these resluts to a results csv file that indicates the city count in the file name.
# the results csv file should have the following columns:
# path, total distance



