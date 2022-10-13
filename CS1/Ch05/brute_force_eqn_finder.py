"""
Ex:
8x + 7y = 38
and
3x - 5y = -1
have a solution x = 3, y = 2.

Given integer coefficients of two linear equations with variables x and y,
use brute force to find an integer solution for x and y
in the range -10 to 10.

For every value of x from -10 to 10
   For every value of y from -10 to 10
      Check if the current x and y satisfy both equations.
      If so, output the solution, and finish.
"""

x_coeficcient_1 = 8 #int(input('please enter your first coefficient for x.'))
y_coeficcient_1 = 7 #int(input('please enter your first coefficient for y.'))
solution_1 = 38 #int(input('please enter your first constant coefficient.'))

x_coeficcient_2 = 3 #int(input('please enter your second coefficient for x.'))
y_coeficcient_2 = -5 #int(input('please enter your second coefficient for y.'))
solution_2 = -1 #int(input('please enter your second constant coefficient.'))
equation_1_correct = False
equation_2_correct = False
for x_guess in range(-10, 10+1, 1):
    #print(f'x_guess was{x_guess}')
    for y_guess in range(-10, 10+1, 1):
        #print(f'{x_guess} , {y_guess}')
        equation_1_correct = False
        equation_2_correct = False
        output_1 = \
        x_guess * x_coeficcient_1 + \
        y_guess * y_coeficcient_1
        if output_1 == solution_1:
            equation_1_correct = True
            #print(f'equation 1 was correct for ({x_guess}, {y_guess})')
        output_2 = \
        x_guess * x_coeficcient_2 + \
        y_guess * y_coeficcient_2
        if output_2 == solution_2:
            equation_2_correct = True
            #print(f'equation 2 was correct for ({x_guess}, {y_guess})')

        if equation_1_correct and equation_2_correct:
            print(f'we had a match for both with: ({x_guess}, {y_guess})')
            exit()
