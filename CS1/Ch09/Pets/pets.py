class Pet:
    def __init__(self):
        print('Pet __init__ called')
        self.__name = ''

    def speak(self):
        print('Pet speak called')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_type(self, type):
        self.__type = type

    def print_infomation(self):
        print(f"Name: {self.__name}, Type: {self.__type}, Owner: {self.__owner}")

    def set_owner(self, owner):
        self.__owner = owner

    # I want to have one function call where I can feed all the pets for the class
    def feed():
        print('Pet feed called')


if __name__ == '__main__':
    mike = Pet()
    mike.set_name('Mike')
    print(f"Our pet name is {mike.get_name()}")
    # this line no longer works because the data is private: print(f"mike.__name = {mike.__name}")
    #mike.__name = 'Mike2'
    #print(f"Our pet name is {mike.get_name()}")
    #mike.set_name('Mike3')
    #print(f"Our pet name is {mike.get_name()}")

    mike.set_type('Cat')
    mike.set_owner('Joseph')
    mike.print_infomation()

    ranger = Pet()
    ranger.set_name('Ranger')
    ranger.set_type('Dog')
    ranger.set_owner('Joseph')
    ranger.print_infomation()

    luna = Pet()
    luna.set_name('Luna')
    luna.set_type('Dog')
    luna.set_owner('Charlene')
    luna.print_infomation()

    bella = Pet()
    bella.set_name('Adorabella Dearheart')
    bella.set_type('Double Doodle')
    bella.set_owner('Amanda (Jeremy\'s Wife and Favorite Person)')
    bella.print_infomation()

    muffin = Pet()
    muffin.set_name('Muffin (Snowball, Princess, Aggressive Little Ankle Biter)')
    muffin.set_type('BegealDore')
    muffin.set_owner('Magdalena, unless she needs something and then its Jeremy')
    muffin.print_infomation()

    Pet.feed()

