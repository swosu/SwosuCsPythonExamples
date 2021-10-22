

""" This code follows Example 16 of Section 4.3"""
def calc_gcd(num1,num2):
    print('we will find the gcd of', str(num1), 'and', str(num2))
    if(num2 == 0):
        print('we had a zero for the second number')
        return num1
    else:
        print('we need to break it down')
        print('first number is', num2)
        print('second number becomes', num1, '%', num2,\
         '=',num1%num2)
        return calc_gcd(num2,num1%num2)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

result = calc_gcd(num1,num2)
print("GCD is : {}".format(result))
