class our_class:
    def __init__(self):
        self.data = []

    def say_hello(self):
        print('hello from inside the class.')


if __name__ == '__main__':
    our_object = our_class()
    our_object.say_hello()
