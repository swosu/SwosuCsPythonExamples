
class Greetings:

    def say_howdy():
        print('hello')

    def __init__(self):
        self.__message = 'hello'
        self.unhidden_message = 'Greetings!'

    def say_hello(self):
        print(self.__message)

    def set_message(self, message):
        self.__message = message

        
if __name__ == '__main__':
    
    #Greetings.say_hello()
    #for index in range(5):
    #    say_hello()

    Greetings.say_howdy()
    our_greeting = Greetings()
    our_greeting.say_hello()
    our_greeting.set_message('I like warm hugs.')
    our_greeting.say_hello()

    print(our_greeting.unhidden_message)

    #print(our_greeting.__message)
    our_greeting.unhidden_message = 'Goodbye!'
    print(our_greeting.unhidden_message)
    our_greeting.__message = 'So long!'
    our_greeting.say_hello()

