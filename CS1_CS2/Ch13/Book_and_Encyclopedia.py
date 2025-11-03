# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 13:22:51 2023

@author: evertj
"""

class Book:
    
    def __init__(self):
        self.data = []
        self.fan = ''
        self.__title = ''
        
        
    def set_title(self, user_given_title):
        self.__title = user_given_title
        
    def get_title(self):
        return self.__title
    
    def print_info(self):
        print(f'the title is: {self.__title}.')
    
class Encyclopedia (Book):
    
    def __init__(self):
        self.data = []
        self.__edition = ''
        self.__page_count = 0
        
    def set_edition(self, user_given_edition):
        self.__edition = user_given_edition
        
    def get_edition(self):
        return self.__edition
    
    def set_page_numbers(self, user_given_page_count):
        self.__page_count = user_given_page_count
        
    def get_page_numbers(self):
        return self.__page_count
    
    def print_info(self):
        print('ha, and you think I am going to tell you? Crazy!!!')

if __name__ == '__main__':
    print('welcome to books and encyclopedias.')
    
    my_book = Book()
    my_book.set_title('Going Postal')
    #print(f'the book title is: {my_book.__title}.')
    #AttributeError: 'Book' object has no attribute '__title'
    print(f'the book title is: {my_book.get_title()}.')
    my_book.fan = 'jeremy'
    print(f'who is a fan of the book? {my_book.fan}.')
    
    my_book.print_info()
    
    my_encyclopedia = Encyclopedia()
    my_encyclopedia.set_title('Disc World')
    print(f'the encyclopedia title is: {my_encyclopedia.get_title()}.')
    my_encyclopedia.set_edition('fourty second edition')
    print(f'the edition of the encyclopedia is: {my_encyclopedia.get_edition()}.')
    my_encyclopedia.set_page_numbers('42000')
    print(f'the page count of the encyclopedia is: {my_encyclopedia.get_page_numbers()}.')
    
    my_encyclopedia.print_info()
    
    
    
    
    #