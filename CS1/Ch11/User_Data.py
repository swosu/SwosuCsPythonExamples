class User_Data:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__(self):
        self.user_artist_name = input('input artist name: ')
        self.user_birth_year = int(input('inpu birth year: '))
        self.user_death_year = int(input('input death year: '))
        self.user_title = input('what is the name of the work: ')
        self.user_year_created = int(input('when was this done?: '))

    def load_data():
        self.user_artist_name = input('second input artist name: ')
        self.user_birth_year = int(input('second inpu birth year: '))
        self.user_death_year = int(input('second input death year: '))
        self.user_title = input('second what is the name of the work: ')
        self.user_year_created = int(input('second when was this done?: '))

    def get_user_artist_name(self):
        return self.user_artist_name
