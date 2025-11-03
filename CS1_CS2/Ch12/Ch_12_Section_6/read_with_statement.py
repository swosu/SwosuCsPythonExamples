print("Opening myfile.txt")
with open("myfile.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents)
print("File closed automatically after this block!")
