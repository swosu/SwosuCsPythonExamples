#https://www.geeksforgeeks.org/python-decimal-to-binary-list-conversion/

# Python3 code to demonstrate 
# decimal to binary number conversion
# using format() + list comprehension
  
# initializing number 
test_num = 8
  
# printing original number
print ("The original number is : " + str(test_num))
  
# using format() + list comprehension
# decimal to binary number conversion 
res = [int(i) for i in list('{0:0b}'.format(test_num))]
  
# printing result 
print ("The converted binary list is : " +  str(res))

num_2 = 12
print ("The original second number is : " + str(test_num))

res_2 = [int(i) for i in list('{0:0b}'.format(num_2))]

print ("The second converted binary list is : " +  str(res_2))

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
            print(first_array[index], end = ', ')
            print(second_array[index], end = ', ')
            print()

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

