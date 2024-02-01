def double_the_number(our_initial_number):
    new_number = 2 * our_initial_number
    return new_number

def double_test_number(input_number):
    output_number = 2 * input_number
    return output_number

def print_hello_function ():
    print('hello inside a function')
    
    
def repeated_print_hello_function(number_of_times_to_repeat):
    for index in range(number_of_times_to_repeat):
        #print(f'index is: {index}')
        print(f'hello from inside the repeated for loop {index+1}')

print('hello')
print_hello_function()
escargot = 4
repeated_print_hello_function(escargot)
our_initial_number = 10
our_new_number = double_the_number(our_initial_number)

print(f'our answer was: {our_new_number}')

test_number = 2
test_number = double_test_number(test_number)
print(f'after the double function, test number is {test_number}.')


def go_find_pi():
    return 3

def go_square_radius( radius):
    radius_squared = radius * radius
    return radius_squared

def go_find_area(thing1, thing2):
    stuff = thing1 * thing2
    return stuff
    


# Area = pi * radius squared

our_pi_value = go_find_pi()

radius = 2
radius_squared = go_square_radius( radius)
Area = go_find_area(our_pi_value, radius_squared)

print(f'our area is: {Area}')