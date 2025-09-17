import csv
import os

def write_results_csv(filename, rows, header=None):
    """Append rows of results to a CSV file, writing a header if new."""
    file_exists = os.path.isfile(filename)
    with open(filename, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header or rows[0].keys())
        if not file_exists:
            writer.writeheader()
        writer.writerows(rows)
