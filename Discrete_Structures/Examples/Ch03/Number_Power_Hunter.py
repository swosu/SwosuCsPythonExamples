print('hello')
import math

def calculate_left_side_number(number):
    partial_result = math.pow(number, 2)
    final_result = math.pow(partial_result, 100)
    return final_result

def calculate_right_side_number(number):
    result = math.pow(2, number)
    return result



if __name__ == "__main__":
    print("hello")
    number = 1
    while True:
        number = number + 1
        print('our number is ', number, end = ' ')
        left_side_number = calculate_left_side_number(number)
        print('left side number is ', left_side_number, end = ' ')
        right_side_number = calculate_right_side_number(number)
        print('right side number is ', right_side_number)
        if left_side_number < right_side_number:
            print('left side is smaller')
            break

    print('number is ', number)
