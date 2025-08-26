import random
import time

# Tic Tac Toe board
board = [" " for _ in range(9)]

# Mapping of positions to grid
def print_board():
    display = ""
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        display += row + "\n"
        if i < 2:
            display += "---------\n"
    print(display)

def print_positions():
    print("Board Positions (1-9):")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")

# Check for winner
def check_winner(b, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    return any(all(b[pos] == player for pos in combo) for combo in win_combos)

def get_empty_positions(b):
    return [i for i in range(9) if b[i] == " "]

# Simple heuristic: how many winning combos a square contributes to
def evaluate_move_scores(b, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    scores = {}
    for pos in get_empty_positions(b):
        score = 0
        for combo in win_combos:
            if pos in combo:
                marks = [b[i] for i in combo]
                if marks.count(player) == 1 and marks.count(" ") == 2:
                    score += 1
                elif marks.count(player) == 2 and marks.count(" ") == 1:
                    score += 3
        scores[pos] = score
    return scores

# Computer selects move with best score
def get_computer_move(b):
    scores = evaluate_move_scores(b, "X")
    print("\nComputer evaluating moves:")
    for pos, score in scores.items():
        print(f" Position {pos+1}: score {score}")
    best_move = max(scores, key=scores.get)
    input(f"\nComputer will place 'X' at position {best_move+1}. Press Enter to confirm...")
    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe! You are 'O'. Computer is 'X'.")
    print_positions()
    current_player = "O"

    while True:
        print_board()
        if current_player == "O":
            while True:
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if board[move] == " ":
                        board[move] = "O"
                        break
                    else:
                        print("That spot is already taken.")
                except (ValueError, IndexError):
                    print("Invalid input. Choose a number from 1 to 9.")
        else:
            move = get_computer_move(board)
            board[move] = "X"

        if check_winner(board, current_player):
            print_board()
            print(f"{'You' if current_player == 'O' else 'Computer'} won!")
            break
        elif " " not in board:
            print_board()
            print("It's a tie!")
            break
        else:
            current_player = "X" if current_player == "O" else "O"

if __name__ == "__main__":
    play_game()
