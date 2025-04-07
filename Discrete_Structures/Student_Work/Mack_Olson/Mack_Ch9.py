import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class Book:
    def __init__(self, title, author, genre, year):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year

    def save_to_db(self):
        conn = sqlite3.connect('books.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS books
                     (title TEXT PRIMARY KEY, author TEXT, genre TEXT, year INTEGER)''')
        c.execute('''UPDATE books SET author = ?, genre = ?, year = ? WHERE title = ?''', 
                  (self.author, self.genre, self.year, self.title))
        if c.rowcount == 0:
            c.execute('''INSERT INTO books (title, author, genre, year)
                         VALUES (?, ?, ?, ?)''', (self.title, self.author, self.genre, self.year))
        conn.commit()
        conn.close()

    @staticmethod
    def fetch_books():
        conn = sqlite3.connect('books.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM books''')
        books = c.fetchall()
        conn.close()
        return books

    @staticmethod
    def fetch_book_by_title(title):
        conn = sqlite3.connect('books.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM books WHERE title = ?''', (title,))
        book = c.fetchone()
        conn.close()
        return book

    @staticmethod
    def delete_book(title):
        conn = sqlite3.connect('books.db')
        c = conn.cursor()
        c.execute('''DELETE FROM books WHERE title = ?''', (title,))
        conn.commit()
        conn.close()

class BookDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Database")
        self.root.geometry("400x550")
        self.root.config(bg="#f0f0f0")
        self.font = ('Arial', 12)

        # Entry fields
        self.title_label = ttk.Label(root, text="Title", font=self.font)
        self.title_label.grid(row=0, column=0, pady=5, padx=10, sticky="e")
        self.title_entry = ttk.Entry(root, font=self.font)
        self.title_entry.grid(row=0, column=1, pady=5, padx=10)

        self.author_label = ttk.Label(root, text="Author", font=self.font)
        self.author_label.grid(row=1, column=0, pady=5, padx=10, sticky="e")
        self.author_entry = ttk.Entry(root, font=self.font)
        self.author_entry.grid(row=1, column=1, pady=5, padx=10)

        self.genre_label = ttk.Label(root, text="Genre", font=self.font)
        self.genre_label.grid(row=2, column=0, pady=5, padx=10, sticky="e")
        self.genre_entry = ttk.Entry(root, font=self.font)
        self.genre_entry.grid(row=2, column=1, pady=5, padx=10)

        self.year_label = ttk.Label(root, text="Year", font=self.font)
        self.year_label.grid(row=3, column=0, pady=5, padx=10, sticky="e")
        self.year_entry = ttk.Entry(root, font=self.font)
        self.year_entry.grid(row=3, column=1, pady=5, padx=10)

        # Buttons
        self.save_button = ttk.Button(root, text="Save Book", command=self.save_book, width=20)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.show_button = ttk.Button(root, text="Show All Books", command=self.show_books, width=20)
        self.show_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.update_button = ttk.Button(root, text="Update Book", command=self.update_book, width=20)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.delete_button = ttk.Button(root, text="Delete Book", command=self.delete_book, width=20)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=5)

        # Search for Book (by Title) to update or delete
        self.search_label = ttk.Label(root, text="Search Title to Modify", font=self.font)
        self.search_label.grid(row=8, column=0, pady=5, padx=10, sticky="e")
        self.search_entry = ttk.Entry(root, font=self.font)
        self.search_entry.grid(row=8, column=1, pady=5, padx=10)

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        year = self.year_entry.get()

        if not title or not author or not genre or not year:
            messagebox.showerror("Input Error", "All fields must be filled!")
            return
        
        book = Book(title, author, genre, int(year))
        book.save_to_db()
        
        messagebox.showinfo("Success", "Book saved successfully!")
        self.clear_entries()

    def show_books(self):
        books = Book.fetch_books()
        if not books:
            messagebox.showinfo("No Books", "No books found in the database.")
            return

        book_list = "\n".join([f"{book[0]} by {book[1]} ({book[2]}, {book[3]})" for book in books])
        messagebox.showinfo("Books in Database", book_list)

    def update_book(self):
        title = self.search_entry.get()
        
        if not title:
            messagebox.showerror("Input Error", "Enter a title to search.")
            return

        existing_book = Book.fetch_book_by_title(title)
        if not existing_book:
            messagebox.showerror("Not Found", f"No book found with title: {title}")
            return
        
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, existing_book[0])

        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, existing_book[1])

        self.genre_entry.delete(0, tk.END)
        self.genre_entry.insert(0, existing_book[2])

        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, existing_book[3])

        self.save_button.config(text="Save Updated Book", command=self.save_book)

    def delete_book(self):
        title = self.search_entry.get()
        if not title:
            messagebox.showerror("Input Error", "Enter a title to delete.")
            return

        existing_book = Book.fetch_book_by_title(title)
        if not existing_book:
            messagebox.showerror("Not Found", f"No book found with title: {title}")
            return

        Book.delete_book(title)
        messagebox.showinfo("Success", f"Book '{title}' deleted successfully!")
        self.clear_entries()

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.genre_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.search_entry.delete(0, tk.END)

# Start the GUI
root = tk.Tk()
app = BookDatabaseApp(root)
root.mainloop()
