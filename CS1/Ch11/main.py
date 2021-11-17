# TODO: Add import statement
from Artist import Artist
from Artwork import Artwork
from Data_Manager import Data_Manager

if __name__ == "__main__":
    #print('Hey there.')
    user_inputs = Data_Manager()
    #print('and now you have an object')
    user_inputs.set_artist_name()
    user_artist_name = user_inputs.get_artist_name()
    user_inputs.set_artist_birth_year()
    user_birth_year = int(user_inputs.get_artist_birth_year())
    user_inputs.set_artist_death_year()
    user_death_year = int(user_inputs.get_artist_death_year())
    user_inputs.set_title()
    user_title = user_inputs.get_title()
    user_inputs.set_year_created()
    user_year_created = int(user_inputs.get_year_created())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()
