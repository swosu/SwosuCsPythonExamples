import time


# Function to convert decimal number
# to binary using recursion
def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end = '')


print('Hello and welcome to chapter 04 section 02 example 12')
b = 3000
#b = int(input('please enter a value for b in b^n mod m\n'))
print('you entered ' + str(b) + ' for b.')

n = 644000
#n = int(input('please enter a value for n in b^n mod m\n'))
print('you entered ' + str(n) + ' for n.')

m = 645000
#m = int(input('please enter a value for n in b^n mod m\n'))
print('you entered ' + str(m) + ' for m.')

#print('this is the start of the first algorithm')
start_time_algorithm_5 = time.time()
x = 1
#print('x begins as ' + str(x))

#power = b mod m
power = b % m

#print('power begins as ' + str(power))

#print('now we find the binary expansion of n. n was ' + str(n))

binary_n = bin(n)
#print('in binary, our exponenet is ' + binary_n)
#print('the type of our binary exponenet is ',  type(binary_n))
#print('now we need to split the string on letter b.')
string_binary_n = str(binary_n)
#print('our binary as a string is: ', string_binary_n)

#print('how long is our binary string?')
#print('we need to clip off the leading 0s.')
string_binary_n = string_binary_n.lstrip('0b')
#print('our stripped binary as a string is: ', string_binary_n)
string_binary_n_length = len(string_binary_n)
#print('our string length is ', string_binary_n_length)

# from: https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/
# Calling function
#DecimalToBinary(n)

#print('now we begin our loop.')

for i in range (0,string_binary_n_length):
    right_to_left_bit =  string_binary_n[string_binary_n_length - i -1]
    #print('if i is ', i, ' then our ith bit is ', right_to_left_bit)
    if(str(1) == right_to_left_bit):
        #print('we had a 1 at bit ', i)
        x = (x * power) % m
        #print('at loop iteration ', i, ' x has become ', x)

    power = (power*power) % m
    #print('at loop iteration ', i, ' power has become ', power)

print('after the algorithm, x is ', x   )

stop_time_algorithm_5 = time.time()



start_time_python_default = time.time()
print(pow(b,n)%m)
stop_time_python_default = time.time()

print(' time to complete algorithm 5 was: ', "--- %s seconds ---" % (stop_time_algorithm_5 - start_time_algorithm_5))
print(' time to complete default operation was: ', "--- %s seconds ---" % (stop_time_python_default - start_time_python_default))
