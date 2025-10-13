# 💥 7.6 LAB: Name Format - Super Verbose Python Version 💥
# by Jeremy & ChatGPT

# 🧠 REMINDER: In Python, strings are OBJECTS created from the 'str' CLASS.
# For example: name = "Blossom" → creates an OBJECT (instance) of the 'str' CLASS.

# Let's start!

# Step 1️⃣: Take user input (this creates a new str OBJECT)
full_name = input("Enter full name: ")  # object of class str
print(type(full_name))  # confirms it's <class 'str'>

# Step 2️⃣: Split the string into parts (this calls a method defined in str class)
name_parts = full_name.split()  # split() returns a LIST object (another class!)
# The result is something like ['Pat', 'Silly', 'Doe']

# Step 3️⃣: Determine number of name parts
if len(name_parts) == 3:
    first, middle, last = name_parts
    formatted_name = f"{last}, {first[0]}.{middle[0]}."
elif len(name_parts) == 2:
    first, last = name_parts
    formatted_name = f"{last}, {first[0]}."
else:
    formatted_name = "Invalid input format"

# Step 4️⃣: Output the result
print(formatted_name)

# 🧩 Bonus Learning Section: Peeking Inside the str CLASS
print("\n--- STRING CLASS INSPECTION ---")
print("Type of full_name:", type(full_name))  # tells us it's <class 'str'>
print("Available methods in str class (truncated view):")
print(dir(str)[:10], "...")  # shows first 10 methods of the class

# You can learn more by using:
# help(str)  # <-- try this interactively, it shows class docstring & method details

# 🧪 Let's also show off a few powerful str methods
example = "  blossom rocks!  "
print("\n--- STR METHOD DEMO ---")
print("Original:", repr(example))
print("After strip():", example.strip())  # removes whitespace
print("Uppercase:", example.upper())      # all caps
print("Title Case:", example.title())     # capitalizes each word
print("Replace 'rocks' with 'rules':", example.replace("rocks", "rules"))
print("Does it start with 'blo'? ->", example.strip().startswith("blo"))

# 🦸‍♀️ Now, let’s do the Powerpuff Cast Exercise!

print("\n--- POWERPUFF CAST FORMATTING ---")

# Each name is a string object!
powerpuff_cast = [
    "Blossom Commander Leader",
    "Bubbles Joy Balloons",
    "Buttercup Tough Fighter",
    "Mojo Jojo Villainous Genius",
    "Him Sinister Enchanter",
    "Professor Utonium Supportive Scientist"
]

# Process each name using our earlier logic
for hero in powerpuff_cast:
    parts = hero.split()
    if len(parts) == 3:
        first, middle, last = parts
        formatted = f"{last}, {first[0]}.{middle[0]}."
    elif len(parts) == 2:
        first, last = parts
        formatted = f"{last}, {first[0]}."
    else:
        formatted = f"{parts[-1]}, {parts[0][0]}."
    
    print(f"{hero:<40} → {formatted}")

# ✨ End of the verbose exploration
# 💬 TIP: Explore str in interactive mode
# >>> dir(str)
# >>> help(str.upper)
# >>> help(str.split)
