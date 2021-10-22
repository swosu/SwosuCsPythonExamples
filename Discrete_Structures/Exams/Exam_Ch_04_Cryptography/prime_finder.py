import math
def say_hello():
    print('Hello, and welcome to the prime finder.')

def is_number_prime(number_to_check):
    print('we are going to check if ', number_to_check, ' is prime')
    place_to_stop_looking = math.floor(number_to_check/2)
    print('our place to stop looking was', place_to_stop_looking)
    for divisor_check in range(2, place_to_stop_looking ):
        print('checking if', number_to_check, 'is evenly divisible by',divisor_check )
        if number_to_check % divisor_check == 0:
            print('turns out that', number_to_check, 'was not prime...')
            return False
    print('we found a prime!', number_to_check, 'is prime.')
    return True

def count_primes_less_than(number_range):
    print('we want to know how many numbers less than', \
    number_range, ' are prime')

    number_of_primes = 0;
    for number_to_check in range(2,number_range):
        print('we are looking at ', number_to_check)
        if is_number_prime(number_to_check):
            print('confirmed after the function call, we had a prime')
            number_of_primes += 1
    print('We found ', number_of_primes, 'primes less than', number_range)
