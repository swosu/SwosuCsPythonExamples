class PlayerScoreCard:
    def __init__(self):
        self.aces = 0
        self.twos = 0
        self.threes = 0
        self.fours = 0
        self.fives = 0
        self.sixs = 0
        self.bonus = 0
        self.threeofakind = 0
        self.fourofakind = 0
        self.fullhouse = 0
        self.smallstraight = 0
        self.largestraight = 0
        self.yahtzee = 0
        self.chance = 0
        self.bonusyahtzee = 0

    def InitiateScores(player):
        player.aces = None
        player.twos = None
        player.threes = None
        player.fours = None
        player.fives = None
        player.sixs = None
        player.bonus = None
        player.threeofakind = None
        player.fourofakind = None
        player.fullhouse = None
        player.smallstraight = None
        player.largestraight = None
        player.yahtzee = None
        player.chance = None
        player.bonusyahtzee = None

listOfScoringOptions = {
    "1) All 1's": 1,
    "2) All 2's": 2,
    "3) All 3's": 3,
    "4) All 4's": 4,
    "5) All 5's": 5,
    "6) All 6's": 6,
    "7) 3 of a kind": 7,
    "8) 4 of a kind": 8,
    "9) Full House": 9,
    "10) Small Straight": 10,
    "11) Large Straight": 11,
    "12) Yahtzee": 12,
    "13) Chance": 13
}

def ChooseScoringOption(player, numbers_list):
    print("What would you like to score your roll as?")
    for options in listOfScoringOptions:
        print(options)
    whatToScoreAs = int(input())
    if whatToScoreAs in listOfScoringOptions.values():
        if whatToScoreAs == 0:
            ScoreAces(player, numbers_list)
        if whatToScoreAs == 1:
            ScoreTwos(player, numbers_list)
        if whatToScoreAs == 2:
            ScoreThrees(player, numbers_list)
        if whatToScoreAs == 3:
            ScoreFours(player, numbers_list)
        if whatToScoreAs == 4:
            ScoreFives(player, numbers_list)
        if whatToScoreAs == 5:
            ScoreSixes(player, numbers_list)
        if whatToScoreAs == 6:
            ScoreThreeOfAKind(player, numbers_list)
        if whatToScoreAs == 7:
            ScoreFourOfAKind(player, numbers_list)
        if whatToScoreAs == 8:
            ScoreFullHouse(player, numbers_list)
        if whatToScoreAs == 9:
            ScoreSmallStraight(player, numbers_list)
        if whatToScoreAs == 10:
            ScoreLargeStraight(player, numbers_list)
        if whatToScoreAs == 11:
            ScoreYahtzee(player, numbers_list)
        if whatToScoreAs == 12:
            ScoreChance(player, numbers_list)
    else:
        print("You did not enter a valid scoring option")

def ScoreAces(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if numberOfEachFace[1] == 0:
        print("You do not have any 1's to score")
        player.aces = 0
    elif numberOfEachFace[1] != 0:
        player.aces = numberOfEachFace[1]
    print(player.aces)
    return player.aces

def ScoreTwos(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if numberOfEachFace[2] == 0:
        print("You do not have any 2's to score")
        player.twos = 0
    elif numberOfEachFace[2] != 0:
        player.twos = numberOfEachFace[2]*2
    print(player.twos)
    return player.twos

def ScoreThrees(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if numberOfEachFace[3] == 0:
        print("You do not have any 3's to score")
        player.threes = 0
    elif numberOfEachFace[3] != 0:
        player.threes = numberOfEachFace[3]*3
    print(player.threes)
    return player.threes

def ScoreFours(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if numberOfEachFace[4] == 0:
        print("You do not have any 4's to score")
        player.fours = 0
    elif numberOfEachFace[4] != 0:
        player.fours = numberOfEachFace[4]*4
    print(player.fours)
    return player.fours

def ScoreFives(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if numberOfEachFace[5] == 0:
        print("You do not have any 5's to score")
        player.fives = 0
    elif numberOfEachFace[5] != 0:
        player.fives = numberOfEachFace[5]*5
    print(player.fives)
    return player.fives

def ScoreSixes(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if numberOfEachFace[6] == 0:
        print("You do not have any 6's to score")
        player.sixs = 0
    elif numberOfEachFace[6] != 0:
        player.sixs = numberOfEachFace[6]*6
    print(player.sixs)
    return player.sixs

def ScoreThreeOfAKind(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if not 3 in numberOfEachFace.values() and not 4 in numberOfEachFace.values() and not 5 in numberOfEachFace.values():
        print("You do not have a valid three of a kind")
        player.threeofakind = 0
    elif 3 in numberOfEachFace.values() or 4 in numberOfEachFace.values() or 5 in numberOfEachFace.values():
        player.threeofakind = sum(numbers_list)
    print(player.threeofakind)
    return player.threeofakind

def ScoreFourOfAKind(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if not 4 in numberOfEachFace.values() and not 5 in numberOfEachFace.values():
        print("You do not have a vaild four of a kind")
    elif 4 in numberOfEachFace.values() or 5 in numberOfEachFace.values():
        player.fourofakind = sum(numbers_list)
    print(player.fourofakind)
    return player.fourofakind

def ScoreFullHouse(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if 3 in numberOfEachFace.values() and 2 in numberOfEachFace.values():
        player.fullhouse = 25
    else:
        print("You do not have a valid Full House")
    print(player.fullhouse)
    return player.fullhouse

def ScoreSmallStraight(player, numbers_list):
    issmallstraight = any(all(numbers_list[roll]+ numberafterroll in numbers_list for numberafterroll in range(1,5)) for roll in range(len(numbers_list)-4))
    if issmallstraight == True:
        print("This is a valid small straight")
        player.smallstraight = 30
    else:
        print("You do not have a valid Small Straight")
        player.smallstraight = 0
    print(player.smallstraight)
    return player.smallstraight

def ScoreLargeStraight(player, numbers_list):
    if sorted(numbers_list) == [1,2,3,4,5]:
        player.largestraight = 40
    elif sorted(numbers_list) == [2,3,4,5,6]:
        player.largestraight = 40
    else:
        print("You do not have a valid Large Straight")
        player.largestraight = 0
    print(player.largestraight)
    return player.largestraight

def ScoreYahtzee(player, numbers_list):
    numberOfEachFace = {}
    for results in numbers_list:
        numberOfEachFace[results] = numberOfEachFace.get(results, 0) + 1
    if 5 in numberOfEachFace.values():
        if player.yahtzee == 50:
            __ScoreBonusYahtzee(player)
        else:
            player.yahtzee = 50
    else:
        print("You do not have a valid Yahtzee")
        player.yahtzee = 0
    print(player.yahtzee)
    return player.yahtzee

def __ScoreBonusYahtzee(player):
    print("For your bonus yahtzee, what spot would you like to put your 100 points in?")
    #Still needs a function to choose from remaining open spots which one to replace with a 100
    player.bonusyahtzee += 100

def ScoreChance(player, numbers_list):
    player.chance = sum(numbers_list)
    print(player.chance)
    return player.chance

if __name__=="__main__":

    Player1 = PlayerScoreCard
    Player2 = PlayerScoreCard
    Player1.InitiateScores(Player1)
    Player2.InitiateScores(Player2)
    numbers_list = [1,1,1,1,1]
    ChooseScoringOption(Player1, numbers_list)
