class Artist:
    def __init__(self, name, birth_year, death_year):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year
   
    def print_info(self):
        print(f"Artist: {self.name}, ({self.birth_year} to {self.death_year})")

      
class Artwork:
    def __init__(self, title, year_created, artist):
        self.title = title
        self.year_created = year_created
        self.artist = artist
    
    def print_info(self):
        print(f"Artwork: {self.title}, {self.year_created}")

if __name__ == "__main__":
    user_artist_name = input("What is your artist's name?\n")
    user_birth_year = int(input(f"What year was {user_artist_name} born?\n"))
    user_death_year = int(input(f"What year did {user_artist_name} die?\n"))
    user_title = input(f"What is the title of  your favorite artwork by {user_artist_name}?\n")
    user_year_created = int(input(f"What year did {user_artist_name} create {user_title}?\n"))

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    user_artist.print_info()

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()