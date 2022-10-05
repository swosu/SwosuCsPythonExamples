''' Read in first equation, ax + by = c '''
a = int(input())
b = int(input())
c = int(input())

''' Read in second equation, dx + ey = f '''
d = int(input())
e = int(input())
f = int(input())

solution_found = False
   
for x in range(-10,11):
    for y in range(-10,11):
        eqn_1_solved = ( (a*x + b*y) == c )
        eqn_2_solved = ( (d*x + e*y) == f )
        if eqn_1_solved and eqn_2_solved:
            solution_found = True
            x_solution = x
            y_solution = y
            # Note: Could insert break here
   
if solution_found:
    print('x =', x_solution, ', y =', y_solution)
else:
    print('There is no solution')
