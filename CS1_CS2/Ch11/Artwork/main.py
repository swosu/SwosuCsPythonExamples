# Add import statements to main.py to import the Artist and Artwork classes.
from Artist import Artist
from Artist import Artwork

# creat a test case that prints off the default values for the Artist and Artwork classes

# Create an Artist object with the default values
artist = Artist()
# Print the Artist object
print(artist)

# now we want to ask the user for the 
# #artist's name, 
# birth year, and 
# death year
# the name of the piece
# the year the piece was created

# Ask the user for the artist's name
artist_name = input("Enter the artist's name: ")
# Ask the user for the artist's birth year
artist_birth_year = int(input("Enter the artist's birth year: "))
# Ask the user for the artist's death year
artist_death_year = int(input("Enter the artist's death year: "))
# Ask the user for the title of the artwork
artwork_title = input("Enter the title of the artwork: ")
# Ask the user for the year the artwork was created
artwork_year_created = int(input("Enter the year the artwork was created: "))
# Create an Artist object with the user's input
artist = Artist(artist_name, artist_birth_year, artist_death_year)
# Create an Artwork object with the user's input
artwork = Artwork(artwork_title, artwork_year_created, artist)
# Print the Artwork object
print(artwork)
# print the artist object
print(artist)


