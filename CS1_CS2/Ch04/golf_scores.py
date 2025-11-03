"""
4.19 LAB: Golf scores

Golf scores record the number of strokes used to
get the ball in the hole.
The expected number of strokes varies from
hole to hole and is called par (i.e. 3, 4, or 5).
Each score's name is based on the actual strokes
taken compared to par:


"Eagle": number of strokes is two less than par
"Birdie": number of strokes is one less than par
"Par": number of strokes equals par
"Bogey": number of strokes is one more than par

Given two integers that represent par and
the number of strokes used,
write a program that prints the appropriate score name.
"""


number_of_strokes = int(input())
#number_of_strokes = int(input('please tell me how many strokes you took.'))
#print(f'you said you took {number_of_strokes} strokes.')

par_for_the_hole = int(input())
#par_for_the_hole = int(input('please tell me what is par for this hole.'))
#print(f'you said this hole should take {par_for_the_hole} strokes.')

stroke_difference = par_for_the_hole - number_of_strokes
#print(f'the current stroke difference is {stroke_difference}.')

if 2 == stroke_difference:
    print('Eagle')
    
elif 1 == stroke_difference:
    print('Birdie')
    
elif 0 == stroke_difference:
    print('Par')
    
elif -1 == stroke_difference:
    print('Bogey')
    
else:
    print('Error')
    

