import random
import time

# --------------------------------------------
# Choose Your Own Adventure (but the dice choose)
# Goals:
# - One user input (name)
# - No functions yet
# - Expressive variable names
# - If/else + random + lots of prints + time pauses
# --------------------------------------------

print("Welcome to: THE PATH OF CHAOS AND TURKEYS")
time.sleep(1.2)
print("A tiny choose-your-own-adventure where the dice are the narrator.")
time.sleep(1.2)
print()

user_name = input("What is your name, adventurer? ").strip()
if user_name == "":
    user_name = "Nameless Hero"

print()
print(f"Nice. Logged: user_name = {user_name}")
time.sleep(1.0)
print("Now... the world squints at you and decides your destiny.")
time.sleep(1.3)
print()

# --------------------------------------------
# 1) Role assignment: 4d6 vs d20 (slightly rigged toward the user)
# --------------------------------------------

print("=== ROLE ASSIGNMENT ===")
time.sleep(0.8)

user_role_roll_die_1 = random.randint(1, 6)
user_role_roll_die_2 = random.randint(1, 6)
user_role_roll_die_3 = random.randint(1, 6)
user_role_roll_die_4 = random.randint(1, 6)

user_role_roll_total_4d6 = (
    user_role_roll_die_1
    + user_role_roll_die_2
    + user_role_roll_die_3
    + user_role_roll_die_4
)

world_role_roll_d20 = random.randint(1, 20)

print(f"You roll 4d6 for destiny: {user_role_roll_die_1}, {user_role_roll_die_2}, {user_role_roll_die_3}, {user_role_roll_die_4}")
print(f"Total (4d6) = {user_role_roll_total_4d6}")
time.sleep(1.1)
print(f"The world rolls a d20 against you: {world_role_roll_d20}")
time.sleep(1.1)

if user_role_roll_total_4d6 > world_role_roll_d20:
    player_role = "Knight"
    player_title_name = f"Knight {user_name}"
    print()
    print("The universe nods respectfully.")
    print(f"You are a KNIGHT. All shall fear: {player_title_name}")
else:
    player_role = "Scribe"
    player_title_name = f"Welp {user_name}"
    print()
    print("The universe shrugs and hands you paperwork.")
    print(f"You are a SCRIBE. Your new official title is: {player_title_name}")

time.sleep(1.5)
print()

# --------------------------------------------
# 2) Weapon assignment based on the same role outcome
#    - If favorable (Knight): Chainsaw, attack points from TWO rolls of 4d6 (8d6 total each attack)
#    - If not favorable (Scribe): Book, attack points from ONE d6 halved (minimum 1)
# --------------------------------------------

print("=== WEAPON SELECTION ===")
time.sleep(0.8)

if player_role == "Knight":
    player_weapon_name = "CHAINSAW OF BAD IDEAS"
    player_weapon_is_favorable = True
    print(f"{player_title_name}, you are granted a favorable weapon:")
    print(f"Weapon: {player_weapon_name}")
    print("Damage each attack: TWO separate 4d6 rolls (added together).")
else:
    player_weapon_name = "VERY EDUCATIONAL BOOK"
    player_weapon_is_favorable = False
    print(f"{player_title_name}, you are granted a weapon of... learning:")
    print(f"Weapon: {player_weapon_name}")
    print("Damage each attack: roll 1d6, cut it in half (minimum 1).")
    print("You may also accidentally hit yourself with the corner. Knowledge hurts.")

time.sleep(1.6)
print()

# --------------------------------------------
# 3) Encounter assignment: new contest 4d6 vs d20
#    - If 4d6 wins: Turkey caught in bush
#    - If d20 wins: Angry female dwarf roasting turkey
# --------------------------------------------

print("=== THE ENCOUNTER ===")
time.sleep(0.8)

user_encounter_die_1 = random.randint(1, 6)
user_encounter_die_2 = random.randint(1, 6)
user_encounter_die_3 = random.randint(1, 6)
user_encounter_die_4 = random.randint(1, 6)
user_encounter_total_4d6 = user_encounter_die_1 + user_encounter_die_2 + user_encounter_die_3 + user_encounter_die_4

world_encounter_d20 = random.randint(1, 20)

print(f"You roll 4d6 for luck: {user_encounter_die_1}, {user_encounter_die_2}, {user_encounter_die_3}, {user_encounter_die_4}")
print(f"Total (4d6) = {user_encounter_total_4d6}")
time.sleep(1.1)
print(f"The world rolls a d20 for chaos: {world_encounter_d20}")
time.sleep(1.1)

if user_encounter_total_4d6 > world_encounter_d20:
    enemy_type = "Turkey"
    enemy_name = "A Turkey With Its Leg Stuck In A Bush"
    enemy_attack_die_sides = 6
    print()
    print("You push aside a fern and find...")
    time.sleep(1.0)
    print(f"{enemy_name}!")
    print("It looks confused, offended, and lightly marinated by fate.")
else:
    enemy_type = "Dwarf"
    enemy_name = "An Angry Female Dwarf Roasting A Turkey"
    enemy_attack_die_sides = 20
    print()
    print("You step into a clearing and immediately commit a social crime:")
    time.sleep(1.0)
    print(f"{enemy_name}!")
    print("This was her first peaceful moment in weeks.")
    print("You interrupted the sacred silence of snack-time.")
    print("She is now powered entirely by rage and protein.")

time.sleep(1.7)
print()

# --------------------------------------------
# 4) Health assignment
#    - If Turkey: turkey health = 1 d20; player health = sum of 3 separate 4d6 rolls
#    - If Dwarf: dwarf health = sum of 3 d20 rolls; player health = sum of 3 separate 4d6 rolls
# --------------------------------------------

print("=== HEALTH SETUP ===")
time.sleep(0.8)

player_health_roll_1 = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
player_health_roll_2 = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
player_health_roll_3 = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
player_health_points = player_health_roll_1 + player_health_roll_2 + player_health_roll_3

print(f"{player_title_name} health comes from THREE 4d6 rolls:")
print(f"  Roll 1 total = {player_health_roll_1}")
print(f"  Roll 2 total = {player_health_roll_2}")
print(f"  Roll 3 total = {player_health_roll_3}")
print(f"PLAYER HEALTH (sum) = {player_health_points}")
time.sleep(1.5)

if enemy_type == "Turkey":
    enemy_health_points = random.randint(1, 20)
    print()
    print(f"{enemy_name} health is ONE d20 roll:")
    print(f"ENEMY HEALTH = {enemy_health_points}")
else:
    enemy_health_roll_1 = random.randint(1, 20)
    enemy_health_roll_2 = random.randint(1, 20)
    enemy_health_roll_3 = random.randint(1, 20)
    enemy_health_points = enemy_health_roll_1 + enemy_health_roll_2 + enemy_health_roll_3
    print()
    print(f"{enemy_name} health comes from THREE d20 rolls:")
    print(f"  Roll 1 = {enemy_health_roll_1}")
    print(f"  Roll 2 = {enemy_health_roll_2}")
    print(f"  Roll 3 = {enemy_health_roll_3}")
    print(f"ENEMY HEALTH (sum) = {enemy_health_points}")

time.sleep(1.8)
print()

# --------------------------------------------
# 5) Enemy attack points (established once, per your spec)
#    - Dwarf: 1 d20
#    - Turkey: 1 d6
#
# Special rule:
# - If the attacker (enemy) rolls a 1 on THEIR attack die, they bonk themselves and lose that many attack points from their own health.
# --------------------------------------------

print("=== ENEMY ATTACK POWER ===")
time.sleep(0.8)

enemy_attack_points = random.randint(1, enemy_attack_die_sides)

print(f"{enemy_name} rolls 1d{enemy_attack_die_sides} to establish attack points...")
time.sleep(1.0)
print(f"Enemy attack points = {enemy_attack_points}")

time.sleep(1.2)
print()

# --------------------------------------------
# 6) Battle loop
# Turns alternate:
# - Player attacks (4d6 vs enemy's die)
# - Enemy attacks (enemy's die vs player's 4d6)
#
# Damage rules:
# - If player outrolls enemy on player turn => enemy loses player attack points
# - If enemy outrolls player on enemy turn => player loses enemy attack points
# - If attack roll is 1 for the attacker (enemy die), attacker hurts self (their attack points)
#
# Player attack points per turn:
# - Chainsaw: two 4d6 rolls summed
# - Book: 1d6 halved (minimum 1)
#   Book has a "corner hazard": if the raw d6 is 1, you take 1 self-damage (tiny but funny)
# --------------------------------------------

print("=== BATTLE BEGINS ===")
time.sleep(1.2)

battle_round_number = 1
player_turn_is_next = True

while player_health_points > 0 and enemy_health_points > 0:
    print()
    print(f"--- Round {battle_round_number} ---")
    time.sleep(0.9)

    if player_turn_is_next:
        print(f"{player_title_name}'s TURN to attack!")
        time.sleep(0.8)

        player_roll_for_combat_die_1 = random.randint(1, 6)
        player_roll_for_combat_die_2 = random.randint(1, 6)
        player_roll_for_combat_die_3 = random.randint(1, 6)
        player_roll_for_combat_die_4 = random.randint(1, 6)
        player_combat_roll_total_4d6 = (
            player_roll_for_combat_die_1
            + player_roll_for_combat_die_2
            + player_roll_for_combat_die_3
            + player_roll_for_combat_die_4
        )

        enemy_defense_roll = random.randint(1, enemy_attack_die_sides)

        print(f"You roll 4d6 to attack: {player_roll_for_combat_die_1}, {player_roll_for_combat_die_2}, {player_roll_for_combat_die_3}, {player_roll_for_combat_die_4}")
        print(f"Your attack roll total (4d6) = {player_combat_roll_total_4d6}")
        time.sleep(1.0)
        print(f"Enemy rolls 1d{enemy_attack_die_sides} to defend: {enemy_defense_roll}")
        time.sleep(1.0)

        # Compute player attack points this turn (weapon-driven)
        if player_weapon_is_favorable:
            player_damage_roll_a = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            player_damage_roll_b = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
            player_attack_points_this_turn = player_damage_roll_a + player_damage_roll_b

            print(f"Weapon effect: {player_weapon_name}")
            print(f"Damage roll A (4d6 total) = {player_damage_roll_a}")
            print(f"Damage roll B (4d6 total) = {player_damage_roll_b}")
            print(f"PLAYER ATTACK POINTS (sum) = {player_attack_points_this_turn}")
        else:
            book_raw_d6 = random.randint(1, 6)
            player_attack_points_this_turn = book_raw_d6 // 2
            if player_attack_points_this_turn < 1:
                player_attack_points_this_turn = 1

            print(f"Weapon effect: {player_weapon_name}")
            print(f"Book toss raw roll (1d6) = {book_raw_d6}")
            print(f"Book damage is half (min 1) => PLAYER ATTACK POINTS = {player_attack_points_this_turn}")

            # Book corner hazard (tiny self-bonk)
            if book_raw_d6 == 1:
                print("CRITICAL LITERATURE INCIDENT: The book corners your own face. -1 health.")
                player_health_points -= 1
                if player_health_points < 0:
                    player_health_points = 0

        time.sleep(1.2)

        # Compare rolls to see if attack lands
        if player_combat_roll_total_4d6 > enemy_defense_roll:
            enemy_health_points -= player_attack_points_this_turn
            if enemy_health_points < 0:
                enemy_health_points = 0
            print("HIT! Your roll beat their defense.")
            print(f"Enemy loses {player_attack_points_this_turn} health.")
        elif player_combat_roll_total_4d6 == enemy_defense_roll:
            glancing_damage = player_attack_points_this_turn // 2
            if glancing_damage < 1:
                glancing_damage = 1
            enemy_health_points -= glancing_damage
            if enemy_health_points < 0:
                enemy_health_points = 0
            print("TIE! A glancing blow!")
            print(f"Enemy loses {glancing_damage} health.")
        else:
            print("BLOCKED! The enemy stuffs your attack in the metaphorical trash.")
            print("No damage dealt.")

        time.sleep(1.1)
        print(f"STATUS: Player HP = {player_health_points} | Enemy HP = {enemy_health_points}")

        player_turn_is_next = False
        battle_round_number += 1

    else:
        print(f"{enemy_name}'s TURN to attack!")
        time.sleep(0.8)

        enemy_attack_roll = random.randint(1, enemy_attack_die_sides)
        player_defense_die_1 = random.randint(1, 6)
        player_defense_die_2 = random.randint(1, 6)
        player_defense_die_3 = random.randint(1, 6)
        player_defense_die_4 = random.randint(1, 6)
        player_defense_total_4d6 = (
            player_defense_die_1
            + player_defense_die_2
            + player_defense_die_3
            + player_defense_die_4
        )

        print(f"Enemy rolls 1d{enemy_attack_die_sides} to attack: {enemy_attack_roll}")
        time.sleep(1.0)
        print(f"You roll 4d6 to defend: {player_defense_die_1}, {player_defense_die_2}, {player_defense_die_3}, {player_defense_die_4}")
        print(f"Your defense total (4d6) = {player_defense_total_4d6}")
        time.sleep(1.2)

        # "roll a 1 and you hurt yourself" rule for the attacker (enemy)
        if enemy_attack_roll == 1:
            print("DISASTER! The attacker rolled a 1 and basically kicked their own toe into another dimension.")
            print(f"{enemy_name} loses {enemy_attack_points} health (self-inflicted).")
            enemy_health_points -= enemy_attack_points
            if enemy_health_points < 0:
                enemy_health_points = 0
        else:
            # Compare rolls to see if enemy lands attack
            if enemy_attack_roll > player_defense_total_4d6:
                player_health_points -= enemy_attack_points
                if player_health_points < 0:
                    player_health_points = 0
                print("HIT! Enemy roll beat your defense.")
                print(f"You lose {enemy_attack_points} health.")
            elif enemy_attack_roll == player_defense_total_4d6:
                chip_damage = enemy_attack_points // 2
                if chip_damage < 1:
                    chip_damage = 1
                player_health_points -= chip_damage
                if player_health_points < 0:
                    player_health_points = 0
                print("TIE! A painful little nick.")
                print(f"You lose {chip_damage} health.")
            else:
                print("BLOCKED! You defend like a champion (or at least like someone who wants to remain alive).")
                print("No damage taken.")

        time.sleep(1.1)
        print(f"STATUS: Player HP = {player_health_points} | Enemy HP = {enemy_health_points}")

        player_turn_is_next = True
        battle_round_number += 1

# --------------------------------------------
# 7) Battle outcome
# --------------------------------------------

print()
print("=== BATTLE RESULT ===")
time.sleep(1.0)

if player_health_points > 0 and enemy_health_points == 0:
    print(f"{player_title_name} wins!")
    time.sleep(1.0)

    if enemy_type == "Turkey":
        print("The turkey is defeated (and also dinner, apparently).")
        time.sleep(1.0)
        turkey_feast_heal_roll = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
        print(f"You feast and restore health by 4d6 = {turkey_feast_heal_roll}")
        player_health_points += turkey_feast_heal_roll
        print(f"NEW PLAYER HEALTH = {player_health_points}")
        time.sleep(1.0)
        print("You walk away stronger... and unreasonably thankful for bushes.")
    else:
        print("The dwarf drops her turkey fork in disbelief.")
        time.sleep(1.0)
        print("You step away slowly, respectfully, and with the wisdom of someone who will never interrupt dinner again.")
else:
    print(f"{player_title_name} has fallen...")
    time.sleep(1.0)
    print("Your legend ends here, in a dramatic heap of questionable decisions.")
    time.sleep(1.0)
    print("On the bright side: your story will be retold as a warning, and possibly a meme.")

print()
print("=== THE END ===")
