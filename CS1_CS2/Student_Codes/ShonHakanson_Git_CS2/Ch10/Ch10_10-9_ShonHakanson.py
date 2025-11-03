#Chapter 10 Homwork, Lab 10.9: Exceptions with Lists, Shon Hakanson
#Given a list of 10 names, complete the program that outputs the name specified by the list index entered 
# by the user. Use a try block to output the name and an except block to catch any IndexError exception as a 
# variable. Output "Exception! " followed by the message from the exception variable. Output also the first 
# element in the list if the invalid index is negative or the last element if the invalid index is positive.



names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input("Enter an index: "))

# Type your code here.

try:
    print("Name:", names[index])

except IndexError as error_message:
    print("Exception!", error_message)
    if index < 0:
        print("The closest name is:", names[0])
    else:
        print("The closest name is:", names[-1])