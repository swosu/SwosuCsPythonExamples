
import re

secret_code = {
    "a": "e",
    "b": "u",
    "c": "p",
    "d": "h",
    "e": "o",
    "f": "r",
    "g": "i",
    "h": "c",
    "i": "a",
    "j": "b",
    "k": "d",
    "l": "f",
    "m": "g",
    "n": "j",
    "o": "k",
    "p": "l",
    "q": "m",
    "r": "n",
    "s": "q",
    "t": "s",
    "u": "t",
    "v": "w",
    "w": "v",
    "x": "z",
    "y": "x",
    "z": "y",
}

def Encrypt(message):    
    message = message.lower()
    message = message.replace(" ", "")
    message = re.sub(r'[^\w\s]','',message)
    message = re.sub(r'\d+', '', message)
    Message = []
    for letter in message:
        Message.append(letter)
    for letter in Message:
        if letter in secret_code:
            message = message.replace(letter, secret_code[letter])
    print(f'Your encrypted message is: {message}')


if __name__ == '__main__':
    
    message = input("Please enter the message you want to encrypt: ")
    Encrypt(message)
    print("This message is safe to send.")
