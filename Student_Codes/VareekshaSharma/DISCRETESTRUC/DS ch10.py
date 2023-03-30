"""Construct knight's tours on chessboards of various sizes.
doing this one  ^^^

OR

Find the shortest path a traveling salesperson can take to visit 
each of the capitals of the 50 states in the United States traveling 
by air between cities in a straight line, visiting each city only 
once and stopping back at the city you began with.

OR

Discuss the applications of graph theory to sociology and psychology

OR

Explain what the area of graph mining, an important area of data 
mining, is and describe some of the basic techniques used in graph mining."""
import random

def get_next_moves(board_size, row, col, visited):
    moves = []
    # print('made list')
    for r, c in [(row + 2, col + 1), (row + 2, col - 1), (row - 2, col + 1), (row - 2, col - 1),
                 (row + 1, col + 2), (row + 1, col - 2), (row - 1, col + 2), (row - 1, col - 2)]:
        if 0 <= r < board_size and 0 <= c < board_size and visited[r][c] == 0:
            moves.append((r, c))
            # print('append to list')
    # print(moves)
    return moves

def knight_tour(board_size):
    board = [[0 for col in range(board_size)] for row in range(board_size)]
    visited = [[0 for col in range(board_size)] for row in range(board_size)]
    visited[0][0] = 1
    row, col = 0, 0
    move_number = 1
    # print('move 1')
    while move_number < board_size**2:
        next_moves = get_next_moves(board_size, row, col, visited)
        if next_moves:
            valid_moves = []
            for r, c in next_moves:
                if len(get_next_moves(board_size, r, c, visited)) <= 1:
                    valid_moves.append((r, c))
            if valid_moves:
                r, c = valid_moves[0]
            else:
                r, c = random.choice(next_moves)
            visited[r][c] = 1
            board[r][c] = move_number
            move_number += 1
            row, col = r, c
            # print('end of if in while loop')
        else:
            break
        # print("breaking statement")
    print(board)
    for sublist in board:
        print(sublist)


if __name__ == "__main__":
    user_input = int(input("enter board size: "))
    # get_next_moves()
    knight_tour(user_input)
