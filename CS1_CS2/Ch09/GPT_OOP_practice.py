# Create the class GPT_OOP_practice with the following methods:
class GPT_OOP_practice:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'Hello, {self.name}!')

    def change_name(self, new_name):
        self.name = new_name
        print(f'Name changed to {self.name}!')



if __name__ == '__main__':
    # create the object
    our_object = GPT_OOP_practice('Joe')

    # call the method
    our_object.say_hello()

    another_object = GPT_OOP_practice('Jane')
    another_object.say_hello()

    our_object.change_name('Bob')

    our_object.say_hello()
    another_object.say_hello()

    