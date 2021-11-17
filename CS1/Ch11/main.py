from Artist import Artist
from Artwork import Artwork
from Data_Manager import Data_Manager

if __name__ == "__main__":
    user_inputs = Data_Manager()
    user_inputs.load_user_inputs()

    user_artist = Artist(user_inputs.get_artist_name(),\
     int(user_inputs.get_artist_birth_year()), \
     int(user_inputs.get_artist_death_year()))

    new_artwork = Artwork(user_inputs.get_title(), \
    int(user_inputs.get_year_created()), user_artist)

    new_artwork.print_info()
