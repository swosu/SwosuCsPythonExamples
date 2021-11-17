# TODO: Import Artist from Artist.py
from Artist import Artist

class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    #       (name, birth_year, death_year)
    def __init__(self, title='None', year_created=0, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print('Title: %s, %d' % (self.title, self.year_created))
