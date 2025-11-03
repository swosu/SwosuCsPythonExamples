class Artist:
    def __init__(self, name, birth_year, death_year):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if self.birth_year >= 0 and self.death_year >= 0:
            print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')
        elif self.birth_year >= 0:
            print(f'Artist: {self.name} ({self.birth_year} - present)')
        else:
            print(f'Artist: {self.name} (unknown)')