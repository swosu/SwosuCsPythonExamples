import numpy as np
import random

# Environment setup
n_states = 5  # positions 0...4
actions = [0, 1]  # 0 = left, 1 = right
q_table = np.zeros((n_states, len(actions)))

# Hyperparameters
alpha = 0.1   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration rate
episodes = 5000

def step(state, action):
    """Environment dynamics"""
    if action == 0:  # left
        next_state = max(0, state - 1)
    else:  # right
        next_state = min(n_states - 1, state + 1)

    reward = -1
    done = False
    if next_state == n_states - 1:  # goal reached
        reward = 10
        done = True
    return next_state, reward, done

# Training loop
for ep in range(episodes):
    state = 0
    done = False
    while not done:
        # ε-greedy choice
        if random.random() < epsilon:
            action = random.choice(actions)
        else:
            action = np.argmax(q_table[state])

        next_state, reward, done = step(state, action)

        # Update Q-table
        old_value = q_table[state, action]
        new_value = old_value + alpha * (
            reward + gamma * np.max(q_table[next_state]) - old_value
        )
        q_table[state, action] = new_value

        state = next_state

# Print final result
print("\n=== Final Learned Q-table after", episodes, "episodes ===")
print(q_table)

policy = ["←" if np.argmax(row) == 0 else "→" for row in q_table]
print("Learned policy:", policy)
