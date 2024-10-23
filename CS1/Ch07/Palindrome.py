"""
A palindrome is a word or a phrase that is the 
same when read both forward and backward. 

Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). 

Write a program whose input is a word or phrase, 
and that outputs whether the input is a palindrome.

Ex: If the input is:

bob
the output is:

palindrome: bob
Ex: If the input is:

bobby
the output is:

not a palindrome: bobby
Hint: Start by removing spaces. Then check if the string equals itself in reverse.


"""

user_input = input("Please enter a word or prhase: ")

test_phrase = user_input.replace(" ", "")

if test_phrase == test_phrase[::-1]:
    print(f"palindrome: {user_input} : {test_phrase}")
else:   
    print(f"not a palindrome: {user_input} : {test_phrase}")

    