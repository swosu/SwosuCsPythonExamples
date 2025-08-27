# Dollar General Mad Libs — Small-Town Edition
# Run in any online Python runner (e.g., Replit, Programiz, Python.org shell).
# Tip: Press Enter to accept the silly default for faster laughs.

import random
import textwrap

Random_Variable_Object = random.choice

DEFAULTS = {
    "town": ["Possum Springs", "Prairie Dog Ridge", "Red Dirt Junction", "Coyote Flats"],
    "name": ["Bo", "Sharon", "Travis", "Lulu", "Aunt Deb"],
    "vehicle": ["rusty pickup", "sparkly scooter", "tractor", "1998 minivan", "rollerblades"],
    "adjective1": ["heroic", "questionable", "dramatic", "mysterious", "crispy"],
    "adjective2": ["family-sized", "economy", "thunderous", "unnecessarily bold", "spicy"],
    "animal": ["armadillo", "possum", "barn cat", "prize chicken", "sassy goat"],
    "snack": ["off-brand cheese puffs", "kettle chips", "mystery jerky", "cosmic brownie"],
    "soda": ["Mountain Mist", "Doctor Thunder", "Cola Maybe", "Orange-ish Fizz"],
    "aisle": ["3", "5", "7", "9", "12"],
    "clerk": ["Sharon", "Earl", "Misty", "DeShawn", "Tina"],
    "awkward": ["giant family pack of toilet paper", "hemorrhoid cushion", "industrial antacids",
                "minty foot spray", "jumbo hair nets"],
    "exclaim": ["MERP!", "Well butter my biscuits!", "Yee-haw!", "Sweet pickles!", "Oh beans!"],
    "verb_ing": ["speed-walking", "moonwalking", "power-lurking", "cart-drifting", "tip-toeing"],
    "number": ["7", "13", "27", "108", "5000"],
    "bodypart": ["elbow", "kneecap", "left eyebrow", "spleen (probably)", "big toe"],
    "color": ["neon yellow", "sunburn red", "denim blue", "tractor green", "dust-tan"],
}

def ask(prompt, key):
    """
    Ask with a funny hint; accept Enter for a random default.
    """
    hint = f" (Press Enter for something silly like: '{Random_Variable_Object(DEFAULTS[key])}')"
    val = input(prompt + hint + "\n> ").strip()
    return val if val else Random_Variable_Object(DEFAULTS[key])

def a_an(word: str) -> str:
    return ("an " if word[:1].lower() in "aeiou" else "a ") + word

def story(data):
    t = textwrap.dedent(f"""
        On a {data['adjective1']} afternoon in {data['town']}, our legend {data['name']}
        rolled up to Dollar General on {a_an(data['vehicle'])} that had exactly {data['number']} good noises
        and {data['number']} concerning ones.

        The automatic doors didn’t so much open as sigh. A display of {data['color']} {data['animal']}
        air fresheners stared with judgment. {data['name']} grabbed a cart that squeaked in Morse code for “help.”

        Mission: acquire {data['awkward']}. But destiny whispered, “snacks first.”
        Into the basket flew {data['snack']} and a bottle of {data['soda']}.
        The quest detoured through aisle {data['aisle']}, where {data['name']} practiced
        competitive {data['verb_ing']} and accidentally bonked a {data['bodypart']} on a rogue pool noodle.

        Suddenly, the PA crackled to life. It was {data['clerk']} at the register:
        “Price check on {data['awkward']}! Is this the {data['adjective2']} size, or the
        ‘hosting a barn-raising’ size?” Somewhere in produce, a single grape rolled in shame.

        At checkout, the card reader beeped like a small, angry robot. {data['name']} declared,
        “{data['exclaim']}” and fished out a wrinkled coupon shaped vaguely like Oklahoma.
        {data['clerk']} scanned it, the lights flickered, a distant banjo strummed,
        and the total changed to exactly ${data['number']}. Fate. Destiny. Discounts.

        With {data['awkward']} secured, {data['name']} strutted out triumphant—
        a conquering hero beneath the fluttering banner: “WELCOME TO {data['town'].upper()}:
        HOME OF {data['number']}-ISH DREAMS AND PRETTY GOOD PARKING.”
    """).strip("\n")
    return "\n" + textwrap.fill(t, width=90) + "\n"

def main():
    print("\n=== Dollar General Mad Libs — Small-Town Edition ===")
    print("Pro tip: Go bold. Weird adjectives, awkward items, and big exclamations = bigger laughs.\n")

    while True:
        data = {
            "town": ask("Name a tiny town", "town"),
            "name": ask("Your hero’s first name (or nickname)", "name"),
            "vehicle": ask("Mode of transport (e.g., tractor, scooter, rollerblades)", "vehicle"),
            "adjective1": ask("A dramatic adjective (e.g., heroic, mysterious, crispy)", "adjective1"),
            "animal": ask("A local animal (funnier = better)", "animal"),
            "color": ask("A loud color (e.g., neon yellow)", "color"),
            "snack": ask("A questionable snack choice", "snack"),
            "soda": ask("An off-brand soda name", "soda"),
            "aisle": ask("Pick a random aisle number", "aisle"),
            "clerk": ask("Name of the clerk on the PA", "clerk"),
            "awkward": ask("An awkward item to buy (keep it PG-13)", "awkward"),
            "adjective2": ask("Another adjective (for SIZE DRAMA)", "adjective2"),
            "exclaim": ask("A goofy exclamation", "exclaim"),
            "verb_ing": ask("An -ing verb (e.g., moonwalking)", "verb_ing"),
            "number": ask("A funny number", "number"),
            "bodypart": ask("A harmless body part", "bodypart"),
        }

        print(story(data))

        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for shopping—watch out for rogue pool noodles.")
            break

if __name__ == "__main__":
    main()
