import random

def get_user_input(prompt):
    return input(prompt + " ")

def generate_mad_lib():
    print("Welcome to the Silly Mad Lib Adventure!")
    print("-------------------------------------")

    # Ask silly questions
    adjective = get_user_input("Give me a funny adjective:")
    emotion = get_user_input("An emotion you might feel on a roller coaster:")
    animal = get_user_input("A type of animal:")
    unexpected_place = get_user_input("A place you'd never expect to find yourself:")
    silly_sound = get_user_input("A silly sound:")
    favorite_food = get_user_input("Your favorite food:")
    random_number = get_user_input("Give me a random number:")

    # Use random responses in different places in the story
    random_response_1 = random.choice([adjective, emotion, animal, unexpected_place, silly_sound, favorite_food])
    random_response_2 = random.choice([adjective, emotion, animal, unexpected_place, silly_sound, favorite_food])

    # Generate the mad lib story
    mad_lib_story = f"Once upon a time, in a {adjective} land, I decided to go on an emotional roller coaster."
    mad_lib_story += f" As I stepped onto the roller coaster, I felt a surge of {emotion}."

    mad_lib_story += f" Suddenly, a wild {animal} appeared and joined me for the ride. We went through twists and turns,"
    mad_lib_story += f" and before I knew it, we ended up in {unexpected_place}!"

    mad_lib_story += f" Out of nowhere, I heard a {silly_sound} and saw {random_response_1} flying around. It was like a scene from a crazy dream."

    mad_lib_story += f" After the roller coaster, I had a craving for {favorite_food}. I ate {random_number} servings and felt absolutely {random_response_2}."

    mad_lib_story += " The end! Thanks for joining the Silly Mad Lib Adventure!"

    print("\n" + mad_lib_story)

# Run the mad lib generator
generate_mad_lib()
