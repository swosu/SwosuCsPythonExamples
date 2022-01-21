from Artist import Artist

class Artwork:
    def __init__(self, title='None', year_created=0,\
     artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def print_info(self):
        self.artist.print_info()
        print('Title: %s, %d' % (self.title, self.year_created))
