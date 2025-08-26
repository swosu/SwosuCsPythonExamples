def print_decimal(number):
    print(f'that number is {number}.')

def string_to_binary_list_converter(number):
    print(f'number you want to convert is{number}')
    # https://www.geeksforgeeks.org/python-decimal-to-binary-list-conversion/
    res =[ int(i) for i in list('{0:0b}'.format(int(number)))]  
    return res

def convert_binary_to_list(binary_number):
    print(f'number you are trying to convert binary to list {binary_number}')
    binary_list = []
    while binary_number:
        binary_list = [binary_number & 1] + binary_list
        binary_number >>= 1
    return binary_list or [0]


if __name__ == '__main__':
    print('hello')

    number_one = input('please enter your first number: ')
    print_decimal(number_one)

    # number 2 input
    number_two = input('please enter your second number: ')
    print_decimal(number_one)

    # convert decimal to binary
    #bin(number_two)
    binary_1_list = string_to_binary_list_converter(number_one)
    print(f'After conversion, our first binary number is {binary_1_list}.')
    binary_2_list = string_to_binary_list_converter(number_two)
    print(f'After conversion, our second binary number is {binary_2_list}.')
    # convert binary to list
    #list_of_binary_1 = convert_binary_to_list(binary_1)
    #print(list_of_binary_1)
    # do bitwise operations:
  
   