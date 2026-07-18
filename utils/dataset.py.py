import random

def generate_dataset(size):
    return [random.randint(1, 100000) for _ in range(size)]

def copy_dataset(dataset):
    return dataset.copy()
