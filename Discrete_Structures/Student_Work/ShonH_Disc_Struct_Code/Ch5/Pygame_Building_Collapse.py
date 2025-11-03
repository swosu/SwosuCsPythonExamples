import pygame
import random
import time
import sys

# ============================================================
# CONFIGURATION
# ============================================================

CELL_SIZE = 10              # Size of each square block (pixels)
ROWS, COLS = 60, 100        # Grid dimensions
INITIAL_FORCE = 20          # Explosion strength
FRAME_DELAY = 0.005         # Seconds between frames for animation

# Colors
COLOR_BG = (25, 25, 25)
COLOR_BLOCK = (220, 60, 60)
COLOR_BROKEN = (40, 40, 40)

pygame.init()
WIDTH, HEIGHT = COLS * CELL_SIZE, ROWS * CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Collapse Simulation — Click to Explode")

# ============================================================
# BUILDING INITIALIZATION (CENTERED TOWER)
# ============================================================

def create_building(rows, cols):
    """Create a tower centered horizontally."""
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    building_width = cols // 3
    start_col = (cols - building_width) // 2
    end_col = start_col + building_width
    for r in range(rows):
        for c in range(start_col, end_col):
            grid[r][c] = 1
    return grid

building_grid = create_building(ROWS, COLS)

# ============================================================
# DRAW FUNCTION
# ============================================================

def draw_building():
    """Render the building grid."""
    screen.fill(COLOR_BG)
    for row in range(ROWS):
        for col in range(COLS):
            if building_grid[row][col] == 1:
                pygame.draw.rect(
                    screen, COLOR_BLOCK,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                )
            else:
                pygame.draw.rect(
                    screen, COLOR_BROKEN,
                    (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
                )
    pygame.display.flip()

# ============================================================
# GRAVITY AND HORIZONTAL SHIFT
# ============================================================

def apply_gravity(row, col):
    """Recursive gravity: blocks fall if air is below."""
    if row < 0 or col < 0 or row >= ROWS or col >= COLS:
        return
    if building_grid[row][col] == 0:
        return

    below_row = row + 1
    if below_row < ROWS and building_grid[below_row][col] == 0:
        building_grid[below_row][col] = 1
        building_grid[row][col] = 0
        draw_building()
        time.sleep(FRAME_DELAY)
        apply_gravity(below_row, col)
        # Neighbor checks for ripple falling
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            apply_gravity(row + dr, col + dc)

def apply_horizontal_shift(row, col, direction):
    """Simulate sideways sliding when supports are gone."""
    target_col = col + direction
    if (0 <= target_col < COLS) and building_grid[row][col] == 1 and building_grid[row][target_col] == 0:
        building_grid[row][target_col] = 1
        building_grid[row][col] = 0
        draw_building()
        time.sleep(FRAME_DELAY)
        # Continue sliding in same direction
        apply_horizontal_shift(row, target_col, direction)

# ============================================================
# DAMAGE / EXPLOSION PROPAGATION
# ============================================================

def apply_damage(row, col, force, side_bias=0.0):
    """Recursive explosion propagation with force decay and sideways bias."""
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        return
    if building_grid[row][col] == 0:
        return
    if force < 1:
        return

    # Random destruction threshold
    threshold = random.uniform(0.0, 1.0)
    if (force / 10.0) > threshold:
        building_grid[row][col] = 0
        draw_building()
        time.sleep(FRAME_DELAY)

        # Propagate to neighboring blocks
        for dr, dc in [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]:
            # Add sideways bias (explosions on one side push harder opposite)
            bias = 1.0
            if dc > 0:
                bias += side_bias  # stronger to right
            elif dc < 0:
                bias -= side_bias  # weaker to left

            new_force = force * bias * 0.75
            apply_damage(row + dr, col + dc, new_force, side_bias)

        # Gravity effect
        apply_gravity(row - 1, col)

        # Small chance to trigger horizontal sliding when low force
        if random.random() < 0.1:
            direction = 1 if side_bias > 0 else -1
            apply_horizontal_shift(row, col, direction)

# ============================================================
# MAIN LOOP
# ============================================================

def run_simulation():
    draw_building()
    print("Click anywhere to create an explosion! Press ESC or close window to quit.")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                impact_row = mouse_y // CELL_SIZE
                impact_col = mouse_x // CELL_SIZE

                # Compute bias: if you click on left half, pushes right; right half, pushes left
                center = COLS // 2
                side_bias = -0.3 if impact_col > center else 0.3

                print(f"Explosion at ({impact_row}, {impact_col}), bias={side_bias:.2f}")
                apply_damage(impact_row, impact_col, INITIAL_FORCE, side_bias)

    pygame.quit()
    sys.exit()

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    run_simulation()
