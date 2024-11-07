"""
24.1 LAB: Acronyms
An acronym is a word formed from the initial letters of words in a set phrase. 
Write a program whose input is a phrase and whose output is an acronym of the input. 
Append a period (.) after each letter in the acronym. 
If a word begins with a lower case letter, don't include that letter in the acronym. 
Assume the input has at least one upper case letter.

Ex: If the input is:

Institute of Electrical and Electronics Engineers
the output is:

I.E.E.E.
Ex: If the input is:

Association for computing MACHINERY
the output is:

A.M.
Although the letters ACHINERY in MACHINERY are upper case, 
those letters are omitted for being a part of the word MACHINERY.

Hint: Use isupper() to check if a letter is upper case.
"""



if __name__ == '__main__':
    phrase = input('please enter a phrase: ')
    acronym = ''
    tokens = phrase.split()
    for word in tokens:
        print('our token is: ', word)
        if word[0].isupper():
            acronym += word[0] + '.'
            print('now our acronym is: ', acronym)
        else:
            print('skipping this word')
    
    print('our acronym is:')
    print(acronym)