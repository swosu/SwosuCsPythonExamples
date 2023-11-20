import os
import random

def load_distance_table(city_count):
    print('starting process to load distance table.')
    print('city count: ', city_count)

    # create csv file name to look for
    csv_file_name = 'distance_table_' + str(city_count) + '.csv'
    print('csv file name: ', csv_file_name)

    if os.path.isfile(csv_file_name):
        print('file exists')
        rows, cols = (city_count, city_count)
    
        # initilize distance table
        distance_table = [[0 for i in range(cols)] for j in range(rows)]
        # open file
        with open (csv_file_name, 'r') as f:
            # read file
            for row in f:
                # split file into list
                row_list = row.split(',')
                # remove new line character
                row_list[-1] = row_list[-1].strip()
                # convert list to int
                row_list = list(map(int, row_list))
                # add row to distance table
                distance_table.append(row_list)

        print('distance table loaded from the file: ', csv_file_name)
        
        # print distance table
        print('distance table: ')
        for row in distance_table:
            print(row)
        
        return distance_table
    else:
        print('file does not exist')
        
        # create distance table
        create_distance_table(city_count)

def create_distance_table(city_count):
    # set up our working variables
    rows, cols = (city_count, city_count)
    
    # initilize distance table
    distance_table = [[0 for i in range(cols)] for j in range(rows)]

    # populate distance table
    for column in range(city_count):
        for row in range(city_count):
            distance_table[column][row] = random.randint(1, city_count * 10)