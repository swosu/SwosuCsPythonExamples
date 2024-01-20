#1)

24.3 LAB: Fun with characters
Complete the check_character() function which has 2 parameters: A string, and a specified index. The function checks the character at the specified index of the string parameter, and returns a string based on the type of character at that location indicating if the character is a letter, digit, whitespace, or unknown character.

Ex: The function calls below with the given arguments will return the following strings:

check_character('happy birthday', 2) returns "Character 'p' is a letter"
check_character('happy birthday', 5) returns "Character ' ' is a white space"
check_character('happy birthday 2 you', 15) returns "Character '2' is a digit"
check_character('happy birthday!', 14) returns "Character '!' is unknown"


Starter Code

def check_character(word, index):
    # Type your code here.
      
      if __name__ == '__main__': 
          print(check_character('happy birthday', 2))
              print(check_character('happy birthday', 5))
                  print(check_character('happy birthday 2 you', 15))
                      print(check_character('happy birthday!', 14))

                      #2)

                       

                       24.6 LAB: Parsing dates
                       Write a program to read dates from input, one date per line. Each date's format must be as follows: March 1, 1990. Any date not following that format is incorrect and should be ignored. The input ends with -1 on a line alone. Output each correct date as: 3/1/1990.

                       Hint: Use string[start:end] to get a substring when parsing the string and extracting the date. Use the split() method to break the input into tokens.

                       Ex: If the input is:

                       March 1, 1990
                       April 2 1995
                       7/15/20
                       December 13, 2003
                       -1
                       then the output is:

                       3/1/1990
                       12/13/2003


                       Starter Code

                       def get_month_as_int(monthString):

                           if monthString == 'January':
                                   month_int = 1
                                       elif monthString == 'February':
                                               month_int = 2
                                                   elif monthString == 'March':
                                                           month_int = 3
                                                               elif monthString == 'April':
                                                                       month_int = 4
                                                                           elif monthString == 'May':
                                                                                   month_int = 5
                                                                                       elif monthString == 'June':
                                                                                               month_int = 6
                                                                                                   elif monthString == 'July':
                                                                                                           month_int = 7
                                                                                                               elif monthString == 'August':
                                                                                                                       month_int = 8
                                                                                                                           elif monthString == 'September':
                                                                                                                                   month_int = 9
                                                                                                                                       elif monthString == 'October':
                                                                                                                                               month_int = 10
                                                                                                                                                   elif monthString == 'November':
                                                                                                                                                           month_int = 11
                                                                                                                                                               elif monthString == 'December':
                                                                                                                                                                       month_int = 12
                                                                                                                                                                           else:
                                                                                                                                                                                   month_int = 0

                                                                                                                                                                                       return month_int


                                                                                                                                                                                       user_string = input()

                                                                                                                                                                                       # TODO: Read dates from input, parse the dates to find the one
                                                                                                                                                                                       #       in the correct format, and output in m/d/yyyy format

                                                                                                                                                                                       #3)

                                                                                                                                                                                       24.10 LAB: Warm up: Parsing strings
                                                                                                                                                                                       (1) Prompt the user for a string that contains two strings separated by a comma. (1 pt)

                                                                                                                                                                                       Examples of strings that can be accepted:
                                                                                                                                                                                       Jill, Allen
                                                                                                                                                                                       Jill , Allen
                                                                                                                                                                                       Jill,Allen
                                                                                                                                                                                       Ex:

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       Jill, Allen

                                                                                                                                                                                       (2) Report an error if the input string does not contain a comma. Continue to prompt until a valid string is entered. Note: If the input contains a comma, then assume that the input also contains two strings. (2 pts)

                                                                                                                                                                                       Ex:

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       Jill Allen
                                                                                                                                                                                       Error: No comma in string.

                                                                                                                                                                                       Enter input string: Jill, Allen

                                                                                                                                                                                       (3) Using string splitting, extract the two words from the input string and then remove any spaces. Output the two words. (2 pts)

                                                                                                                                                                                       Ex:

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       Jill, Allen
                                                                                                                                                                                       First word: Jill
                                                                                                                                                                                       Second word: Allen

                                                                                                                                                                                       (4) Using a loop, extend the program to handle multiple lines of input. Continue until the user enters q to quit. (2 pts)

                                                                                                                                                                                       Ex:

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       Jill, Allen
                                                                                                                                                                                       First word: Jill
                                                                                                                                                                                       Second word: Allen

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       Golden , Monkey
                                                                                                                                                                                       First word: Golden
                                                                                                                                                                                       Second word: Monkey

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       Washington,DC
                                                                                                                                                                                       First word: Washington
                                                                                                                                                                                       Second word: DC

                                                                                                                                                                                       Enter input string:
                                                                                                                                                                                       q
