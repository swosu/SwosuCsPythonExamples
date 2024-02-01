import tkinter as tk

# Initialize the game board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

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

# Define the function to make a move
def make_move(index, marker):
    global board
    if board[index] == ' ':
        board[index] = marker
        buttons[index].config(text=marker)
        if check_win(board, marker):
            label.config(text=f"{names[marker]} Wins!")
            for button in buttons:
                button.config(state=tk.DISABLED)
        elif len([i for i in board if i == ' ']) == 0:
            label.config(text="Tie Game!")
        else:
            if marker == 'X':
                label.config(text=f"{names['O']}'s turn")
            else:
                label.config(text=f"{names['X']}'s turn")

# Define the function for when a button is clicked
def button_click(index):
    global current_player
    make_move(index, current_player)
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

# Initialize the GUI
root = tk.Tk()
root.title("Tic Tac Toe")

# Ask for player names
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")
names = {'X': player1, 'O': player2}

# Create the game board buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=6, height=3, command=lambda index=i: button_click(index))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# Create the label for game status
current_player = 'X'
label = tk.Label(root, text=f"{names[current_player]}'s turn", font=('Arial', 14))
label.grid(row=3, column=0, columnspan=3)

# Start the game loop
root.mainloop()
