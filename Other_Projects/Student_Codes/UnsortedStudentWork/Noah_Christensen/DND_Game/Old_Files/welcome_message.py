'''NOTES: WHAT I NEED TO ADD/FIX
I need to modify health and attack for each character type.  


'''






class Char:
    def __init__(self, type, attack, health):
        self.type = type
        self.attack = attack
        self.health = health
    def modify_health(self, amount):
        self.health += amount
    def modify_attack(self, amount):
        self.attack += amount


char_classes = {
    "Knight": Char("knight", 3, 100),
    "Elf": Char("elf", 1, 80),
    "Viking": Char("viking", 4, 100),
    "Dwarf": Char("dwarf", 3, 100),
    "Assassin": Char("assassin", 3, 100),
    "Archer": Char("archer", 3, 100)
}



def main(character_instance):
    print("Welcome Traveler, ya'v come a long way...")
    username = input("What should I call ya? ")
    print()
    print(f"Well it is nice to meet ya {username}")
    char_class(character_instance)
    game_rules()
    start_loc()



def char_class(character_instance):

    print("\nBefore I do, what kind of traveler are ya?")
    
    print("\n1. Knight\n    As a guardian of the land, ya must be on a quest from the king.\nSuch a noble life, ya'l most likely have cheaper rates through ya journey\nalthough watch out for those who don't like the knights always in their business.")
    print("    Knights are naturally gifted with their swords however their armor tends to weigh them down not allowing them to move very quietly.")
    print("Here are the statistics for the Knight:")
    print("- Health: 100\n- Attack: +3")
    
    print("\n2. Elf\n    As an elf ya grew up on the outskirts of civilization.  Outcasted by society, set on revenge.\nElves aren't respected in cities, watch yer back.")
    print("    Elves are naturally gifted in the spiritual world.  They're the only class to be able to wield magic and enchanted weapons.")
    print("Here are the statistics for the Elf:")
    print("- Health: 80\n- Attack: +1")
    
    print("\n3. Viking\n    As pillagers of the sea, yer known to use anything to take what they please.")
    print("    Vikings are naturally gifted in fighting, not bound by moral code, nothing will stop the viking.")
    print("Here are the statistics for the Viking:")
    print("-- Health: 100\n- Attack: +4")
    
    print("\n4. Dwarf\n    ya'v spend most of ya life underground, were ya working or hiding from the world?")
    print("    Dwarves are naturally gifted underground, in caves they have an increased chance of fleeing.")
    print("Here are the statistics for the Dwarf:")
    print("- Health: 100\n- Attack: +2")
    
    print("\n5. Assassin\n    Hired by some rich fella, ya must be on a journey across the land, fulfilling a contract.")
    print("    Assassins are naturally gifted in stealth, with greater chance at fleeing across almost every location.")
    print("Here are the statistics for the Assassin:")
    print("- Health: 100\n- Attack: +1")
    
    print("\n6. Archer\n    Are ya hunting a monster or your next meal?")
    print("    Archers are naturally gifted in range weapons, this allows them to flee more easily.")
    print("Here are the statistics for the Archer:")
    print("- Health: 100\n- Attack: +1")


    charclass_num = int(input("Please select your class (1-6): "))
    class_keys = ["Knight", "Elf", "Viking", "Dwarf", "Assassin", "Archer"]

    if 1 <= charclass_num <= 6:
        selected_class = class_keys[charclass_num - 1] # we subtract one to adjust for 0
        character_instance = Char(selected_class)
        print(f"Ah, of course, how could I not see, yer a {character_instance.type}.")
        char_stats(character_instance)
        if selected_class == "Knight":
            print("\nOh such nobility from ya.")
            character_instance.modify_attack(3)
        elif selected_class == "Elf":
            print("Ya better watch yer back... elf...")
            character_instance.modify_health(80)
        elif selected_class == "Viking":
            print("\nOh I wouldn't want to mess with ya.")
            character_instance.modify_attack(4)
        elif selected_class == "Dwarf":
            print("\nHA")
            character_instance.modify_attack(3)
        elif selected_class == "Assassin":
            print("\nI don't want any trouble...")
            character_instance.modify_attack(3)
        elif selected_class == "Archer":
            print("Got any food on ya, I'm starving?")
            character_instance.modify_attack(3)
    else:
        print("Yer not gonna be easy to deal with are ya?")
        return character_instance





def char_stats(character_instance):
    print(f"Yer a {character_instance.type}")
    print(f"Yer Health: {character_instance.health}")
    print(f"Yer Attack: {character_instance.attack}")

def game_rules():
    print()
    print("Before ya leave, let me tell you a bit about what ya getting yaself into.\nBe careful as you move about the lands, creatures may pop up.\nHowever so might valuable treasure.")
    print("There aren't many rules, but from one friend to another, let me give ya advice to help ya on ya journey.")
    print("There are three rules you'll need to follow to survive.\n1.) Survival is the most important, it'd be wise to find a companion.  You know, someone to use as bait as you escape, you must do what you can to survive, you can always get another one later.\n2.) Do not work with Demons.\n3.) If you're in a guarded city, I'd recommend exploring the city.")

def start_loc():
    print()
    print("You're a long ways from home, my friend.  How did you end up here?")
    print("Where are you?")
    print("1.) Washed up on shore (With Nothing)\n2.) In a tavern (Drunk and Armed)\n3.) In the woods (Hunting a creature)\n4.) Aboard a docked ship (Seasick and Armed)\n5.) In a cemetary (Performing a seance naked)\n6.) In a Guarded City (Fully Armed)")
    user_loc = int(input("Please enter 1-6 for ya starting location: "))


main()
