""" 
Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2. 
Given integer coefficients of two linear equations with variables x and y, 
use brute force to find an integer solution for x and y in the range -10 to 10.

For every value of x from -10 to 10
   For every value of y from -10 to 10
      Check if the current x and y satisfy both equations. If so, output the solution, and finish.
"""

x_1 = 8 #int(input('please enter your first coefficient for x.'))
y_1 = 7 #int(input('please enter your first coefficient for y.'))
c_1 = 38 #int(input('please enter your first constant coefficient.'))

x_2 = 3 #int(input('please enter your second coefficient for x.'))
y_2 = -5 #int(input('please enter your second coefficient for y.'))
c_2 = -1 #int(input('please enter your second constant coefficient.'))

for x_guess in range(-10, 10+1, 1):
    #print(f'x_guess was{x_guess}')
    for y_guess in range(-10, 10+1, 1):
        print(f'{x_guess} , {y_guess}')

        # test the first equation. 
        # if it matches, test the second equation
        # if both mathc, then print result.