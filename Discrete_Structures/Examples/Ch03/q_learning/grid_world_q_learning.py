import numpy as np
import random

# Grid setup
n_rows, n_cols = 4, 4
n_states = n_rows * n_cols
actions = ["UP", "DOWN", "LEFT", "RIGHT"]

def state_to_rc(s):
    return divmod(s, n_cols)  # (row, col)

def rc_to_state(r, c):
    return r * n_cols + c

goal_state = rc_to_state(3, 3)

# Q-table
q_table = np.zeros((n_states, len(actions)))

# Hyperparameters
alpha = 0.1   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration rate
episodes = 5000

def step(state, action):
    """Take an action and return (next_state, reward, done)."""
    if state == goal_state:
        return state, 0, True

    r, c = state_to_rc(state)

    if action == "UP":
        r = max(0, r - 1)
    elif action == "DOWN":
        r = min(n_rows - 1, r + 1)
    elif action == "LEFT":
        c = max(0, c - 1)
    elif action == "RIGHT":
        c = min(n_cols - 1, c + 1)

    next_state = rc_to_state(r, c)

    reward = -1
    done = False
    if next_state == goal_state:
        reward = 10
        done = True

    return next_state, reward, done

# Training loop
for ep in range(episodes):
    state = 0  # always start top-left
    done = False
    while not done:
        # ε-greedy action
        if random.random() < epsilon:
            action_idx = random.randint(0, len(actions) - 1)
        else:
            action_idx = np.argmax(q_table[state])

        action = actions[action_idx]
        next_state, reward, done = step(state, action)

        old_value = q_table[state, action_idx]
        new_value = old_value + alpha * (
            reward + gamma * np.max(q_table[next_state]) - old_value
        )
        q_table[state, action_idx] = new_value

        state = next_state

# Build policy
policy_grid = []
value_grid = np.zeros((n_rows, n_cols))

arrow_map = {"UP":"↑", "DOWN":"↓", "LEFT":"←", "RIGHT":"→"}

for s in range(n_states):
    r, c = state_to_rc(s)
    if s == goal_state:
        policy_grid.append("G")  # goal
        value_grid[r, c] = 0
    else:
        best_action = actions[np.argmax(q_table[s])]
        policy_grid.append(arrow_map[best_action])
        value_grid[r, c] = np.max(q_table[s])

# Reshape into 4x4
policy_grid = np.array(policy_grid).reshape((n_rows, n_cols))

print("\n=== Learned Policy (arrows) ===")
for row in policy_grid:
    print(" ".join(row))

print("\n=== State Value Heatmap (approx. V) ===")
print(np.round(value_grid, 2))
