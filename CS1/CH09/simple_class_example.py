class simple_class:
    def __init__(self):
        self.data = [1, 2, 3, 4]

    def test_print_function(self, number_of_stuff):
        print(f'hello special inside of class {number_of_stuff}.')

    def print_data(self):
        print('inside print data function')
        print(self.data)

if __name__ == '__main__':
    print('hello')
    our_object = simple_class()

    our_object.test_print_function(7)

    print(our_object.data)

    our_object.print_data()
