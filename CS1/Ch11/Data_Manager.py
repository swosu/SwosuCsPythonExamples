class Data_Manager:
    def __init__(self):
        self.data = []

    def load_user_inputs(self):
        self.set_artist_name()
        self.set_artist_birth_year()
        self.set_artist_death_year()
        self.set_title()
        self.set_year_created()

    # Setters
    def set_artist_birth_year(self):
        self.birth_year = input('what year was the artist born? ')

    def set_artist_name(self):
        self.name = input('what is the artist name you want? ')

    def set_artist_death_year(self):
        self.death_year = input('what year was the artist died? ')

    def set_title(self):
        self.title = input('what was the name of the work? ')

    def set_year_created(self):
        self.year_created = input('what year was the artwork created? ')

    # Getters
    def get_artist_name(self):
        return self.name

    def get_artist_birth_year(self):
        return self.birth_year

    def get_artist_death_year(self):
        return self.death_year

    def get_title(self):
        return self.title

    def get_year_created(self):
        return self.year_created
