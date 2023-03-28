'''13.10 LAB: Book information (overriding member methods)
Given a Book base class, define a derived class called Encyclopedia with a constructor that initializes the attributes of the Book class as well as new attributes of the following types:

string to store the edition
int to store the number of pages
Within the derived Encyclopedia class, define a print_info() method that overrides the Book class' print_info() method by printing the title, author, publisher, publication date, edition, and number of pages.

Ex: If the input is:

The Hobbit
J. R. R. Tolkien
George Allen & Unwin
21 September 1937
The Illustrated Encyclopedia of the Universe
Ian Ridpath
Watson-Guptill
2001
2nd
384
the output is:

Book Information:
   Book Title: The Hobbit
   Author: J. R. R. Tolkien
   Publisher: George Allen & Unwin
   Publication Date: 21 September 1937
Book Information:
   Book Title: The Illustrated Encyclopedia of the Universe
   Author: Ian Ridpath
   Publisher: Watson-Guptill
   Publication Date: 2001
   Edition: 2nd
   Number of Pages: 384


Starter Code'''

class Book:
    def __init__(self, title, author, publisher, publication_date):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.publication_date = publication_date
   
    def print_info(self):
        print('Book Information:')
        print(f'   Book Title: {self.title}')
        print(f'   Author: {self.author}')
        print(f'   Publisher: {self.publisher}')
        print(f'   Publication Date: {self.publication_date}')


class Encyclopedia(Book):
    # TODO: Define constructor with attributes:
    #       title, author, publisher, publication_date, edition, num_volumes (is it not pages??)
    def __init__(self, title, author, publisher, publication_date, edition, num_pages):
        super().__init__(title, author, publisher, publication_date)
        self.edition = edition
        self.num_pages = num_pages
    
    # TODO: Define a print_info() method that overrides the print_info() in the Book class
    def print_info(self):
        super().print_info()
        print(f'   Edition: {self.edition}')
        print(f'   Page numbers: {self.num_pages}')


if __name__ == "__main__":
    title = input("Enter the name of the book: ")
    author = input("Enter the book author: ")
    publisher = input("Enter the publisher: ")
    publication_date = input("Enter when the book was published: ")
    
    e_title = input("Enter the encyclopidea title: ")
    e_author = input("Enter the author: ")
    e_publisher = input("Enter the publisher name: ")
    e_publication_date = input("Enter the publication date: ")
    edition = input("Enter the edition: ")
    num_pages = int(input("Enter the number of pages: "))
    
    my_book = Book(title, author, publisher, publication_date)
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia(e_title, e_author, e_publisher, e_publication_date, edition, num_pages)
    my_encyclopedia.print_info()