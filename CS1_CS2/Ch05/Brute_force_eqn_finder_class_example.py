''' Read in first equation, ax + y_1_coefficienty = c '''
x_1_coefficient = int(input())
y_1_coefficient = int(input())
function_1_solution = int(input())

''' Read in second equation, dx + ey = f '''
x_2_coefficient = int(input())
y_2_coefficient = int(input())
function_2_solution = int(input())

solution_found = False
   
for x in range(-10,11):
    for y in range(-10,11):
        eqn_1_solved = ( (x_1_coefficient*x + y_1_coefficient*y) == function_1_solution )
        eqn_2_solved = ( (x_2_coefficient*x + y_2_coefficient*y) == function_2_solution )
        if eqn_1_solved and eqn_2_solved:
            solution_found = True
            x_solution = x
            y_solution = y
            # Note: Could insert break here
   
if solution_found:
    print(f'x = { x_solution } , y = { y_solution }')
else:
    print('There is no solution')