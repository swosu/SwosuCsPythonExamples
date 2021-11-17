class Data_Manager:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__(self):
        self.data = []

    def set_artist_name(self):
        self.name = input('what is the artist name you want? ')

    def get_artist_name(self):
        return self.name

    def set_artist_birth_year(self):
        self.birth_year = input('what year was the artist born? ')

    def get_artist_birth_year(self):
        return self.birth_year

    def set_artist_death_year(self):
        self.death_year = input('what year was the artist died? ')

    def get_artist_death_year(self):
        return self.death_year

    # name of artwork
    def set_title(self):
        self.title = input('what was the name of the work? ')

    def get_title(self):
        return self.title

    # Year artwork created
    def set_year_created(self):
        self.year_created = input('what year was the artwork created? ')

    def get_year_created(self):
        return self.year_created
