def find_simple_sum(number_to_sum_to):
    #print(f'we are going to sum up to: {number_to_sum_to}.')
    sum = 0
    for our_number in range(1, (number_to_sum_to + 1)):
        #print(f'our number is: {our_number}.')
        #sum = sum + our_number
        sum += our_number
        #print(f'sum is now: {sum}.')
    return sum

if __name__ == '__main__':
    #print('welcome to the problem 5.4.8.')

    user_selected_positive_integer = int(input('what do you want to sum up to?'))
    #print(f'you entered {user_selected_positive_integer}.')

    simple_sum = find_simple_sum(user_selected_positive_integer)
    print(f'the simple function says the sum is: {simple_sum}.')