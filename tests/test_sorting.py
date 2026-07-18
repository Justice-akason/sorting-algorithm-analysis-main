from algorithms.bubble_sort import bubble_sort
from algorithms.heap_sort import heap_sort


def test_bubble_sort():

    numbers = [5, 3, 8, 1, 4]

    expected = sorted(numbers)

    assert bubble_sort(numbers.copy()) == expected

    print("✓ Bubble Sort test passed")


def test_heap_sort():

    numbers = [5, 3, 8, 1, 4]

    expected = sorted(numbers)

    assert heap_sort(numbers.copy()) == expected

    print("✓ Heap Sort test passed")


if __name__ == "__main__":

    test_bubble_sort()
    test_heap_sort()

    print("\nAll tests passed successfully!")
