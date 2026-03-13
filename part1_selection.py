"""
part1_selection.py

Assignment 6 - Part 1: Selection Algorithms

This module implements two algorithms for finding the k-th smallest element in an unsorted list:

1. Deterministic Selection using the Median of Medians technique
2. Randomized Selection using Randomized Quickselect

Both algorithms solve the order statistics problem, but they differ in pivot selection strategy and theoretical guarantees.
"""

import random


def insertion_sort(arr):
    """
    Return a sorted copy of the input list using insertion sort.

    Insertion sort is used here because it is simple and efficient for very small lists, such as the groups of five used in the Median of Medians algorithm.

    Args: arr (list[int]): Input list of integers.

    Returns: list[int]: A new sorted list.
    """
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        # Shift larger elements one position to the right
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
    return a


def partition(arr, pivot):
    """
    Partition the input list into three groups relative to the pivot.

    This three-way partitioning is useful because it handles duplicate values correctly.

    Args:
        arr (list[int]): Input list of integers.
        pivot (int): Pivot value used for partitioning.

    Returns:
        tuple: Three lists in the form:
            - lows: elements smaller than pivot
            - pivots: elements equal to pivot
            - highs: elements greater than pivot
    """
    lows = [x for x in arr if x < pivot]
    pivots = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]
    return lows, pivots, highs

# ==============================================================================
# Deterministic Selection Algorithm
# ==============================================================================
def deterministic_select(arr, k):
    """
    Find the k-th smallest element using the Median of Medians algorithm.

    This algorithm guarantees worst-case O(n) time by choosing a pivot carefully through recursive median selection.

    Args:
        arr (list[int]): Input list of integers.
        k (int): Position of the desired element using 1-based indexing.

    Returns: int: The k-th smallest element.

    Raises: ValueError: If k is outside the valid range.
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k is out of bounds")

    # Base case: directly sort small arrays
    if len(arr) <= 5:
        return insertion_sort(arr)[k - 1]

    # Divide array into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Find the median of each group
    medians = [insertion_sort(group)[len(group) // 2] for group in groups]

    # Recursively find the median of medians
    pivot = deterministic_select(medians, (len(medians) + 1) // 2)

    # Partition around the pivot
    lows, pivots, highs = partition(arr, pivot)

    # Decide which partition contains the k-th smallest element
    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# ==============================================================================
# Randomized Selection Algorithm
# ==============================================================================

def randomized_select(arr, k):
    """
    Find the k-th smallest element using Randomized Quickselect.

    This algorithm chooses a random pivot and recursively searches only the relevant partition. Its expected running time is O(n), although
    the worst case is O(n^2).

    Args:
        arr (list[int]): Input list of integers.
        k (int): Position of the desired element using 1-based indexing.

    Returns:int: The k-th smallest element.

    Raises: ValueError: If k is outside the valid range.
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k is out of bounds")

    # Base case: only one element remains
    if len(arr) == 1:
        return arr[0]

    # Choose a pivot randomly
    pivot = random.choice(arr)

    # Partition the array around the pivot
    lows, pivots, highs = partition(arr, pivot)

    # Recur only into the part that contains the answer
    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))


def main():
    """
    Demonstrate both selection algorithms on a sample input.
    """
    arr = [12, 3, 5, 7, 4, 19, 26, 3, 7]
    k = 4

    print("Input array:", arr)
    print(f"{k}th smallest element using Deterministic Select:",
          deterministic_select(arr, k))
    print(f"{k}th smallest element using Randomized Select:",
          randomized_select(arr, k))


if __name__ == "__main__":
    main()