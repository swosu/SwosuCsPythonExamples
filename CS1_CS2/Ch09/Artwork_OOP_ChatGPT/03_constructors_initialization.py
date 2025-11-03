# 03_constructors_initialization.py
# Goal: Teach constructors (__init__) and default initialization.

class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        """Initialize an Artist with default or provided values."""
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        """Display artist details in the specified format."""
        if self.birth_year >= 0 and self.death_year >= 0:
            date_info = f"({self.birth_year} to {self.death_year})"
        elif self.birth_year >= 0 and self.death_year < 0:
            date_info = f"({self.birth_year} to present)"
        else:
            date_info = "(unknown)"
        print(f"Artist: {self.name} {date_info}")


class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        """Initialize Artwork with title, year, and an Artist object."""
        self.title = title
        self.year_created = year_created
        # If no artist given, use a default Artist
        self.artist = artist if artist is not None else Artist()

    def print_info(self):
        """Display artwork details."""
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")


if __name__ == "__main__":
    # Example 1: Fully specified artist and artwork
    artist1 = Artist("Pablo Picasso", 1881, 1973)
    artwork1 = Artwork("Three Musicians", 1921, artist1)
    artwork1.print_info()
    print()

    # Example 2: Living artist
    artist2 = Artist("Brice Marden", 1938, -1)
    artwork2 = Artwork("Distant Muses", 2000, artist2)
    artwork2.print_info()
    print()

    # Example 3: Anonymous artist with defaults
    artwork3 = Artwork()
    artwork3.print_info()
