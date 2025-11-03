"""
Define the Artist class in Artist.py with a constructor to initialize an artist's information. 
The constructor should by default initialize 
the artist's name to "unknown" and 
the years of birth and death to -1.

Define the Artwork class in Artwork.py 
with a constructor to initialize an artwork's information. 
The constructor should by default initialize 
the title to "unknown", 
the year created to -1, and 
the artist to use the Artist default constructor parameter values. 

Add an import statement to import the Artist class.

Add import statements to main.py to import the Artist and Artwork classes.
"""

class Artist():
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year


    def __repr__(self):
        return f"Artist:{self.name} ({self.birth_year} to {self.death_year})"

class Artwork():
    def __init__(self, title="unknown", year_created=-1, artist=Artist()):
        self.title = title
        self.year_created = year_created
        self.artist = artist

    def __repr__(self):
        return f"Title: {self.title}, {self.year_created}"

if __name__ == '__main__':
    """
    Ex: If the input is:

Pablo Picasso
1881
1973
Three Musicians
1921
the output is:

Artist: Pablo Picasso (1881 to 1973)
Title: Three Musicians, 1921
    """
    artist_name = "Pablo Picasso"
    artist_birth_year = 1881
    artist_death_year = 1973
    artwork_title = "Three Musicians"
    artwork_year_created = 1921

    artist = Artist(artist_name, artist_birth_year, artist_death_year)
    artwork = Artwork(artwork_title, artwork_year_created, artist)
    print(artist)
    print(artwork)