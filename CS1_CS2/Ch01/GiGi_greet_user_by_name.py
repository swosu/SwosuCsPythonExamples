import time

def flash_text(text):
    
    for i in range(5):
        print("\033[1;31m" + text + "\033[0m", end="\r")
        time.sleep(0.5)
        print(" " * len(text), end="\r")
        time.sleep(0.5)

name = input("Enter your name: ")
print("Hello, " + name + "! Welcome!")
flash_text(name )
