#class Decide:
    #def __init__(self):
        #self.data = []
        #self.explore_asylum = ""


decision = ''
leave_asylum = ''
explore_asylum = ''
explore_alone = ''
visit_party_ghost = ''
visit_mentor_ghost = ''
visit_party_ghost2 = ''
visit_mentor_ghost2 = ''
ignore_party_ghost = ''
follow_party_ghost = ''
follow_mentor_ghost = ''
trust_mentor_ghost = ''

def choices2(option1,option2):
    decision = input("What is your decision, A or B?\n")
    if decision == 'A':
        option1()
    elif decision == 'B':
        option2()

def choices3(option1, option2, option3):
    decision = input("What is your decision, A, B, or C?\n")
    if decision == 'A':
        option1()
    elif decision == 'B':
        option2()
    elif decision == 'C':
        option3()

def LeaveAsylumEnd():
    print("This place gives you the shivers, you're out. As you make your way to the edge of the asylum, you get the strange feeling you're being watched, but the feeling only makes you move faster. In your hurry, you don't see the trap waiting for you right outside the asylum. Some crazy ghost hunters were waiting for you! You're sucked into the trap, and can only watch, helpless as they gather around you excitedly, as if your last breaths as a ghost were some kind of show.\nGame Over.")
    global leave_asylum
    leave_asylum = 'active'
    return leave_asylum
    
def ExploreAsylum():
    print('Okay, so that asylum definitely looks haunted, but you are technically a ghost, so you might as well check it out.')
    global explore_asylum
    explore_asylum = 'active'
    return explore_asylum
    

def ExploreAlone():
    print('You decided to explore alone.')
    global explore_alone
    explore_alone = 'active'
    return explore_alone

def VisitPartyGhost():
    print("You decided to talk to the party ghost.")
    global visit_party_ghost
    visit_party_ghost = 'active'
    return visit_party_ghost

def VisitMentorGhost2():
    print('You decided to talk to the lonely ghost.')
    global visit_mentor_ghost2
    visit_mentor_ghost2 = 'active'
    return visit_mentor_ghost2

def VisitPartyGhost2():
    print("You decided to talk to the party ghost.")
    global visit_party_ghost2
    visit_party_ghost2 = 'active'
    return visit_party_ghost2

def VisitMentorGhost():
    print('You decided to talk to the lonely ghost.')
    global visit_mentor_ghost
    visit_mentor_ghost = 'active'
    return visit_mentor_ghost

def FollowPartyGhostEnd():
    print("At first, you're hesitant to jump right in to the swirling mass of chaos that is the party of ghosts, but once you do, it's the most fun you've ever had in your life! Well, as far as you can remember, which is not very far. You party with the party ghost for the rest of your life, with only a vague feeling that you should be somewhere else.\nGame Over.")
    global follow_party_ghost
    follow_party_ghost = 'active'
    return follow_party_ghost

def FollowMentorGhost():
    print("Okay, so you're going to follow this ghost and see what happens. He begins talking to you again. 'Upstairs, the portal is upstairs I can feel it. We have to go upstairs to get home. We're going to get home!' You have two choices.\n(A) Leave the asylum. Everyone here is out of their minds, and maybe there's someone who knows what they're talking about in town.\n(B) Trust this ghost. He seems crazy, but he also seems like he knows what he's talking about.\n")
    global follow_mentor_ghost
    follow_mentor_ghost = 'active'
    return follow_mentor_ghost

def IgnorePartyGhost():
    print('You ignored the party ghost.')
    global ignore_party_ghost
    ignore_party_ghost = 'active'
    return ignore_party_ghost

def FollowGlimmerEnd():
    print("You approach the blue glimmer slowly. Something about this seems so familiar... Behind the cracked wall, the light dances and fades, only to come back brighter than before. You begin to feel into the cracks of the wall, and as you do, it simply flakes away, revealing a swirling, blue, rip in space. Or at least, that's how you would describe it. Well, you've gone this far, might as well go all the way. You step through the portal, and are immediately met by the sounds of singing birds, the bright blue of a cloudless sky, and the smell of wildflowers filling your nose. You hear a voice,'There he is!, We found him!' and are soon surrounded by your mother, your grandmother, your father, your grandfather, all the friends you thought were gone for good. 'Wait, wh-where am I?' you ask, overwhelmed. They explain to you that this is the land of the ghosts, where spirits go when they have been freed of their bodies. They warn you never to follow that intriguing blue light again, because countless ghosts are still stuck in the land of men, and you are incredibly lucky to have found your way back safely.")

def FollowGlowEnd():
    print("You bend down near the floorboards, trying to get a closer look at that glow. The light is so mesmerizing, you can't seem to pull yourself away. Oh no. You literally can't pull away! You're sucked into the trap, and can only watch, helpless as they gather around you excitedly, as if your last breaths as a ghost were some kind of show.\nGame Over.")

def TrustMentorGhost():
    print("Maybe, this ghost is crazy, but maybe he's onto something. He continues his muttering, and begins making his way upstairs. You follow, and when you get upstairs, a blue glimmer immediately catches your eye. You begin floating towards the light, entranced, when you hear a shout behind you. You turn, and see the lonely ghost being sucked into the floorboards by some kind of trap! You have two choices.\n(A) Try to help the ghost out. He may be crazy, but he is trying to help you get somewhere, and you can't just let him die. (B) Leave him to die and check out the blue light. It's too late to help him, and you might be able to save yourself.")
    global trust_mentor_ghost
    trust_mentor_ghost = 'active'
    return trust_mentor_ghost

def HelpMentorGhostEnd():
    print("You grab the lonely ghosts's hand to pull him out of the trap, but he just keeps getting sucked in. You have no choice but to let go, so you do, and you turn towards the glimmer again, but you can't move! Slowly, the trap begins sucking you in too, and there's nothing you can do about it. You're sucked into the trap, and can only watch, helpless as a group of ghosthunters gathers around you excitedly, as if your last breaths as a ghost were some kind of show. Now the lonely ghost is dead, and you are too.\nGame Over.")


def Enid_adventure():
    print("After the initial shock has passed, you begin to look around. It appears the truck has stopped just inside a small town called Enid if the sign is correct, and has a package to drop off at the abandoned insane asylum. The truck driver seems to be disturbed. You watch as he scratches his head and mutters, 'Must be a wrong address' as he climbs back into the truck and drives away, without you. You now have two choices,\n(A) Ditch this creepy asylum and try to find your way into the city of Enid.\n(B) Explore the asylum and try to find some help. It sure look like there could be some more ghosts in there...")
    choices2(LeaveAsylumEnd, ExploreAsylum)
    
    if explore_asylum == 'active':
        print("As you walk, or float, or whatever ghosts do up the stairs to the first building, an eerie hush surrounds you. Only the hoot of an owl or the swoop of a bat occasionally disturbs the quiet of the night. You walk around the building, casting no shadow as the moon shines through the broken window. You climb up the stairs, your feet making no crunch on the shattered glass beneath them. Once you're on the top floor, you look out a window and see faint, glimmering movements through the windows of another building and decide to make your way there. When you get there (after the exciting discovery of your abilities to fly), two ghosts immediately catch your attention. The first seems to be having the time of his life, swooping through the building alongside other ghosts. The other is by himself, clearly uninterested in the party taking place across the room. You have three choices.\n(A) Have nothing to do with anyone and keep exploring by yourself. You got yourself into this mess and you can get yourself out.\n(B) Introduce yourself to the party ghost. He seems fun, and considering you just woke up on the side of a highway with no memory, only to discover you're a ghost, a little fun could be exactly what you need right now.\n(C) Introduce yourself to the lonely ghost. He looks like he has some kind of purpose to what he's doing. Maybe he can help you figure out what's going on.")
        choices3(ExploreAlone, VisitPartyGhost, VisitMentorGhost)

        if explore_alone == 'active':
            print("The last thing you need right now is the stress of introducing yourself to ghosts who have obviously already got this ghost thing figured out. You quietly slip past the party, and make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
            choices2(FollowGlimmerEnd, FollowGlowEnd)

        elif visit_party_ghost == 'active':
            print("You hesitantly approach the party ghost, and you immediately catch his eye. 'JOIN THE PARTY!!!' he yells in your direction, and it sure does look fun. You have three choices.\n(A) Continue exploring by yourself. This guy is crazy!\n(B) See if the lonely ghost is a little more helpful.\n(C) Join the party! You deserve it after waking up on the side of the highway.\n")
            choices3(ExploreAlone, VisitMentorGhost, FollowPartyGhostEnd)
            
            if explore_alone == 'active':
                print("The last thing you need right now is the stress of introducing yourself to ghosts who have obviously already got this ghost thing figured out. You quietly slip past the party, and make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
                choices2(FollowGlimmerEnd, FollowGlowEnd)
            elif visit_mentor_ghost == 'active':
                print("You float towards the corner where the lonely ghost is hunched in the corner. He seems to be muttering something to himself and you start to wonder if this was such a good idea. Before you can back out, he turns to face you and begins talking to you. 'We're trapped, trapped, and we have to get out. We don't belong here don't you see?' 'What?' you respond, confused. 'This is the world of men, this is a world of physical bodies and we have to find our way back. I know I'm close I can feel it. The portal is near.' You have three choices.\n(A) Both of these ghosts seem out of their minds. You're better off figuring this out on your own. Explore alone.\n(B) Go back and join the party. That looks way more fun than hanging out with some insane old ghost who's obviously out of his mind.\n(C) Trust this ghost. Sure he seems crazy, but maybe there's actually a way to get back to 'ghostland' or wherever he's trying to go.\n")
                choices3(ExploreAlone, VisitPartyGhost2, FollowMentorGhost)
                if explore_alone == 'active':
                    print("You quietly slip past the party, and make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
                    choices2(FollowGlimmerEnd, FollowGlowEnd)
                elif visit_party_ghost2 == 'active':
                    print("You hesitantly approach the party ghost, and you immediately catch his eye. 'JOIN THE PARTY!!!' he yells in your direction, and it sure does look fun. You have two choices.\n(A) Continue exploring by yourself. This guy is crazy!\n(B) Join the party! You deserve it after waking up on the side of the highway.\n")
                    choices2(ExploreAlone, FollowPartyGhostEnd)
                    if explore_alone == 'active':
                        print("You quietly slip past the party, and make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
                        choices2(FollowGlimmerEnd, FollowGlowEnd)
                elif follow_mentor_ghost == 'active':
                    print("You decided to follow the lonely ghost.")
                    choices2(LeaveAsylumEnd, TrustMentorGhost)
                    if trust_mentor_ghost == 'active':
                        choices2(FollowGlimmerEnd, HelpMentorGhostEnd)

        elif visit_mentor_ghost == 'active':
            choices3(ExploreAlone, VisitPartyGhost, FollowMentorGhost)
            if explore_alone == 'active':
                print("You quietly slip past the party, and make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
                choices2(FollowGlimmerEnd, FollowGlowEnd)
            if visit_party_ghost == 'active':
                print("You hesitantly approach the party ghost, and you immediately catch his eye. 'JOIN THE PARTY!!!' he yells in your direction, and it sure does look fun. You have two choices.\n(A) Continue exploring by yourself. This guy is crazy!\n(B) See if the lonely ghost is a little more helpful.\n(C) Join the party! You deserve it after waking up on the side of the highway.\n")
                choices3(ExploreAlone, VisitMentorGhost2, FollowPartyGhostEnd)
                if explore_alone == 'active':
                    print("You quietly slip past the party, and make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
                    choices2(FollowGlimmerEnd, FollowGlowEnd)
                elif visit_mentor_ghost2 == 'active':
                    print("You float towards the corner where the lonely ghost is hunched in the corner. He seems to be muttering something to himself and you start to wonder if this was such a good idea. Before you can back out, he turns to face you and begins talking to you. 'We're trapped, trapped, and we have to get out. We don't belong here don't you see?' 'What?' you respond, confused. 'This is the world of men, this is a world of physical bodies and we have to find our way back. I know I'm close I can feel it. The portal is near.' You have three choices.\n(A) Both of these ghosts seem out of their minds. You're better off figuring this out on your own. Explore alone.\n(B) Trust this ghost. Sure he seems crazy, but maybe there's actually a way to get back to 'ghostland' or wherever he's trying to go.")
                    choices2(ExploreAlone, FollowMentorGhost)
                    if explore_alone == 'active':
                        print("You make your way upstairs to look for, well, anything that could help you figure out what's going on. On the top floor, you begin looking around, and a blue glimmer catches your eye. You begin floating near, curious, but immediately you are distracted by a warm yellow glow coming from under the floorboards. You have two choices.\n(A) Follow the glimmer coming from the wall. It's so pretty, and you can always come back to the glow if it isn't anything important.\n(B) Follow the glow. It looks so warm and welcoming, and you can always come back to the glimmer if it isn't anything important.")
                        choices2(FollowGlimmerEnd, FollowGlowEnd)
                    elif follow_mentor_ghost == 'active':
                        print('You decided to follow the lonely ghost.')
                        choices2(LeaveAsylumEnd, TrustMentorGhost)
                        if trust_mentor_ghost == 'active':
                            print('You chose to trust the lonely ghost')
                            choices2(FollowGlimmerEnd, HelpMentorGhostEnd)
