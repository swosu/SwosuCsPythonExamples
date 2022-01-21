class Artist:
    
    def __init__(self, name='None', birth_year=0, death_year=0):
        self.name = name
        self.birth_year = birth_year
        self.death_year = death_year

    def print_info(self):
        if self.death_year == -1:
            print('Artist: {}, born {}'.format(self.name, \
            self.birth_year))
        else:
            print('Artist: {} ({}-{})'.format(self.name,\
             self.birth_year, self.death_year))
