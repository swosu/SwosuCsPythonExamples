import os
import random

def load_distance_table(city_count):
    print('starting process to load distance table for a city count of: ', city_count)

    # create csv file name to look for
    csv_file_name = 'distance_table_' + str(city_count) + '.csv'
    print('starting to look for a csv file name: ', csv_file_name)

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print('our path is: ', dir_path)
    dir_list = os.listdir(dir_path)
    print("Files and directories in '", dir_path, "' :")
    print('our directory list is: ', dir_list)
 
    

    # check if file exists
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
        # try to load distance table again
        load_distance_table(city_count)

def create_distance_table(city_count):
    # set up our working variables
    rows, cols = (city_count, city_count)
    
    # initilize distance table
    distance_table = [[0 for i in range(cols)] for j in range(rows)]

    # populate distance table
    for column in range(city_count):
        for row in range(city_count):
            distance_table[column][row] = random.randint(1, city_count * 10)

    # print distance table
    print('distance table: ')
    for row in distance_table:
        print(row)

    # create csv file name to write to
    csv_file_name = 'distance_table_' + str(city_count) + '.csv'

    # print file name
    print('saving new csv file as: ', csv_file_name)

    # open file
    with open(csv_file_name, 'w') as f:
        # write to file
        for row in distance_table:
            f.write(','.join(str(column) for column in row) + '\n')

    print('new csv file saved as.', csv_file_name)
    