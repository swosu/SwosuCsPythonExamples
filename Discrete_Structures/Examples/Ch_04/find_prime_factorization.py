import math
def is_a_prime_number_basic(number_to_check):
    #print(f'number to check is {number_to_check}.')
    is_prime = True
    for check_value in range (2, number_to_check):
        if 0 == number_to_check % check_value:
            is_prime = False
            return is_prime
    return is_prime

if __name__ == '__main__':
    #number_to_work = int(input('what would you like to find the prime factors of?'))
    number_to_work = math.factorial(10)
    print(f'you would like to find the prime factors of: {number_to_work}.')

    prime_factors = []
    print(f'your prime factors so far {prime_factors}')
    working_number = number_to_work # make a copy to play with in our algorithm
    results_check = 1

    while working_number != results_check:

        for number_to_check in range(2, number_to_work):
            #print(f'our number to check is now: {number_to_check}.')
            if 0 == working_number % number_to_check:
                print(f'{working_number} is evenly divisible by {number_to_check}.')
                if is_a_prime_number_basic(number_to_check):
                    prime_factors.append(number_to_check)
                    print(f'your prime factors so far {prime_factors}')
                    working_number = working_number / number_to_check
                else:
                    print('number was not prime.')

    results_check = 1
    for item in prime_factors:
        results_check = results_check * item

    prime_factors.sort()
    print(f'your prime factors are {prime_factors}')
