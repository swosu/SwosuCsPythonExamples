#https://www.geeksforgeeks.org/python-decimal-to-binary-list-conversion/

def get_user_input ():
    user_input = int(input('what is a number? '))
    return user_input

def convert_number_to_array(decimal_number):
    result = []
    for index in list('{0:0b}'.format(decimal_number)):
        #print(f'our index is: {index}')
        result.append(index)
    return result

def find_bitwise_and(first_array, second_array):
    bitwise_and = []
    if len(first_array) == len(second_array):
        for index in range(0, len(first_array)):
            #print(first_array[index], end = ', ')
            #print(second_array[index], end = ', ')
            #print()

            if(first_array[index] == second_array[index]):
                #print('we had a match!')
                if('1' == first_array[index]):
                    #print('and it was a 1!')
                    bitwise_and.append('1')
                else:
                    bitwise_and.append('0')
            else:
                bitwise_and.append('0')

    else:
        print('fix zero padding...')
    
    return bitwise_and

            

if __name__ == '__main__':
    print('first number')
    user_input_1 = get_user_input()

    print('second number')
    user_input_2 = get_user_input()

    print(f'you entered {user_input_1} and {user_input_2}.')

    first_array = convert_number_to_array(user_input_1)
    print('our first array', end = '')
    print(first_array)

    second_array = convert_number_to_array(user_input_2)
    print('our second array', end = '')
    print(second_array)

    bitwise_and_result = find_bitwise_and(first_array, second_array)
    print(f'bitwise_and results {bitwise_and_result}')

