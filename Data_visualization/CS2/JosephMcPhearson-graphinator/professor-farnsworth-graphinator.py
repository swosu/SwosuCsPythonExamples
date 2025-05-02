import random
import matplotlib.pyplot as plt
import pandas as pd


# Function to generate random shipment data
def generate_data(num_shipments=50):
    weights = [random.uniform(5, 50) for _ in range(num_shipments)]
    costs = [weight * random.uniform(8, 12) for weight in weights]
    data = {
        "Date": pd.date_range(start="2025-01-01", periods=num_shipments, freq="D"),
        "Weight (kg)": weights,
        "Cost ($)": costs,
        "Destination": [
            random.choice(
                ["Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Omicron Persei 8"]
            )
            for _ in range(num_shipments)
        ],
    }
    return pd.DataFrame(data)


# Generate shipment data
shipment_data = generate_data()


# Function to plot Weight vs Cost
def plot_weight_vs_cost(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Weight (kg)"], data["Cost ($)"], c="blue", alpha=0.7)
    plt.title("Weight vs Cost of Intergalactic Shipments")
    plt.xlabel("Weight (kg)")
    plt.ylabel("Cost ($)")
    plt.grid(True)
    plt.show()


# Function to plot Shipments per Destination
def plot_shipments_per_destination(data):
    plt.figure(figsize=(10, 6))
    destination_counts = data["Destination"].value_counts()
    destination_counts.plot(kind="bar", color="purple", alpha=0.7)
    plt.title("Number of Shipments to Each Planet")
    plt.xlabel("Destination Planet")
    plt.ylabel("Number of Shipments")
    plt.grid(axis="y")
    plt.show()


# Main function to visualize data
def visualize_data(data):
    while True:
        print("\nWelcome to Professor Farnsworth's Graphinator 3000!")
        print("1. View Weight vs Cost of Intergalactic Shipments")
        print("2. View Number of Shipments to Each Planet")
        print("3. Exit the Graphinator")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            plot_weight_vs_cost(data)
        elif choice == "2":
            plot_shipments_per_destination(data)
        elif choice == "3":
            print("Good news, everyone! You've exited the Graphinator!")
            break
        else:
            print("Invalid choice. Try again, meatbag!")


# Call the main function
visualize_data(shipment_data)