#extract the two words from the input string and then remove any spaces. Output the two words.

def main():
    text = input('please enter text: ')
    text = text.split()
    
    for word in text:
        print(word, end='')



main()