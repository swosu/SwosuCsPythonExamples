#https://www.w3schools.com/python/python_user_input.asp

# from website:
#username = input("Enter username:")
#print("Username is: " + username)

#Terminal output:
#Enter username:jeremy
#Username is: jeremy
# PS C:\Users\EvertJ>

# this did not get me the full story.
# I needed it to be an integer.
# so I went to:
# https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/
# and they had this:
# type cast into integer
#input_a = int(input_a)
# this will make sure we store our inputs as integers and not strings.


# From Book:
# x = Get next input
# y = Get next input
# z = x + y
# Put z to output

x = int(input("Please enter a number:"))
y = int(input("Please enter a second number:"))
z = x + y
print('the sum of the two numbers you entered is:', z)
