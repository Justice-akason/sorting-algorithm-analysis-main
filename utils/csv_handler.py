import csv
import os


def save_dataset(filename, dataset):

    os.makedirs("results/datasets", exist_ok=True)

    filepath = os.path.join("results", "datasets", filename)

    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Value"])

        for value in dataset:
            writer.writerow([value])


def save_results(results):

    os.makedirs("results", exist_ok=True)

    filepath = os.path.join("results", "experiment_results.csv")

    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "Dataset Size",
                "Bubble Sort Average (ns)",
                "Heap Sort Average (ns)",
                "Faster Algorithm",
            ]
        )

        writer.writerows(results)
