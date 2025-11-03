# 04_methods_behavior.py
# Goal: Show that objects are more than just data containers — they can DO things.
#       Methods define behavior that belongs to the object.

class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        """Prints formatted information about the artist."""
        if self.birth_year >= 0 and self.death_year >= 0:
            date_info = f"({self.birth_year} to {self.death_year})"
        elif self.birth_year >= 0 and self.death_year < 0:
            date_info = f"({self.birth_year} to present)"
        else:
            date_info = "(unknown)"
        print(f"Artist: {self.name} {date_info}")

    def is_alive(self):
        """Return True if the artist is alive (death_year < 0)."""
        return self.birth_year >= 0 and self.death_year < 0

    def age_in_year(self, year):
        """
        Calculate the artist's age in a given year.
        NOTE: Returns None if birth_year is unknown.
        """
        if self.birth_year < 0:
            return None
        # If artist has died, cap age at death year
        end_year = min(year, self.death_year) if self.death_year >= 0 else year
        return end_year - self.birth_year


class Artwork:
    def __init__(self, title="unknown", year_created=-1, artist=None):
        self.title = title
        self.year_created = year_created
        self.artist = artist if artist is not None else Artist()

    def print_info(self):
        """Prints information about the artwork and its artist."""
        self.artist.print_info()
        print(f"Title: {self.title}, {self.year_created}")

    def years_since_created(self, current_year):
        """Return how many years have passed since the artwork was created."""
        if self.year_created < 0:
            return None
        return current_year - self.year_created


if __name__ == "__main__":
    # Create an artist and artwork
    artist1 = Artist("Pablo Picasso", 1881, 1973)
    artwork1 = Artwork("Three Musicians", 1921, artist1)

    # Methods that DO things
    artwork1.print_info()
    print(f"Years since created (in 2025): {artwork1.years_since_created(2025)}\n")

    artist2 = Artist("Brice Marden", 1938, -1)
    artwork2 = Artwork("Distant Muses", 2000, artist2)
    artwork2.print_info()
    print(f"Is {artist2.name} alive? {artist2.is_alive()}")
    print(f"Age of {artist2.name} in 2025: {artist2.age_in_year(2025)}")
