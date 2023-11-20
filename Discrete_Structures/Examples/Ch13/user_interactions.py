def ask_how_many_cities():
    try:
        number_of_cities = int(input("How many cities do you wish to enter? "))
    except ValueError:
        print("Please enter a number.")
        ask_how_many_cities()
    else:
        return number_of_cities
    
def respond_to_user_city_count(city_count):
    print("You have chosen to enter {} cities.".format(city_count))