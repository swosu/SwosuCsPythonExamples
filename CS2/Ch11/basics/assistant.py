# assistant.py

class Greeter:
    def __init__(self):
        # A dictionary containing different greeting options
        self.greetings = {
            "morning": "Good morning!",
            "afternoon": "Good afternoon!",
            "evening": "Good evening!",
            "default": "Hello!"
        }

    # Method to get a greeting based on the time of day or a custom option
    def get_greeting(self, time_of_day="default"):
        return self.greetings.get(time_of_day, self.greetings["default"])
