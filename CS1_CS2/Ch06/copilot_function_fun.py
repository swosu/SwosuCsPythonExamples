def make_sure_the_box_works():
    print('hello from inside the function')

def print_hello_repeating(number_of_repeats):
    for index in range(number_of_repeats):
        #print(f'index is: {index}')
        print(f'hello from inside the repeated for loop {index+1}')

def how_many_cats_does_Wyatt_have():
    number_of_cats_Wyatt_has = int(2)
    return number_of_cats_Wyatt_has


if __name__ == '__main__':

    cat_count_Wyatt = how_many_cats_does_Wyatt_have()
    print(f'Wyatt has {cat_count_Wyatt} cats.')


    """"
    make_sure_the_box_works()
    for repeated_call_index in range(3):
        print(f'hello from inside the for loop {repeated_call_index+1}')
        print_hello_repeating(2)
        print_hello_repeating(5)
    """

