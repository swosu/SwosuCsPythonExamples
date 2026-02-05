
"""
Problem 1: Simple Class with Attributes

Goal: Understand what a class is and how objects store data.

Task:
Create a class named Book.

Requirements:

The class should have:

title (string)

author (string)

pages (integer)

Write a constructor (__init__) that sets those values.

In main, create two Book objects using user input.

Store the objects in a list.

Print each book’s information in a readable format.

Why this matters:
If you don’t understand this one, classes will feel like magic later. This problem teaches:

What a class actually holds

How objects are created

How lists can store objects (same idea as storing ints/strings before)
"""

"""
old code:
class Book:
def __init__ (self):
self.title = ""
self.author = ""
self.pages = 0

def addbook(self):
self.title = input("What is the book title: ")
self.author = input("Who is the author: ")
self.pages = input("How many pages: ")

def printbook(self):
Book_list = []


def user_interface():
books = []

while True:
print("1. Add book")
print("2. Print book list")
print("3. Exit")

user_input = input("Select an option: ")

if user_input == "1":
#Used to add books to list.
book = input("Enter book name: ")
books.append(book)

elif user_input == "2":
if not books:
print("No books in list.")
else:
for book in books:
print(book)

elif user_input == "3":
break

else:
print("Invalid selection. Try again.")


if __name__ == "__main__":
#user_interface()
mybook = Book()
mybook.addbook()


"""


