import time
import random
import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta

def flip_coin():
    return random.choice(['H', 'T'])

def simulate_batches(p, n, r):
    successful_batches = 0

    for _ in range(r):
        sequence = ''.join([flip_coin() for _ in range(n)])
        
        if 'H' * p in sequence:
            successful_batches += 1

    return successful_batches, successful_batches / r

def plot_and_save_results(results, filename):
    p_values = set(result['p'] for result in results)
    
    for p in p_values:
        data = [result for result in results if result['p'] == p]
        n_values = [result['n'] for result in data]
        probabilities = [result['probability'] for result in data]

        plt.plot(n_values, probabilities, label=f'p={p}')

    plt.xlabel('Number of Coin Flips (n)')
    plt.ylabel('Probability of Getting p Heads in a Row')
    plt.legend()
    plt.title('Coin Flipping Simulation')
    plt.grid(color='lightgrey', linestyle='-', linewidth=0.5, alpha=0.1)
    plt.savefig(filename)
    plt.show()

def main():
    p_values = [2, 3, 4]
    
    max_duration = 120  # 2 minutes

    results = []

    for p in p_values:
        for n in range(p - 1, 24):
            start_time = time.time()
            r = p * n * 2
            #r = 4
            successful_batches, probability = simulate_batches(p, n, r)

            end_time = time.time()
            elapsed_time = end_time - start_time

            # Convert elapsed time to seconds and minutes
            elapsed_time_seconds = int(elapsed_time)
            elapsed_time_minutes = str(timedelta(seconds=elapsed_time))

            results.append({
                'p': p,
                'n': n,
                'r': r,
                'q': successful_batches,
                'probability': probability,
                'elapsed_time_seconds': elapsed_time_seconds,
                'elapsed_time_minutes': elapsed_time_minutes
            })

            print(f"Completed: p={p}, n={n}, Time: {elapsed_time_minutes}")

            # Play a notification sound
            print('\a')  # This will produce a terminal beep sound

            # Check if the total duration has exceeded the maximum allowed duration
            if elapsed_time_seconds > max_duration:
                print(f"Maximum duration exceeded. Stopping for p={p}, n={n}")
                break

    # Save results to CSV
    csv_filename = 'coin_flip_results.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['p', 'n', 'r', 'q', 'probability', 'elapsed_time_seconds', 'elapsed_time_minutes']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    # close csv file
    csvfile.close()

    # Plot and save results
    plot_and_save_results(results, 'coin_flip_plot.png')

if __name__ == "__main__":
    main()

    # make a ding at the end of the program
    print('\a')  # This will produce a terminal beep sound