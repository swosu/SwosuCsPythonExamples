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
Print "Error" if par is not 3, 4, or 5.

Ex: If the input is:

4
3
the output is:

Birdie

Starter code from book:
''' Type your code here. '''
"""

strokes_used = 6
par_for_the_hole = 4

par_minus_strokes = par_for_the_hole - strokes_used
print(f'''You used {strokes_used}.
The hole par was: {par_for_the_hole}.
Par minus strokes was: {par_minus_strokes}.''')

if 2 == par_minus_strokes:
    print("Eagle")
    print("This means: number of strokes is two less than par")

elif 1 == par_minus_strokes:
    print("Birdie")
    print("This means: number of strokes is one less than par")

elif 0 == par_minus_strokes:
    print("Par")
    print("This means: number of strokes equals par")

elif -1 == par_minus_strokes:
    print("Bogey")
    print("This means: number of strokes is one more than par ")

else:
    print('something has gone wrong.')
