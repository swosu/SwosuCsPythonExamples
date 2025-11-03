import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from bs4 import BeautifulSoup
import os  # Added os import for relative path handling

# Define window
window = None

# Define heart_image 
heart_image = None

# Define white_photo
white_photo = None

# Define hearts list to store heart labels
hearts = []

# Define hearts_label
hearts_label = None

def check_guess():
    global lives

    guess_str = guess_entry.get()

    try:
        guess = int(guess_str)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")
        return

    if guess < 1 or guess > word_count * word_count / 2:
        messagebox.showerror("Invalid Input", "Please enter a number within the specified range.")
    elif guess == word_count:
        messagebox.showinfo("Congratulations", f'You guessed correctly. "{search_query.get()}" appears {word_count} times on the first page of Reddit.')
    elif guess < word_count:
        messagebox.showinfo("Try Again", "Try a higher number.")
        lives -= 1
    else:
        messagebox.showinfo("Try Again", "Try a lower number.")
        lives -= 1

    if lives < 0:
        messagebox.showinfo("Game Over", "You've run out of lives. Game over.")
        window.destroy()
    else:
        update_hearts_display()  # Update the hearts display

def update_hearts_display():
    global white_photo 

    if white_photo is None:
        white_image = Image.new('RGBA', heart_image.size, (255, 255, 255, 255))
        white_photo = ImageTk.PhotoImage(white_image)

    for i, heart_label in enumerate(hearts):
        if i < lives:
            heart_image_tk = ImageTk.PhotoImage(heart_image)
            heart_label.configure(image=heart_image_tk)
            heart_label.image = heart_image_tk  # Retain a reference to the PhotoImage
        else:
            heart_label.configure(image=white_photo)

    # Attach the white_photo to the hearts_label to prevent it from being garbage collected
    hearts_label.white_photo = white_photo

    window.update_idletasks()
 

def main():
    global search_query, word_count, search_label, guess_entry, lives, window, heart_image, hearts_label

    # Create a Tkinter window
    window = tk.Tk()
    window.title("Reddit Search Guessing Game")

    # Load the heart image using PIL with a relative path
    heart_image = Image.open("heart.jpg")
    heart_photo = ImageTk.PhotoImage(heart_image)

    # Create and configure labels
    search_query_label = tk.Label(window, text="Enter a search query:")
    search_query_label.pack()

    search_query = tk.StringVar()  # Variable to store the search query
    search_entry = tk.Entry(window, textvariable=search_query)
    search_entry.pack()

    guess_entry = tk.Entry(window)

    search_label = tk.Label(window, text="")

  #LIVES ARE HERE ()()()()()()()()()()()()()()()()
    lives = 10  # You can change this number

    # Create a label for hearts
    hearts_label = tk.Label(window)
    hearts_label.pack()

    for _ in range(lives):
        heart_label = tk.Label(hearts_label, image=heart_photo)
        heart_label.grid(row=0, column=_)
        hearts.append(heart_label)

    def start_game():
        global search_query, word_count, lives

        #Removed, might attempt to implement at a future date
        #lives = 10  # Supposed to Reset the lives when a new game starts

        query = search_query.get()
        if not query:
            messagebox.showerror("Missing Input", "Please enter a search query.")
            return
        
        #Copy Pasted Reddit Search from Oddesy Assignment

        url = f'https://www.reddit.com/search/?q={query}'

        # Set a User-Agent header to mimic a web browser request
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the text on the page
            page_text = soup.get_text()
            word_count = page_text.lower().count(query.lower())

            # Configure labels for search query and guess
            search_label.config(text=f'Search query: {query}')
            guess_label.config(text=f'Guess how many times "{query}" appears on the first page of Reddit:')

            # Make Stuff Exist Visibly
            search_label.pack()
            guess_label.pack()
            guess_entry.pack()
            check_button.pack()

            # Reset the heart labels'
            for heart in hearts:
                heart.grid()

            update_hearts_display()  # Call the function to display the hearts

        else:
            messagebox.showerror('Failed to Retrieve Webpage', 'Failed to retrieve the webpage.')

    start_button = tk.Button(window, text="Start Game", command=start_game)
    start_button.pack()

    guess_label = tk.Label(window, text="")

    check_button = tk.Button(window, text="Check Guess", command=check_guess)

    window.mainloop()

if __name__ == "__main__":
    main()