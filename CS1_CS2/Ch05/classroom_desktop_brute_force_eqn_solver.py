eq_1_x_coef = 8
eq_1_y_coef = 7
eq_1_solution = 38
eq_1_match = False

eq_2_x_coef = 3
eq_2_y_coef = -5
eq_2_solution = -1
eq_2_match = False

found_solution = False
x_solution = -1000
y_solution = -1000

for x_guess in range (-10, 10):
    
    for y_guess in range (-10, 10):
        
        #print(f'(x guess, y guess): ({x_guess}, {y_guess})')
        
        eq_1_result = eq_1_x_coef * x_guess + eq_1_y_coef * y_guess
        if eq_1_solution == eq_1_result:
            eq_1_match = True
            print('\nWE HAD A MATCH!!!, ', end = '')
            print('for equation 1, ', end = '')
            print(f'for (x,y) of ({x_guess},{y_guess}, ', end ='')
            print(f'result was {eq_1_result} which matches {eq_1_solution}')
        else:
            eq_1_match = False
            print('for equation 1, ', end = '')
            print(f'for (x,y) of ({x_guess},{y_guess}, ', end ='')
            print(f'result was {eq_1_result} not {eq_1_solution}')
            
        eq_2_result = eq_2_x_coef * x_guess + eq_2_y_coef * y_guess
        if eq_2_solution == eq_2_result:
            eq_2_match = True
            print('\nWE HAD A MATCH!!!, ', end = '')
            print('for equation 2, ', end = '')
            print(f'for (x,y) of ({x_guess},{y_guess}, ', end ='')
            print(f'result was {eq_2_result} which matches {eq_2_solution}')
        else:
            eq_2_match = False
            print('for equation 2, ', end = '')
            print(f'for (x,y) of ({x_guess},{y_guess}, ', end ='')
            print(f'result was {eq_2_result} not {eq_2_solution}')
            
        if eq_1_match and eq_2_match:
            x_solution = x_guess
            y_solution = y_guess
            found_solution = True
            
if found_solution:
    print(f'solution is: x = {x_solution}, y = {y_solution}')
else:
    print(f'no solution was found')
            
