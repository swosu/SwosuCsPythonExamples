class Greetings_and_things:

    def __init__(self):
        self.__message = 'hello'

    def set_greeting(self, message):
        self.__message = message

    def print_greeting(self):
        print(self.__message)

if __name__ == '__main__':
    first_object = Greetings_and_things()
    second_object = Greetings_and_things()

    first_object.set_greeting('Thanks for all the fish.')
    first_object.print_greeting()

    second_object.print_greeting()

    user_greeting = input('Please enter a greeting: ')

    second_object.set_greeting(user_greeting)
    second_object.print_greeting()
    first_object.print_greeting()
