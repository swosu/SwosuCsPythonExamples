import pandas as pd

def greedy_shortest_path(starting_city, df):

    # create a list of cities to visit
    current_path = [starting_city]

    # create a list of cities to visit
    cities_to_visit = list(range(1, 1 + city_count))
    cities_to_visit.remove(starting_city)
    print(f'cities to visit are {cities_to_visit}')

    current_city = starting_city

    # loop through the cities to visit
    while len(cities_to_visit) > 0:
        # find the distance to each of the cities to visit from the starting city
        
        # grab the row of distances from the current city
        distances = df.loc[df['City'] == current_city]
        print(f'distances are {distances}')


        # add the closest city to the current path
        #current_path.append(closest_city)

        # remove the closest city from the cities to visit
        #cities_to_visit.remove(closest_city)

    # add the starting city to the end of the current path
    #current_path.append(starting_city)

    # print the current path
    #print(f'current path after greedy is {current_path}')


if __name__ == '__main__':
    print('hello world')

    city_count = 6

    # Load the data
    file_name = str(city_count) + '.csv'
    print(f'file name is {file_name}.')
    file = open(file_name, 'r')


    
    # save the data into a data structure
    df = pd.read_csv(file)

    # print the data file without row numbers
    print(df.to_string(index=False))

    # loop through starting at all the cities for the greedy algorithm
    for starting_city in range(1, 1 + city_count):
        print(f'Starting city is {starting_city}')

        # create a list of cities to visit
        current_path = greedy_shortest_path(starting_city, df)


    print('So long and thanks for all the fish')