import matplotlib.pyplot as plt
from algorithms.bubble_sort import bubble_sort
from algorithms.heap_sort import heap_sort
from utils.csv_handler import save_dataset, save_results
from utils.dataset import copy_dataset, generate_dataset
from utils.timer import measure_time

# -------------------------------------------------
# Experiment Configuration
# -------------------------------------------------

DATASET_SIZES = [1000, 5000, 10000, 15000, 20000, 25000]

NUMBER_OF_RUNS = 5

results = []

bubble_graph = []
heap_graph = []


# -------------------------------------------------
# Start Experiment
# -------------------------------------------------

print("\n")
print("=" * 60)
print("SORTING ALGORITHM PERFORMANCE ANALYSIS")
print("=" * 60)
print(f"Datasets : {DATASET_SIZES}")
print(f"Runs per dataset : {NUMBER_OF_RUNS}")
print("=" * 60)


for size in DATASET_SIZES:
    print("\n")
    print("=" * 60)
    print(f"Testing Dataset Size: {size:,}")
    print("=" * 60)

    dataset = generate_dataset(size)

    save_dataset(f"dataset_{size}.csv", dataset)

    bubble_times = []
    heap_times = []

    for run in range(NUMBER_OF_RUNS):
        bubble_dataset = copy_dataset(dataset)
        heap_dataset = copy_dataset(dataset)

        _, bubble_time = measure_time(bubble_sort, bubble_dataset)

        _, heap_time = measure_time(heap_sort, heap_dataset)

        bubble_times.append(bubble_time)
        heap_times.append(heap_time)

        print(f"Run {run + 1}/{NUMBER_OF_RUNS} completed.")

    bubble_average = sum(bubble_times) / NUMBER_OF_RUNS
    heap_average = sum(heap_times) / NUMBER_OF_RUNS

    bubble_graph.append(bubble_average)
    heap_graph.append(heap_average)
    winner = "Bubble Sort"

    if heap_average < bubble_average:
        winner = "Heap Sort"

    results.append([size, round(bubble_average), round(heap_average), winner])

    print("\nAverage Results")
    print("-" * 40)
    print(f"Bubble Sort : {round(bubble_average):>15,} ns")
    print(f"Heap Sort   : {round(heap_average):>15,} ns")
    print(f"Winner      : {winner}")
    print("-" * 40)


# -------------------------------------------------
# Save Results
# -------------------------------------------------

save_results(results)

print("\nResults successfully saved.")
print("Location: results/experiment_results.csv")


# -------------------------------------------------
# Generate Graph
# -------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    DATASET_SIZES,
    bubble_graph,
    marker="o",
    linewidth=2.5,
    markersize=7,
    label="Bubble Sort",
)

plt.plot(
    DATASET_SIZES,
    heap_graph,
    marker="s",
    linewidth=2.5,
    markersize=7,
    label="Heap Sort",
)

plt.title(
    "Performance Comparison of Bubble Sort and Heap Sort",
    fontsize=14,
    fontweight="bold",
)

plt.xlabel("Dataset Size", fontsize=12)

plt.ylabel("Average Runtime (Nanoseconds)", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.7)

plt.legend()

plt.tight_layout()

plt.savefig("results/graph.png", dpi=300)

plt.show()


# -------------------------------------------------
# Finish
# -------------------------------------------------

print("\n")
print("=" * 60)
print("EXPERIMENT COMPLETED SUCCESSFULLY")
print("=" * 60)
print("Datasets saved to : results/datasets/")
print("CSV results saved : results/experiment_results.csv")
print("Graph saved       : results/graph.png")
print("=" * 60)
