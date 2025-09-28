import random

def welcome_message(name):
    responses = [
        "The universe smiles upon you,",
        "A grand day awaits you,",
        "Fortune favors you today,",
        "The world is your oyster,",
        "Adventure calls you,",
    ]
    chosen_response = random.choice(responses)
    print(f"Hey {name}")
    print(f"{chosen_response} welcome to zyBooks!")

user_name = input("Enter your first name: ")
welcome_message(user_name)
