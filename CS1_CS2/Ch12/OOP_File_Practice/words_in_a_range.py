filename = input("Enter the filename: ")
lower = input("Enter the lower word bound: ")
upper = input("Enter the upper word bound: ")

# open() RETURNS an object
file_obj = open(filename, "r")

# calling a method on the object
words = file_obj.readlines()

# another method
file_obj.close()

for word in words:
    word = word.strip()

    if lower <= word <= upper:
        print(word, "- in range")
    else:
        print(word, "- not in range")


f = open("input1.txt")

print(type(f))
print(type(f).__name__)
f.close()