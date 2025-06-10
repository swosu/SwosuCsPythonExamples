# main.py

import helper  # Import the helper module
from assistant import Greeter  # Import the Greeter class from helper

def main():
    greeter = Greeter()  # Create an instance of the Greeter class
    
    # Get and print different greetings
    print(greeter.get_greeting("morning"))
    print(greeter.get_greeting("afternoon"))
    print(greeter.get_greeting("evening"))
    print(greeter.get_greeting("unknown"))  # This will use the default greeting

if __name__ == "__main__":
    main()

    helper.print_message()  # Call the function from the helper module
