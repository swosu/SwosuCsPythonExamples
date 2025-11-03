from fixture import run_experiment

if __name__ == "__main__":
    sizes = [100, 1000, 5000]   # very small warm-up set
    run_experiment(sizes, runs_per_size=1)
