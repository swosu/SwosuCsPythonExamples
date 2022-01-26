"""
Programming Exam: Develop a collection of four different rules for generating
the terms of a sequence. Generate a program for randomly selecting a rule,
and a starting point. Give the user the first four terms of the sequence,
and ask them for the fifth. Tell them if they were correct or not.
"""
print('hello')


def function_one():
    print(' here is our first sequence')
    how_many_numbers_to_print = 5
    initial_term = 4
    common_difference = 2
    for index in range(how_many_numbers_to_print):
        #print('our index is:',index)
        next_term = initial_term + common_difference * index
        print('for index:', index, ' our term is:', next_term)
    next_term = initial_term + common_difference * how_many_numbers_to_print
    print('for the first sequence, the next term is', next_term)
    return next_term

print(' here is our second sequence is Fibonacci')
f_of_zero = 0
print(f_of_zero, end='')
print(' first term in sequence is f of zero ')


f_of_one = 1
print(f_of_one, end='')
print(' second term in sequence is f of one ')

#print('calculate the third term, f of two.')
f_of_two = f_of_one + f_of_zero
print(f_of_two, end='')
print(' third term in sequence is f of two ')


#print('calculate the fourth term, f of three.')
f_of_n_minus_two = f_of_one
f_of_n_minus_one = f_of_two
f_of_n = f_of_n_minus_one + f_of_n_minus_two
print(f_of_n, end='')
print(' fourth term in sequence is f of three ')

f_of_n_minus_two = f_of_n_minus_one
f_of_n_minus_one = f_of_n
f_of_n = f_of_n_minus_one + f_of_n_minus_two
print(f_of_n, end='')
print(' fifth term in sequence is f of four ')

print('our third sequence is n squared')
how_many_numbers_to_print = 5
for index in range(how_many_numbers_to_print):
    next_term =  index * index
    print('for index:', index, ' our term is:', next_term)

print('our fourth sequence is n factorial')
import math
for index in range(how_many_numbers_to_print):
    next_term = math.factorial( index )
    print('for index:', index, ' our term is:', next_term)

print('\n\nstarting the quiz part.')
next_term = 42

function_index = 1
if 1 == function_index:
    next_term = function_one()
    print('after function call, next term is', next_term)

user_answer = input('what is the next term?')

print('you entered:', user_answer)

if(user_answer ==  str(next_term)):
    print('you were correct')
else:
    print('you were not correct')
