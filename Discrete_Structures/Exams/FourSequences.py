"""
Programming Exam: Develop a collection of four different rules for generating
the terms of a sequence. Generate a program for randomly selecting a rule,
and a starting point. Give the user the first four terms of the sequence,
and ask them for the fifth. Tell them if they were correct or not.
"""
print('hello')
how_many_numbers_to_print = 5

print(' here is our first sequence')
initial_term = 4
common_difference = 2
for index in range(how_many_numbers_to_print):
    #print('our index is:',index)
    next_term = initial_term + common_difference * index
    print('for index:', index, ' our term is:', next_term)

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
