import time
from collections import deque
import os

def print_board(board_size, knight_pos, target_pos):
    """Draw the board with the knight (K) and target (T)."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for animation
    for row in range(board_size):
        line = ""
        for col in range(board_size):
            if (row, col) == knight_pos:
                line += " K "
            elif (row, col) == target_pos:
                line += " T "
            else:
                line += " . "
        print(line)
    print()  # Blank line after board


def find_knight_path(board_size, target_row, target_col):
    """Find and return the shortest path from (0,0) to (target_row, target_col)."""
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    start_pos = (0, 0)
    queue = deque([(start_pos, [start_pos])])
    visited = {start_pos}
    
    while queue:
        (current_row, current_col), path = queue.popleft()
        
        if (current_row, current_col) == (target_row, target_col):
            return path  # Found the path
        
        for dr, dc in knight_moves:
            new_row, new_col = current_row + dr, current_col + dc
            if 0 <= new_row < board_size and 0 <= new_col < board_size:
                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append(((new_row, new_col), path + [(new_row, new_col)]))
    return None  # No path found (shouldn't happen)


def knight_travel_animation():
    # --- Get user input for board size and target ---
    board_size = int(input("Enter board size (e.g. 8 for 8x8): "))
    target_row = int(input(f"Enter target row (0–{board_size-1}): "))
    target_col = int(input(f"Enter target column (0–{board_size-1}): "))
    
    # --- Find the path ---
    path = find_knight_path(board_size, target_row, target_col)
    if not path:
        print("No path found!")
        return
    
    # --- Animate the path ---
    for position in path:
        print_board(board_size, position, (target_row, target_col))
        time.sleep(0.3)  # Delay between moves
    
    print(f"✅ Knight reached target at {path[-1]} in {len(path)-1} moves!")


# Run it!
knight_travel_animation()
#timer start and ends
# Start timer, run the animation, then print end time and elapsed duration
start_ts = time.time()
start_perf = time.perf_counter()
print("Start:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_ts)))

knight_travel_animation()

end_ts = time.time()
end_perf = time.perf_counter()
print("End:  ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_ts)))
print(f"Elapsed: {end_perf - start_perf:.2f} seconds")
