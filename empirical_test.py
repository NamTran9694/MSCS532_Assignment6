"""
empirical_test.py

Assignment 6 - Empirical Performance Testing

This module benchmarks the deterministic and randomized selection
algorithms on different input sizes and input distributions.

Input types tested:
1. Random
2. Sorted
3. Reverse-sorted

Author: Your Name
Course: MSCS-532 Algorithms and Data Structures
"""

import random
import time
from part1_selection import deterministic_select, randomized_select


def generate_data(n, mode="random"):
    """
    Generate a list of integers according to the requested input pattern.

    Args:
        n (int): Number of elements.
        mode (str): Input type ('random', 'sorted', or 'reverse').

    Returns:
        list[int]: Generated dataset.

    Raises:
        ValueError: If mode is invalid.
    """
    if mode == "random":
        return [random.randint(1, 100000) for _ in range(n)]
    elif mode == "sorted":
        return list(range(n))
    elif mode == "reverse":
        return list(range(n, 0, -1))
    else:
        raise ValueError("Unknown mode")


def benchmark(func, arr, k, trials=5):
    """
    Measure the average execution time of a selection algorithm.

    Args:
        func (callable): Selection algorithm to test.
        arr (list[int]): Input list.
        k (int): Order statistic to find.
        trials (int): Number of repeated runs.

    Returns:
        float: Average running time in seconds.
    """
    total = 0

    for _ in range(trials):
        data = arr[:]  # copy list so each trial uses the same input
        start = time.perf_counter()
        func(data, k)
        end = time.perf_counter()
        total += (end - start)

    return total / trials


def main():
    """
    Run performance tests and print formatted results.
    """
    sizes = [100, 500, 1000, 5000]
    modes = ["random", "sorted", "reverse"]

    for mode in modes:
        print(f"\nInput Type: {mode}")

        for n in sizes:
            arr = generate_data(n, mode)
            k = n // 2

            det_time = benchmark(deterministic_select, arr, k)
            rand_time = benchmark(randomized_select, arr, k)

            print(
                f"n={n:<5} Deterministic={det_time:.6f}s  "
                f"Randomized={rand_time:.6f}s"
            )


if __name__ == "__main__":
    main()