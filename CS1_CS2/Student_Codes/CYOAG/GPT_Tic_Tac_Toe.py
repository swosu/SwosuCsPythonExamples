import tkinter as tk
import random

# Initialize the game board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Initialize the player and computer markers
player_marker = 'X'
computer_marker = 'O'

# Define the function to check for a win
def check_win(board, marker):
    return ((board[0] == marker and board[1] == marker and board[2] == marker) or
            (board[3] == marker and board[4] == marker and board[5] == marker) or
            (board[6] == marker and board[7] == marker and board[8] == marker) or
            (board[0] == marker and board[3] == marker and board[6] == marker) or
            (board[1] == marker and board[4] == marker and board[7] == marker) or
            (board[2] == marker and board[5] == marker and board[8] == marker) or
            (board[0] == marker and board[4] == marker and board[8] == marker) or
            (board[2] == marker and board[4] == marker and board[6] == marker))

# Define the function to make the computer's move
def computer_move():
    global board
    open_spots = [i for i in range(len(board)) if board[i] == ' ']
    if len(open_spots) > 0:
        move = random.choice(open_spots)
        board[move] = computer_marker
        buttons[move].config(text=computer_marker)
        if check_win(board, computer_marker):
            label.config(text="Computer Wins!")
        elif len([i for i in board if i == ' ']) == 0:
            label.config(text="Tie Game!")
        else:
            label.config(text="Your turn!")
    else:
        label.config(text="Tie Game!")

# Define the function for when the player makes a move
def player_move(index):
    global board
    if board[index] == ' ':
        board[index] = player_marker
        buttons[index].config(text=player_marker)
        if check_win(board, player_marker):
            label.config(text="You Win!")
        elif len([i for i in board if i == ' ']) == 0:
            label.config(text="Tie Game!")
        else:
            computer_move()

# Initialize the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

# Create the game board buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=6, height=3, command=lambda index=i: player_move(index))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create the label for game status
label = tk.Label(root, text="Your turn!", font=('Arial', 14))
label.grid(row=3, column=0, columnspan=3)

# Start the game loop
root.mainloop()
