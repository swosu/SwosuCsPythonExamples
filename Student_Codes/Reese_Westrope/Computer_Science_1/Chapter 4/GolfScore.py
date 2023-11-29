par = int(input('Enter the par for this hole (3,4, or 5):'))
strokes = int(input('Enter the number of strokes you took:'))
score = par - strokes
score_name = ''

if score == 2:
    score_name = 'Eagle'

elif score == 1:
    score_name = 'Birdie'

elif score == 0:
    score_name = 'Par'

elif score == -1:
    score_name = 'Bogey'

print('You scored a',score_name)