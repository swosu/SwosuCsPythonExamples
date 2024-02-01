def is_valid_move(board, x, y, move_number, board_size):
    # Check if the move is within the board and the cell is not visited
    if 0 <= x < board_size and 0 <= y < board_size and board[x][y] == -1:
        return True
    return False

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print("\n")

def knight_tour(board_size):
    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
    move_number = 0

    # Possible moves for a knight (2 cells in one direction, 1 cell in the other)
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Start from the top-left corner (you can choose any other starting position)
    board[0][0] = move_number

    def solve_knight_tour(x, y, move_number):
        if move_number == board_size * board_size - 1:
            return True

        for i in range(len(move_x)):
            next_x = x + move_x[i]
            next_y = y + move_y[i]

            if is_valid_move(board, next_x, next_y, move_number, board_size):
                board[next_x][next_y] = move_number + 1
                print('our current move number is: ', move_number )
                print_board(board)
                if solve_knight_tour(next_x, next_y, move_number + 1):
                    return True

                # Backtrack
                board[next_x][next_y] = -1

        return False

    if solve_knight_tour(0, 0, move_number):
        print("Knight's Tour on a", board_size, "x", board_size, "chessboard:")
        print_board(board)
    else:
        print("No solution found.")

# Example usage:
knight_tour(5)  # Change the board size as desired
