import os
import pandas as pd
import numpy as np
import itertools



# for all csv files in the current directory, open each file and save it as a dataframe <distance_talbe>

# make a list of the files in the current directory
file_list = os.listdir()

# make a list of the csv files in the current directory
#csv_file_list = []
#for file in file_list:
#    if file.endswith('.csv'):
#        csv_file_list.append(file)

# print the names of the csv files
#for file in csv_file_list:
#    print(file)

# for each csv file in csv_file_list, open the file and save it as a dataframe
# the data frame should be named after the file name

# create a list of the data frames
#data_frame_list = []
#for file in csv_file_list:
#    data_frame_list.append(pd.read_csv(file))

# print the names of the data frames
#for data_frame in data_frame_list:
#    print(data_frame)

# set our city count
city_count = 4

# read in the data from 4.csv and save it as a dataframe
#df = pd.read_csv('4.csv')
df = pd.read_csv('4.csv', header=None)

print("df shape:", df.shape)
print(df)


# print the dataframe without row numbers
#print(df.to_string(index=False))

# print the dataframe with row numbers
#print(df)

# make a list of all possible paths through the 4 cities, visiting each city exactly once 
# and returning to the starting city
# the list should be a list of lists, where each list is a path through the 4 cities
# the list should be in the order of the cities in the csv file
# the list should be in alphabetical order

possible_path_list = []
perms = itertools.permutations([1, 2, 3, 4])

perms_list = [list(perm) for perm in perms]

for perm in perms_list:
    if perm[0] == 1:
        possible_path_list.append(perm)
    #print(perm)

# remove the lists that do not start with 1
possible_path_list = [path for path in possible_path_list if path[0] == 1]

print('possible_path_list: ')
for path in possible_path_list:
    print(path)

print('now we can calculate the distance for each path')
total_distance_list = []
total_distance = 0


# for each path in possible_path_list, calculate the distance of the path
# the distance is the sum of the distances between each city in the path

# work through each path one at a time and create a dictionary that has the path as the key and the distance as the value
# the dictionary should be named total_distance_dict
total_distance_dict = {}
for path in possible_path_list:
    total_distance = 0
    for i in range(len(path)-1):
        total_distance += df.iloc[path[i]-1, path[i+1]-1]
    total_distance += df.iloc[path[-1]-1, path[0]-1]
    total_distance_dict[tuple(path)] = total_distance
    total_distance_list.append(total_distance)

# print the dictionary of total distances
print('total_distance_dict: ')
for key, value in total_distance_dict.items():
    print(key, value)
    


#for i in range(4):
#    for j in range(4):
#        for k in range(4):
#            for l in range(4):
#                if i != j and i != k and i != l and j != k and j != l and k != l:
#                    possible_path_list.append([i, j, k, l])

# print the list of possible paths
#print(possible_path_list)
