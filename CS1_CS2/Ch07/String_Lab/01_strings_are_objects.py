"""
01_strings_are_objects.py

Purpose:
Explore the idea that a string is not just text —
it is an OBJECT created from the Python 'str' class.

This program helps students discover:

1. Strings have a type
2. Strings belong to a class
3. Strings have behaviors (methods)
4. Strings store data (characters)
"""

print("\n==============================")
print("   STRING OBJECT EXPLORER")
print("==============================\n")


# ---------------------------------------------------
# Step 1 — Create a string object
# ---------------------------------------------------

text = input("Enter some text: ")

print("\nYou entered:")
print(text)


# ---------------------------------------------------
# Step 2 — What TYPE is the object?
# ---------------------------------------------------

print("\nSTEP 1: What type is this object?")

print("type(text) ->", type(text))


# ---------------------------------------------------
# Step 3 — What CLASS created it?
# ---------------------------------------------------

print("\nSTEP 2: What class created this object?")

print("text.__class__ ->", text.__class__)


# ---------------------------------------------------
# Step 4 — What DATA does it contain?
# ---------------------------------------------------

print("\nSTEP 3: Exploring the data inside the object")

print("First character:", text[0] if len(text) > 0 else "No characters")
print("Last character:", text[-1] if len(text) > 0 else "No characters")
print("Length of string:", len(text))


# ---------------------------------------------------
# Step 5 — What BEHAVIORS does it have?
# ---------------------------------------------------

print("\nSTEP 4: What behaviors does this object have?")
print("(Listing a few methods from dir())\n")

methods = [m for m in dir(text) if not m.startswith("_")]

for method in methods[:15]:
    print(method)

print("\n... and many more!")


# ---------------------------------------------------
# Step 6 — Try some behaviors
# ---------------------------------------------------

print("\nSTEP 5: Let's use some behaviors")

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Replace spaces with '-':", text.replace(" ", "-"))


# ---------------------------------------------------
# Final Thought
# ---------------------------------------------------

print("\n==============================")
print("Key Idea:")
print("The variable 'text' is an OBJECT")
print("created from the Python class 'str'")
print("==============================\n")