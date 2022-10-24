upper_dice = [1, 2, 2, 5, 5]
upper_score = [0, 0, 0, 0, 0, 0]
ones = 1
twos = 2
threes = 3
fours = 4
fives = 5
sixes = 6
count=0
for ele in upper_dice:
    if ele == ones:
        count=count+1
        upper_score[0] = count*1
count=0
for ele in upper_dice:
    if ele == twos:
        count=count+1
        upper_score[1] = count*2
count=0
for ele in upper_dice:
    if ele == threes:
        count=count+1
        upper_score[2] = count*3
count=0
for ele in upper_dice:
    if ele == fours:
        count=count+1
        upper_score[3] = count*4
count=0
for ele in upper_dice:
    if ele == fives:
        count=count+1
        upper_score[4] = count*5
count=0
for ele in upper_dice:
    if ele == sixes:
        count=count+1
        upper_score[5] = count*6





print(upper_score)

