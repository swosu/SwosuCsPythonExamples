sentence = "  the quick brown fox  "
print(sentence)
print(sentence.strip())
print(sentence.title())
print(sentence.replace("fox", "dog"))
print(sentence.count("o"))

help(str)

print("and here is something different just about replace")

help(sentence.replace)

print("getting help for just replace not tied to an object")

help(str.replace)