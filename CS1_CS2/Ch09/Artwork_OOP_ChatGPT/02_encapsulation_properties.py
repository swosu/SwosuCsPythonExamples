# 02_encapsulation_properties.py
# Goal: Show how to use getters and setters to protect data.

class Artist:
    def __init__(self, name="unknown", birth_year=-1, death_year=-1):
        # Use "private" attributes (leading underscore)
        self._name = name
        self._birth_year = birth_year
        self._death_year = death_year

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name
    def set_name(self, new_name):
        if len(new_name.strip()) > 0:
            self._name = new_name
        else:
            print("Name cannot be empty!")

    # TODO: Add getters/setters for birth_year and death_year


if __name__ == "__main__":
    artist = Artist()
    print("Initial:", artist.get_name())

    artist.set_name("Claude Monet")
    print("Updated:", artist.get_name())

    # Try invalid input
    artist.set_name("")
