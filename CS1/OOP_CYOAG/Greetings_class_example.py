class Greetings:
    def __init__(self):
        self.data = []
        self.repeats = 0
        
    def print_hello(self):
        print("hello.")

    def print_hello_with_repeats(self):
        if 0 == self.repeats:
            print('there were no repeats.')
        else:
            for index in range (0, self.repeats):
                print(f'hello repeating {index + 1} of {self.repeats}.')
            self.repeats = 0

    def set_repeats(self, repeats_input):
        self.repeats = repeats_input


if __name__ == '__main__':
    
    our_object = Greetings()
    our_object.print_hello()
    our_object.print_hello_with_repeats()
    our_object.set_repeats(3)
    our_object.repeats = 5
    our_object.print_hello_with_repeats()
    our_object.print_hello_with_repeats()