import random
import pygame
from Scoring import *


pygame.init()
##Initializes screen, sets size, caption, timer, font, and colors. 
##Also creates variables for white and black.
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
smallText = pygame.font.Font("freesansbold.ttf",20)
midText = pygame.font.Font('freesansbold.ttf', 50)
largeText = pygame.font.Font('freesansbold.ttf',115)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 200, 0)
red = (200, 0, 0)

centered = WIDTH/2 - 50
left = 100
right = 400

topMenuButton = 300
middleMenuButton = 450
bottomMenuButton = 600
bottomRulesButton = 650
menuButtonWidth = 100
menuButtonHeight = 50

numbers_list = [0, 0, 0, 0, 0,]
roll = False
rolls_left = 3
selected = [False, False, False, False, False]
selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False, False]
possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
totals = [0, 0, 0, 0, 0, 0, 0]
clicked = -1
bonus_time = False
player = 1
something_selected = False
score = 0
game_over = False

def check_scores(selected_choice, numbers_list, possible, score):
    active = 0
    for index in range(len(selected_choice)):
        if selected_choice[index]:
            active = index
    if active == 0:
        score = numbers_list.count(1)
    elif active == 1:
        score = numbers_list.count(2) * 2
    elif active == 2:
        score = numbers_list.count(3) * 3
    elif active == 3:
        score = numbers_list.count(4) * 4
    elif active == 4:
        score = numbers_list.count(5) * 5
    elif active == 5:
        score = numbers_list.count(6) * 6
    elif active == 6 or active == 7:
        if possible[active]:
                score = sum(numbers_list)
        else:
                score = 0
    elif active == 8:
        if possible[active]:
            score = 25
        else:
            score = 0
    elif active == 9:
        if possible[active]:
            score = 30
        else:
            score = 0
    elif active == 10:
        if possible[active]:
            score = 40
        else:
            score = 0
    elif active == 11:
        if possible[active]:
            score = 50
        else:
            score = 0
    elif active == 12:
        score = sum(numbers_list)
    return score

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def menuButton(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            if action == "Play":
               game_loop(numbers_list, roll, rolls_left, selected, selected_choice, possible, done, scores, totals, clicked, bonus_time, player, something_selected, score, game_over)
            elif action == "Rules":
               rules_page()
            elif action == "Back":
               game_intro()
            elif action == "How to play":
               htp_page()
            elif action == "Example Turn":
               example_page()
            elif action == "Ending a Game":
               end_page()
            elif action == "Scoring":
                scoring_page()
            elif action == "Upper Deck Scoring":
                upperdeckpage()
            elif action == "Lower Deck Scoring":
                lowerdeckpage()
            elif action == "Back to rules":
                rules_page()
            elif action == "Back to menu":
                game_intro()
            elif action =="Restart":
                restart_function()
            elif action == "Nothing":
                print("No more rolls")
            elif action == "Quit":
               pygame.quit()
               quit()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def wordsOnScreen(msg,txtSize,h,y):
    TextSurf, TextRect = text_objects(msg , txtSize)
    TextRect.center = ((WIDTH/2) , (HEIGHT/h + y))
    screen.blit(TextSurf, TextRect)

def rules_page():
    topText = "The Rules of"
    bottomText = "YAHTZEE"

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        wordsOnScreen(topText, midText, 8, -50)
        wordsOnScreen(bottomText, largeText, 4, -50)

        mouse = pygame.mouse.get_pos()

        Back = menuButton("Back", left, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, green, "Back")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        Howtoplay = menuButton('How to Play' , 225 , 250 , 150 , menuButtonHeight, black , green , 'How to play')
        Scoring = menuButton('Scoring' , centered, 350, menuButtonWidth , menuButtonHeight, black, green, 'Scoring')
        Ending = menuButton('Ending a Game', 220, 450 , 160, menuButtonHeight , black , green , 'Ending a Game')
        ExampleTurn = menuButton('Example Turn' , 225 , 550 , 150 , menuButtonHeight , black , green , 'Example Turn')

        pygame.display.update()
        timer.tick(15)

def htp_page():
    htpTitle = "HOW TO PLAY"
    one = "Each player takes one score card."
    two ="On your turn, you may roll dice up to 3 times."
    three = "Although you may stop and score after your 1st or 2nd roll."
    four = "After the 1st or 2nd roll, you can decide"
    five = "to keep any number of dice and reroll the rest."
    six = "After 3 rolls, or you are happy with your dice"
    seven = "you can now score on the score sheet."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(htpTitle, midText, 4, 0)
        wordsOnScreen(one, smallText, 3, 0)
        wordsOnScreen(two, smallText, 3, 40)
        wordsOnScreen(three, smallText, 3, 60)
        wordsOnScreen(four, smallText, 3, 100)
        wordsOnScreen(five, smallText, 3, 120)
        wordsOnScreen(six, smallText, 3, 160)
        wordsOnScreen(seven, smallText, 3, 180)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def example_page():
    exampleTitle = "EXAMPLE TURN"
    one = "First Roll: 2, 3, 4, 4, 5"
    two ="You could reroll for a 3 of a Kind,"
    three ="a 4 of a Kind, or a Large Straight."
    four = "You already have a Small Straight, so you could reroll a 4"
    five = "in the hopes of getting a 1 or 6. So you reroll a 4."
    six = "Second Roll: 2, 2, 3, 4, 5"
    seven = "You now could reroll a 2 and go for a Large Straight,"
    eight = "or set the Twos aside and roll for Twos or 3 of a Kind."
    nine = "You decide to keep the Twos, and reroll the rest"
    ten = "Third Roll: 2, 2, 2, 3, 3" 
    eleven = "You now have to score, and here are your options:"
    twelve = "6 for Twos"
    thirteen = "6 for Threes"
    fourteen = "12 for Three of a Kind"
    fifteen = "25 for Full House"
    sixteen = "You choose the Full House, so you score 25 points."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(exampleTitle, midText, 6, 0)
        wordsOnScreen(one, smallText, 4, 0)
        wordsOnScreen(two, smallText, 4, 20)
        wordsOnScreen(three, smallText, 4, 40)
        wordsOnScreen(four, smallText, 4, 80)
        wordsOnScreen(five, smallText, 4, 100)
        wordsOnScreen(six, smallText, 4, 140)
        wordsOnScreen(seven, smallText, 4, 160)
        wordsOnScreen(eight, smallText, 4, 180)
        wordsOnScreen(nine, smallText, 4, 200)
        wordsOnScreen(ten, smallText, 4, 240)
        wordsOnScreen(eleven, smallText, 4, 260)
        wordsOnScreen(twelve, smallText, 4, 280)
        wordsOnScreen(thirteen, smallText, 4, 300)
        wordsOnScreen(fourteen, smallText, 4, 320)
        wordsOnScreen(fifteen, smallText, 4, 340)
        wordsOnScreen(sixteen, smallText, 4, 380)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def scoring_page():
    scoreTitle = "SCORING"
    first = "When you have finished rolling,"
    second = "decide which box you would like to fill in."
    third = "For each game there are 13 boxes."
    fourth = "You must fill in a box each turn."
    fifth = "If you are not able to fill in a box (or don't want to)"
    sixth = "you must enter a zero in any box."
    seventh = "You can only fill in a box once, so choose carefully."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(scoreTitle, midText, 6, 0)
        wordsOnScreen(first, smallText, 4, 20)
        wordsOnScreen(second, smallText, 4, 40)
        wordsOnScreen(third, smallText, 4, 80)
        wordsOnScreen(fourth, smallText, 4, 100)
        wordsOnScreen(fifth, smallText, 4, 140)
        wordsOnScreen(sixth, smallText, 4, 160)
        wordsOnScreen(seventh, smallText, 4, 200)

        mouse = pygame.mouse.get_pos()

        upperdeck = menuButton('Upper Section' , (WIDTH/2 - 250), 500, 150 , menuButtonHeight, black, green, 'Upper Deck Scoring')
        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def end_page():
    endTitle = "ENDING A GAME"
    first = "Once each player has filled in all 13 boxes, the game ends."
    second = "Each player then adds up their scores as follows:"
    third = "Add all of the Upper section together."
    fourth = "If you get at least 63 points in the Upper section"
    fifth = "you get 35 bonus points."
    sixth = "Add all of the Lower section together."
    seventh = "If you have any bonus YAHTZEEs add them now."
    eighth = "Add total of Upper and Lower sections."
    ninth = "If you have the highest score, you win!"

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(endTitle, midText, 6, 0)
        wordsOnScreen(first, smallText, 4, 0)
        wordsOnScreen(second, smallText, 4, 40)
        wordsOnScreen(third, smallText, 4, 80)
        wordsOnScreen(fourth, smallText, 4, 100)
        wordsOnScreen(fifth, smallText, 4, 120)
        wordsOnScreen(sixth, smallText, 4, 160)
        wordsOnScreen(seventh, smallText, 4, 180)
        wordsOnScreen(eighth, smallText, 4, 220)
        wordsOnScreen(ninth, smallText, 4, 260)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def upperdeckpage():
    udTitle = "UPPER DECK"
    first = "To score in the Upper Section, add only"
    second = "the dice with the same number you are wanting to enter"
    third = "For Example. You roll: 3, 3, 3, 2, 4 "
    fourth = "You could enter one of the following"
    fifth = "9 in the Threes segment"
    sixth ="2 in the Twos segment"
    seventh = "4 in the Fours segment"
    eighth = "If you are able to score 63 points in the Upper section"
    ninth ="you earn 35 bonus points"

    screen.fill(background)
   
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        wordsOnScreen(udTitle, midText, 6, 0)
        wordsOnScreen(first, smallText, 4, 0)
        wordsOnScreen(second, smallText, 4, 20)
        wordsOnScreen(third, smallText, 4, 60)
        wordsOnScreen(fourth, smallText, 4, 80)
        wordsOnScreen(fifth, smallText, 4, 120)
        wordsOnScreen(sixth, smallText, 4, 140)
        wordsOnScreen(seventh, smallText, 4, 160)
        wordsOnScreen(eighth, smallText, 4, 200)
        wordsOnScreen(ninth, smallText, 4, 220)

        mouse = pygame.mouse.get_pos()
        
        lowerdeck = menuButton('Lower Section' , (WIDTH/2 + 100) , 500 , 150, menuButtonHeight , black , green , 'Lower Deck Scoring')
        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

def lowerdeckpage():
    ldTitle = "LOWER DECK"
    first = "To score in the Lower Section"
    second = "the dice have to match the requirements."
    threeofaKind = "3 of a Kind: 3 of any one number."
    tallyTotal = "Tally the total of all your dice."
    fourofaKind = "4 of a Kind: 4 of any one number."
    fullHouse = "Full House: 3 of a Kind and 2 of a Kind."
    twentyFivePoints = "Worth 25 points regardless of dice numbers."
    smStraight = "Small Straight: Any sequence of 4 numbers in order."
    thirtyPoints = "Worth 30 points."
    lgStraight = "Large Straight: Any sequence of 5 numbers in order."
    fortyPoints = "Worth 40 points."
    yahtzee = "YAHTZEE: 5 of any one number."
    fifty = "Worth 50 points"
    bonusYahtzee = "Any additional YAHTZEEs are 100 bonus points each."
    chance = "Chance: All the dice in your hand."
    allDice = "Add the value of all the dice in your hand."

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        wordsOnScreen(ldTitle, midText, 8, -10)
        wordsOnScreen(first, smallText, 6, 0)
        wordsOnScreen(second, smallText, 6, 20)
        wordsOnScreen(threeofaKind, smallText, 6, 60)
        wordsOnScreen(tallyTotal, smallText, 6, 80)
        wordsOnScreen(fourofaKind, smallText, 6, 120)
        wordsOnScreen(tallyTotal, smallText, 6, 140)
        wordsOnScreen(fullHouse, smallText, 6, 180)
        wordsOnScreen(twentyFivePoints, smallText, 6, 200)
        wordsOnScreen(smStraight, smallText, 6, 240)
        wordsOnScreen(thirtyPoints, smallText, 6, 260)
        wordsOnScreen(lgStraight, smallText, 6, 300)
        wordsOnScreen(fortyPoints, smallText, 6, 320)
        wordsOnScreen(yahtzee, smallText, 6, 360)
        wordsOnScreen(fifty, smallText, 6, 380)
        wordsOnScreen(bonusYahtzee, smallText, 6, 400)
        wordsOnScreen(chance, smallText, 6, 440)
        wordsOnScreen(allDice, smallText, 6, 460)

        mouse = pygame.mouse.get_pos()

        Backtor = menuButton("Back to Rules", centered , bottomRulesButton, 135 , menuButtonHeight, black, green, "Back to rules")
        Quit = menuButton("Exit", right, bottomRulesButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")
        mBack = menuButton("Back to menu", left, bottomRulesButton, 135, menuButtonHeight, black, green, "Back to menu")

        pygame.display.update()
        timer.tick(15)

#Draws scorecard outline + buttons
def draw_stuff(rolls_left):
    global game_over
    if game_over:
        menuButton("Rules", centered, topMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Restart")
        #over_text = font.render("Game Over: Click to Restart", True, white)
        #screen.blit(over_text, 280, 290)
    roll_text = font.render("Click To Roll", True, white)
    screen.blit(roll_text, (100, 167))
    accept_text = font.render("Accept Turn", True, white)
    screen.blit(accept_text, (400, 167))
    rolls_text = font.render("Rolls Left: " + str(rolls_left), True, white)
    screen.blit(rolls_text, (15, 15))
    play_text = font.render("Player " + str(player), True, white)
    screen.blit(play_text, (520, 15))
    pygame.draw.rect(screen, white, [0, 200, 225, HEIGHT - 200])
    pygame.draw.line(screen, black, (0, 40), (WIDTH, 40), 3)
    pygame.draw.line(screen, black, (0, 200), (WIDTH, 200), 5)
    pygame.draw.line(screen, black, (155, 200), (155, HEIGHT), 3)
    pygame.draw.line(screen, black, (225, 200), (225, HEIGHT), 3)

##Class for die, includes draw function used to draw each die 1-6.
class Dice:
    def __init__(self, x_pos, y_pos, num, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = num
        global selected
        self.key = key
        self.active = selected[self.key]
        self.die = ''
    ##Draw function that draws each die.    
    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)    
        if self.number == 6:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
        if self.active:
            pygame.draw.rect(screen, (255, 0, 0), [self.x_pos, self.y_pos, 100, 100], 4, 5)
            
    #Checks if die is clicked & adds to the dice_selected list     
    def check_click(self, coordinates):
        if self.die.collidepoint(coordinates):
            if selected[self.key]:
                selected[self.key] = False
            elif not selected[self.key]:
                selected[self.key] = True
##Class for choice, draws table for choices and text for each choice.
class Choice:
    def __init__(self, x_pos, y_pos, text, select, possibles, dones, my_score):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.text = text
        self.selected = select
        self.possible = possibles
        self.done = dones
        self.score = my_score

    def draw(self):
        pygame.draw.line(screen, (0, 0, 0), (self.x_pos, self.y_pos + 31), (self.x_pos + 225, self.y_pos + 31), 2)
        name_text = ''
        if not self.done:
            if self.possible:
                name_text = font.render(self.text, True, (34, 140, 34))
            elif not self.possible:
                name_text = font.render(self.text, True, (255, 0, 0))
        else:
            name_text = font.render(self.text, True, (0, 0, 0))
        if self.selected:
            pygame.draw.rect(screen, (20, 35, 30), [self.x_pos, self.y_pos + 2, 155, 30])
        screen.blit(name_text, (self.x_pos + 5, self.y_pos + 10))
        score_text = font.render(str(self.score), True, (0, 0, 255))
        screen.blit(score_text, (self.x_pos + 165, self.y_pos + 10))

def restart_function():
    global roll
    global numbers_list
    global selected
    global clicked
    global rolls_left
    global scores
    global choice
    global done
    global possible
    global totals
    global something_selected
    global score
    roll = False
    number_list = [7, 8, 9, 10, 11]
    selected = [False, False, False, False, False]
    selected_choice = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    clicked = False
    rolls_left = 3
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    choice = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    done = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    possible = [False, False, False, False, False, False, False, False, False, False, False, False, False]
    totals = [0, 0, 0, 0, 0, 0, 0]
    something_selected = False
    score = 0
    game_over = False
    game_intro()

    
       
def check_possibilities(possible_list, numbers_list):
    ##How does it handle running out of possibliities?
    ##Checks to see if there are any dice that can be kept for each choice
    possible_list[0] = True
    possible_list[1] = True
    possible_list[2] = True
    possible_list[3] = True
    possible_list[4] = True
    possible_list[5] = True
    possible_list[6] = True
    possible_list[7] = True
    possible_list[8] = True
    possible_list[9] = True
    possible_list[10] = True
    possible_list[11] = True
    possible_list[12] = True
    max_count = 0
    ##Max_count is a variable to check for 3, 4, or 5 of a kind.
    for index in range(1, 7):
        if numbers_list.count(index) > max_count:
            max_count = numbers_list.count(index)
    ##Lines 125-148 check for 3, 4, or 5 of a kind
    if max_count >=3:
        possible_list[6] = True
        if max_count >=4:
            possible_list[7] = True
            if max_count >= 5:
                possible_list[11] = True
    
    if max_count < 3:
        possible_list[6] = False
        possible_list[7] = False
        possible_list[8] = False
        possible_list[11] = False
    elif max_count == 3:
        possible_list[7] = False
        possible_list[11] = False
        checker = False
        for index in range(len(numbers_list)):
            if numbers_list.count(numbers_list[index]) == 2:
                possible_list[8] = True
                checker = True
        if not checker:
            possible_list[8] = False
    elif max_count == 4:
        possible_list[11] = False
        
    lowest = 10
    highest = 0
    for index in range(len(numbers_list)):
        if numbers_list[index] < lowest:
            lowest = numbers_list[index]
        if numbers_list[index] > highest:
            highest = numbers_list[index]
    
    if (lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest+3 in numbers_list) and (lowest+4 in numbers_list):
        possible_list[10] = True
    else:
        possible_list[10] = False
        
    if ((lowest + 1 in numbers_list) and (lowest + 2 in numbers_list) and (lowest+3 in numbers_list)) or ((highest - 1 in numbers_list) and (highest - 2 in numbers_list) and (highest-3 in numbers_list)):
        possible_list[9] = True
    else:
        possible_list[9] = False    
        
    return possible_list
        
def make_choice(clicked_num, selected, done_list):
    for index in range(len(selected)):
        selected[index] = False
    if not done_list[clicked_num]:
        selected[clicked_num] = True
    return selected

def check_totals(totals_list, scores_list, my_bonus):
    totals_list[0] = scores_list[0] + scores_list[1] + scores_list[2] + scores_list[3] + scores_list[4] + scores_list[5]
    if totals_list[0] >= 63:
        totals_list[1] = 35
    else:
        totals_list[1] = 0
    totals_list[2] = totals_list[0] + totals_list[1]

    totals_list[4] = scores_list[6] + scores_list[7] + scores_list[8] + scores_list[9] + scores_list[10] + \
        scores_list[11] + scores_list[12]
    totals_list[5] = totals_list[2]
    totals_list[6] = totals_list[4] + totals_list[5]
    if my_bonus:
        totals_list[3] += 100
        my_bonus = False
    return totals_list, my_bonus


def game_intro():
    topText = "Welcome to"
    bottomText = "YAHTZEE"

    screen.fill(background)

    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        wordsOnScreen(topText, midText, 8, 0)
        wordsOnScreen(bottomText, largeText, 4, 0)

        mouse = pygame.mouse.get_pos()

        Rules = menuButton("Rules", centered, topMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Rules")
        Play = menuButton("Play", centered, middleMenuButton, menuButtonWidth, menuButtonHeight, black, green, "Play")
        Quit = menuButton("Exit", centered, bottomMenuButton, menuButtonWidth, menuButtonHeight, black, red, "Quit")

        pygame.display.update()
        timer.tick(15)        

##Main Loop
def game_loop(numbers_list, roll, rolls_left, selected, selected_choice, possible, done, scores, totals, clicked, bonus_time, player, something_selected, score, game_over):
    game_over = False
    running = True
    while running:
        timer.tick(fps)
        screen.fill(background)
        
        if game_over:
            restart_button = menuButton("Return to Menu", centered + 50, topMenuButton + 150, menuButtonWidth + 100, menuButtonHeight, black, green, "Restart")

        ##Draws 5 Die at top of screen
        die1 = Dice(10, 50, numbers_list[0], 0)
        die2 = Dice(130, 50, numbers_list[1], 1)
        die3 = Dice(250, 50, numbers_list[2], 2)
        die4 = Dice(370, 50, numbers_list[3], 3)
        die5 = Dice(490, 50, numbers_list[4], 4)
        
        
        ones = Choice(0, 200, "Ones", selected_choice[0], possible[0], done[0], scores[0])
        twos = Choice(0, 230, "Twos", selected_choice[1], possible[1], done[1], scores[1])
        threes = Choice(0, 260, "Threes", selected_choice[2], possible[2], done[2], scores[2])
        fours = Choice(0, 290, "Fours", selected_choice[3], possible[3], done[3], scores[3])
        fives = Choice(0, 320, "Fives", selected_choice[4], possible[4], done[4], scores[4])
        sixes = Choice(0, 350, "Sixes", selected_choice[5], possible[5], done[5], scores[5])
        upper_total1 = Choice(0, 380, "Total Score", False, False, True, totals[0])
        upper_bonus = Choice(0, 410, "Bonus if >= 63", False, False, True, totals[1])
        upper_total2 = Choice(0, 440, "Upper Total", False, False, True, totals[2])
        three_kind = Choice(0, 470, "Three of a Kind",selected_choice[6], possible[6], done[6], scores[6])
        four_kind = Choice(0, 500, "Four of a Kind", selected_choice[7], possible[7], done[7],  scores[7])
        full_house = Choice(0, 530, "Full House", selected_choice[8], possible[8], done[8], scores[8])
        small_straight = Choice(0, 560, "Small Straight",selected_choice[9], possible[9], done[9], scores[9])
        large_straight = Choice(0, 590, "Large Straight", selected_choice[10], possible[10], done[10], scores[10])
        yahtzee = Choice(0, 620, "Yahtzee",selected_choice[11], possible[11], done[11], scores[11])
        chance = Choice(0, 650, "Chance", selected_choice[12], possible[12], done[12], scores[12])
        yahtzee_bonus = Choice(0, 680, "Yahtzee Bonus", False, False, True, totals[3])
        lower_total = Choice(0, 710, "Lower Total", False, False, True, totals[4])
        lower_total2 = Choice(0, 740, "Upper Total", False, False, True, totals[5])
        grand_total = Choice(0, 770, "Grand Total", False, False, True, totals[6])
        possible = check_possibilities(possible, numbers_list)
        score = check_scores(selected_choice, numbers_list, possible, scores)
        totals, bonus_time = check_totals(totals, scores, bonus_time)
        if True in selected_choice:
            something_selected = True
        
        roll_button = pygame.draw.rect(screen, black, [10, 160, 280, 30])
        accept_button = pygame.draw.rect(screen, black, [310, 160, 280, 30])

        draw_stuff(rolls_left)

        die1.draw()
        die2.draw()
        die3.draw()
        die4.draw()
        die5.draw()
        ones.draw()
        twos.draw()
        threes.draw()
        fours.draw()
        fives.draw()
        sixes.draw()
        upper_total1.draw()
        upper_bonus.draw()
        upper_total2.draw()
        three_kind.draw()
        four_kind.draw()
        full_house.draw()
        small_straight.draw()
        large_straight.draw()
        yahtzee.draw()
        chance.draw()
        yahtzee_bonus.draw()
        lower_total.draw()
        lower_total2.draw()
        grand_total.draw()
    
        ##Event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                die1.check_click(event.pos)
                die2.check_click(event.pos)
                die3.check_click(event.pos)
                die4.check_click(event.pos)
                die5.check_click(event.pos)
                if roll_button.collidepoint(event.pos) and rolls_left > 0:
                    roll = True
                    rolls_left -= 1
                    draw_clicked = 0
                if accept_button.collidepoint(event.pos) and something_selected and rolls_left < 3:
                    if scores[11] == 50 and done[11] and possible[11]:
                        bonus_time = True
                    for i in range(len(selected_choice)):
                        if selected_choice[i]:
                            done[i] = True
                            scores[i] = score
                            selected_choice[i] = False
                    for i in range(len(selected)):
                        selected[i] = False
                    rolls_left = 3
                    numbers_list = [7, 8, 9, 10, 11]
                    something_selected = False
                if 0 <= event.pos[0] <= 155:
                    if 200 <= event.pos[1] <= 380  or 470 <= event.pos[1] <= 680:
                        if 200 < event.pos[1] < 230:
                            clicked = 0
                        if 230 < event.pos[1] < 260:
                            clicked = 1
                        if 260 < event.pos[1] < 290:
                            clicked = 2
                        if 290 < event.pos[1] < 320:
                            clicked = 3
                        if 320 < event.pos[1] < 350:
                            clicked = 4
                        if 350 < event.pos[1] < 380:
                            clicked = 5
                        if 470 < event.pos[1] < 500:
                            clicked = 6
                        if 500 < event.pos[1] < 530:
                            clicked = 7
                        if 530 < event.pos[1] < 560:
                            clicked = 8
                        if 560 < event.pos[1] < 590:
                            clicked = 9
                        if 590 < event.pos[1] < 620:
                            clicked = 10
                        if 620 < event.pos[1] < 650:
                            clicked = 11
                        if 650 < event.pos[1] < 680:
                            clicked = 12
                        selected_choice = make_choice(clicked, selected_choice, done)
    
 
                    
                
        ##Resets roll to false
        if roll:
            for number in range(len(numbers_list)):
                if not selected[number]:
                    numbers_list[number] = random.randint(1, 6)
            roll = False


        

        if False not in done:
            game_over = True        
            
            
        pygame.display.flip()

    
game_intro()
pygame.quit()
