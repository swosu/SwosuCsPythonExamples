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
episodes = 3  # keep short for demo

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
    print(f"\n=== Episode {ep+1} ===")

    while not done:
        # --- Decision time ---
        print("\nAnd now we decide where to move.")
        print(f"We are in state {state}.")
        print(f"Our choices are: LEFT (Q={q_table[state,0]:.2f}) or RIGHT (Q={q_table[state,1]:.2f}).")

        # ε-greedy choice
        if random.random() < epsilon:
            action = random.choice(actions)
            action_type = "explore (random choice)"
        else:
            action = np.argmax(q_table[state])
            action_type = "exploit (follow best Q so far)"

        print(f"We make the decision based on ε-greedy: {action_type}.")
        print(f"In the end, we decide to move {'LEFT' if action == 0 else 'RIGHT'}.")

        # Take the step
        next_state, reward, done = step(state, action)

        # --- Update time ---
        old_value = q_table[state, action]
        new_value = old_value + alpha * (
            reward + gamma * np.max(q_table[next_state]) - old_value
        )
        q_table[state, action] = new_value

        print(f"Based on that move, we got reward {reward}.")
        print(f"We update Q[{state},{action}] from {old_value:.2f} → {new_value:.2f}.")
        print("And now we see our Q-table, which makes sense because")
        print("it reflects the slightly better estimate of the future reward:")
        print(q_table)

        # Move to next state
        state = next_state

print("\n=== Final Learned Q-table ===")
print(q_table)
policy = ["←" if np.argmax(row) == 0 else "→" for row in q_table]
print("Learned policy:", policy)
