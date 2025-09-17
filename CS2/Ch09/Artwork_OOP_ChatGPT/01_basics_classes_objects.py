# 01_basics_classes_objects.py
# Goal: Introduce classes, attributes, and objects.

class Artist:
    # TODO: Define class-level attributes (like name, birth_year, death_year)
    pass


if __name__ == "__main__":
    # Example: Directly assign attributes (no constructor yet)
    artist1 = Artist()
    artist1.name = "Pablo Picasso"
    artist1.birth_year = 1881
    artist1.death_year = 1973

    artist2 = Artist()
    artist2.name = "Banksy"
    artist2.birth_year = -1
    artist2.death_year = -1

    # Print attributes directly
    print(f"Artist 1: {artist1.name}, {artist1.birth_year}-{artist1.death_year}")
    print(f"Artist 2: {artist2.name}, {artist2.birth_year}-{artist2.death_year}")
