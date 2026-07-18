import time

def measure_time(sort_function, dataset):

    start = time.perf_counter_ns()

    sorted_data = sort_function(dataset)

    end = time.perf_counter_ns()

    if sorted_data != sorted(dataset):
        raise ValueError(
            f"{sort_function.__name__} failed to sort correctly."
        )

    return sorted_data, end - start
