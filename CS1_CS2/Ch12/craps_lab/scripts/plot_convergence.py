import pandas as pd
import matplotlib.pyplot as plt


def plot_convergence():

    df = pd.read_csv("data/convergence.csv")

    plt.figure(figsize=(10,6))

    plt.plot(df["games"], df["house_edge"], label="Simulated House Edge")

    plt.axhline(
        y=0.01414,
        linestyle="--",
        label="True House Edge (1.414%)"
    )

    plt.title("Monte Carlo Convergence of Craps Pass Line House Edge")

    plt.xlabel("Number of Games Simulated")
    plt.ylabel("House Edge")

    plt.legend()

    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    plot_convergence()