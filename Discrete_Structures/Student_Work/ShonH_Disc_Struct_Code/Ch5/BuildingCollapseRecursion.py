import time
import random
import os
import sys

# ============================================================
# Recursive ASCII Building Collapse Simulation with Gravity
# ============================================================

def create_building(num_rows, num_cols):
    """Create a rectangular grid representing a building (1 = intact)."""
    return [[1 for _ in range(num_cols)] for _ in range(num_rows)]


def display_building(building_grid):
    """Clear the console and draw the building using ASCII blocks."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in building_grid:
        print(''.join('#' if cell == 1 else ' ' for cell in row))
    print()
    sys.stdout.flush()


def apply_damage(building_grid, row, col, impact_force):
    """
    Recursively apply damage to the building starting at (row, col).
    Each destroyed block spreads half of its force to its four neighbors.
    """
    # --- Base cases ---
    if row < 0 or row >= len(building_grid) or col < 0 or col >= len(building_grid[0]):
        return
    if building_grid[row][col] == 0:
        return
    if impact_force < 1:
        return

    # --- Random destruction check ---
    threshold = random.uniform(0.0, 1.0)
    if (impact_force / 10.0) > threshold:
        # Block destroyed
        building_grid[row][col] = 0

        # Show progress
        display_building(building_grid)
        time.sleep(0.01)

        # Propagate destruction to neighboring blocks
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            apply_damage(building_grid, row + dr, col + dc, impact_force * 0.6)

        # Trigger gravity collapse for blocks above
        apply_gravity(building_grid, row - 1, col)
    else:
        # Not destroyed, just weakened
        pass


def apply_gravity(building_grid, row, col):
    """
    Recursive gravity check:
    If a block is above empty space, it 'falls' down one row.
    This can cause additional chain collapses.
    """
    if row < 0 or col < 0 or row >= len(building_grid) or col >= len(building_grid[0]):
        return

    # Stop if current cell is empty
    if building_grid[row][col] == 0:
        return

    below_row = row + 1
    # If below is within bounds and empty -> block falls
    if below_row < len(building_grid) and building_grid[below_row][col] == 0:
        building_grid[below_row][col] = building_grid[row][col]
        building_grid[row][col] = 0

        # Visualize movement
        display_building(building_grid)
        time.sleep(0.01)

        # Continue falling if more space below
        apply_gravity(building_grid, below_row, col)

        # After falling, check neighbors for instability
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            apply_gravity(building_grid, row + dr, col + dc)


def simulate_collapse_with_gravity():
    """Main simulation: larger building, impact near lower middle."""
    num_rows, num_cols = 30, 10
    building_grid = create_building(num_rows, num_cols)

    display_building(building_grid)
    print("Initial building created...")
    time.sleep(1.5)

    impact_row = int(num_rows * 0.75)  # lower area of the building
    impact_col = num_cols // 2

    print(f"Applying impact at row {impact_row}, column {impact_col}...")
    time.sleep(1.5)

    apply_damage(building_grid, impact_row, impact_col, impact_force=12)

    print("\nSimulation complete. Final structure:")
    display_building(building_grid)


# ============================================================
# Run simulation
# ============================================================

if __name__ == "__main__":
    simulate_collapse_with_gravity()
