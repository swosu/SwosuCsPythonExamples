import itertools
import random
import time

# Define winning combinations
WINNING_COMBOS = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9},  # rows
    {1, 4, 7}, {2, 5, 8}, {3, 6, 9},  # columns
    {1, 5, 9}, {3, 5, 7}              # diagonals
]

def print_board(board):
    print("\nCurrent Board:")
    for i in range(1, 10, 3):
        row = [board.get(j, str(j)) for j in range(i, i+3)]
        print(" | ".join(row))
        if i < 7:
            print("--+---+--")
    print()

def get_available_positions(board):
    return [i for i in range(1, 10) if i not in board]

def evaluate_moves(board, computer_moves, user_moves):
    available = get_available_positions(board)
    evaluations = {}
    for move in available:
        potential = computer_moves | {move}
        count = sum(1 for combo in WINNING_COMBOS if combo.issuperset(potential))
        block = sum(1 for combo in WINNING_COMBOS if combo.issuperset(user_moves | {move}))
        evaluations[move] = {"win_potential": count, "block_potential": block}
    return evaluations

def computer_choose_move(board, computer_moves, user_moves):
    evaluations = evaluate_moves(board, computer_moves, user_moves)
    
    print("Computer is evaluating moves...")
    time.sleep(1)
    for pos, evals in evaluations.items():
        print(f" - Square {pos}:")
        print(f"     Win potential: {evals['win_potential']}")
        print(f"     Block potential: {evals['block_potential']}")
    print()

    input("Press Enter to let the computer make its move...")

    # Simple decision logic: prioritize block, then win
    best_move = max(evaluations.items(), key=lambda x: (x[1]['block_potential'], x[1]['win_potential']))
    return best_move[0]

def check_winner(moves):
    for combo in WINNING_COMBOS:
        if combo.issubset(moves):
            return True
    return False

def play_game():
    board = {}
    user_moves = set()
    computer_moves = set()

    print("Welcome to Tic Tac Toe!")
    print("You are O. Press keys 1-9 to place your mark.")
    print("Positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    for turn in range(9):
        print_board(board)
        if turn % 2 == 0:
            # User's turn
            while True:
                try:
                    move = int(input("Your move (1-9): "))
                    if move not in range(1, 10):
                        print("Choose a number from 1 to 9.")
                        continue
                    if move in board:
                        print("That spot is already taken.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")
            board[move] = 'O'
            user_moves.add(move)
            if check_winner(user_moves):
                print_board(board)
                print("You win! 🎉")
                return
        else:
            move = computer_choose_move(board, computer_moves, user_moves)
            board[move] = 'X'
            computer_moves.add(move)
            if check_winner(computer_moves):
                print_board(board)
                print("Computer wins! 🤖")
                return

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    play_game()
