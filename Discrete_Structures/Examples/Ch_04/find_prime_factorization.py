
def is_a_prime_number_basic(number_to_check):
    #print(f'number to check is {number_to_check}.')
    is_prime = True
    for check_value in range (2, number_to_check):
        if 0 == number_to_check % check_value:
            is_prime = False
            return is_prime
    return is_prime

def find_prime_factors(number_to_work):
    working_number = number_to_work # make a copy to play with in our algorithm
    for number_to_check in range(2, number_to_work):
        print(f'our number to check is now: {number_to_check}.')
        if 0 == working_number % number_to_check:
            print(f'{working_number} is evenly divisible by {number_to_check}.')
            if is_a_prime_number_basic(number_to_check):
                prime_factors.append(number_to_check)
                print(f'your prime factors so far {prime_factors}')
                working_number = working_number / number_to_check
            else:
                print('number was not prime.')
                prime_factors.append(find_prime_factors(number_to_check))
    return prime_factors

if __name__ == '__main__':
    number_to_work = int(input('what would you like to find the prime factors of?'))
    print(f'you would like to find the prime factors of: {number_to_work}.')

    prime_factors = []
    prime_factors = find_prime_factors(number_to_work)
    print(f'your prime factors so far {prime_factors}')
