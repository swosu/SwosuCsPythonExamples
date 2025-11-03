class Instrument:
    def __init__(self, name, manufacturer, year_built, cost):
        self.name = name
        self.manufacturer = manufacturer
        self.year_built = year_built
        self.cost = cost
     
    def print_info(self):
        print(f'Instrument Information:')
        print(f'   Name: { self.name }')
        print(f'   Manufacturer: { self.manufacturer }')
        print(f'   Year built: { self.year_built }')
        print(f'   Cost: { self.cost }')


class StringInstrument(Instrument):
    # TODO: Define constructor with attributes:
    #       name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed
    def __init__(self, name, manufacturer, year_built, cost, num_strings, num_frets, is_bowed):
        super().__init__(name, manufacturer, year_built, cost)
        self.num_strings = num_strings
        self.num_frets = num_frets
        self.is_bowed = is_bowed

    def print_info(self):
        super().print_info()
        print(f'   Number of strings: { self.num_strings }')
        print(f'   Number of frets: { self.num_frets}')
        print(f'   Is bowed: { self.is_bowed }')

if __name__ == "__main__":
    instrument_name = input("Input the name of the instrument: ")
    manufacturer_name = input("Input the manufacturer name: ")
    year_built = int(input("Input the year built: "))
    cost = int(input("Input the cost: "))
    string_instrument_name = input("Input the name of the string instrument: ")
    string_instrument_manufacturer = input("Input the manufacturer name of the string instrument: ")
    string_instrument_year_built = int(input("Input the year the string instrument was built in: "))
    string_instrument_cost = int(input("Input the cost of the string instrument: "))
    num_strings = int(input("Input the number of strings on the string instrument: "))
    num_frets = int(input("Input the number of frets on the string instrument: "))
    is_bowed = input("Is the string instrument bowed? Say 'True' or 'False': ") == 'True'
   
    my_instrument = Instrument(instrument_name, manufacturer_name, year_built, cost)
    my_string_instrument = StringInstrument(string_instrument_name, string_instrument_manufacturer, string_instrument_year_built, string_instrument_cost, num_strings, num_frets, is_bowed)

    my_instrument.print_info()
    my_string_instrument.print_info()