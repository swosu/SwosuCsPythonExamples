
class Char:
    def __init__(self, type, attack, health, Location):
        self.type = type
        self.attack = attack
        self.health = health
        self.Location = Location
    def modify_health(damage):
        Char.health += damage


def class_selection():
    print("\nwhat kind of traveler are ya??")
    
    print("\n1. Knight\n    As a guardian of the land, ya must be on a quest from the king.\nSuch a noble life, ya'l most likely have cheaper rates through ya journey\nAlthough watch out for those who don't want you up in their business.")
    print("Here are the statistics for the Knight:")
    print("- Health: 100\n- Attack: +3")
    
    print("\n2. Elf\n    As an elf ya grew up on the outskirts of civilization.  Outcasted by society, set on revenge.\nElves aren't respected in cities, watch yer back.")
    print("    Elves are naturally gifted in the spiritual world.  They're the only class to be able to wield magic and enchanted weapons.")
    print("Here are the statistics for the Elf:")
    print("- Health: 80\n- Attack: +1")
    
    print("\n3. Viking\n    As pillagers of the sea, yer known to use anything to take what they please.")
    print("Here are the statistics for the Viking:")
    print("-- Health: 100\n- Attack: +4")
    
    print("\n4. Dwarf\n    Ya'v spend most of ya life underground, were ya working or hiding from the world?")
    print("Here are the statistics for the Dwarf:")
    print("- Health: 100\n- Attack: +3")
    
    print("\n5. Assassin\n    Hired by some rich fella, ya must be on a journey across the land, fulfilling a contract.")
    print("Here are the statistics for the Assassin:")
    print("- Health: 100\n- Attack: +2")
    
    print("\n6. Archer\n    Are ya hunting a monster or your next meal?")
    print("Here are the statistics for the Archer:")
    print("- Health: 100\n- Attack: +2")

    class_selection_num = int(input("\nPlease select your class (1-6): "))

    if class_selection_num == 1:
        Char.type = "Knight"
        Char.attack = 3
        Char.health = 100
    
    elif class_selection_num == 2:
        Char.type = "Elf"
        Char.attack = 1
        Char.health = 80
    
    elif class_selection_num == 3:
        Char.type = "Viking"
        Char.attack = 4
        Char.health = 100

    elif class_selection_num == 4:
        Char.type = "Dwarf"
        Char.attack = 3
        Char.health = 100

    elif class_selection_num == 5:
        Char.type = "Assassin"
        Char.attack = 2
        Char.health = 100
    
    elif class_selection_num == 6:
        Char.type = "Archer"
        Char.attack = 2
        Char.health = 100

    else:
        print("\nINVALID INPUT WE NOW HAVE YER MEDICAL RECORDS\n")
        class_selection()
        
        
 

def char_stats():
    print("\nCharacter Type = ", Char.type,"\nCharacter Health = ", Char.health, "\nCharacter Attack = ", Char.attack)

def main():
    class_selection()
    char_stats()

if __name__ == "__main__":
    main()
