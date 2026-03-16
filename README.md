# Assignment 6: Medians and Order Statistics & Elementary Data Structures

## Author
Nam Tran

## Course
MSCS-532 Algorithms and Data Structures

## Overview
This repository contains my solution for **Assignment 6**, which focuses on two important topics in computer science:

1. **Selection Algorithms**
   - Deterministic Selection using **Median of Medians**
   - Randomized Selection using **Randomized Quickselect**

2. **Elementary Data Structures**
   - Arrays
   - Matrices
   - Stacks
   - Queues
   - Singly Linked Lists

This project includes algorithm implementation, theoretical complexity analysis, empirical testing, and discussion of practical trade-offs among data structures.

---
# Project Objectives

The main objectives of this assignment are to:
* Implement and compare deterministic and randomized selection algorithms.
* Analyze the time and space complexity of both approaches.
* Perform empirical analysis on different input sizes and distributions.
* Implement elementary data structures from scratch in Python.
* Examine the performance of common operations.
* Understand practical trade-offs between different data structures.

---

## Part 1: Selection Algorithms

### Description
The first part of the project focuses on the order statistics problem, specifically finding the $k^{th}$ smallest element in an unsorted array. Two algorithms were implemented:
* Deterministic Selection using the Median of Medians method.
* Randomized Selection using Randomized Quickselect.

These algorithms solve the same problem but use different pivot selection strategies and have different theoretical guarantees.

**Implemented File:** `part1_selection.py`

### Algorithms Included

**1. Deterministic Selection**
This algorithm uses the Median of Medians strategy to choose a pivot that guarantees balanced partitioning. 
* **Worst-case time complexity:** $O(n)$

**2. Randomized Selection**
This algorithm uses a random pivot, similar to Quickselect. 
* **Expected time complexity:** $O(n)$
* **Worst-case time complexity:** $O(n^2)$

### Key Learning Points
* Deterministic selection provides stronger theoretical guarantees.
* Randomized selection is often faster in practice due to lower overhead.
* Both approaches are more efficient than fully sorting the array when only one order statistic is needed.

---

## Part 2: Elementary Data Structures

### Description
The second part of the project focuses on implementing and analyzing basic data structures used in computer science. The following structures were implemented:
* Arrays
* Matrices
* Stacks
* Queues
* Singly Linked Lists

**Implemented File:** `part2_data_structures.py`

### Data Structures Included

**1. ArrayStructure**
A simple list-based structure demonstrating:
* Insertion
* Deletion
* Indexed access

**2. MatrixStructure**
A 2D structure implemented using nested lists, supporting:
* Setting values
* Retrieving values

**3. Stack**
A Last-In, First-Out (LIFO) structure supporting:
* `push()`
* `pop()`
* `peek()`

**4. Queue**
A First-In, First-Out (FIFO) structure supporting:
* `enqueue()`
* `dequeue()`
* `front()`

**5. SinglyLinkedList**
A node-based structure supporting:
* Insertion at the end
* Deletion by value
* Traversal

### Key Learning Points
* Arrays provide fast indexed access but slower middle insertions and deletions.
* Linked lists are flexible for updates but slower for access and search.
* Stacks and queues are useful specialized structures for ordered processing.
* Data structure choice depends on the operation requirements of the application.

---

## Empirical Analysis

### Description
The project includes empirical performance testing to compare the deterministic and randomized selection algorithms.

**Implemented File:** `empirical_test.py`

### Test Cases
The algorithms were tested on:
* Random arrays
* Sorted arrays
* Reverse-sorted arrays

**Input Sizes**
Example sizes used: 100, 500, 1000, 5000.

### Goal
The purpose of this analysis is to compare:
* Practical running time.
* Algorithm stability across different input distributions.
* Alignment between theoretical complexity and observed performance.

### General Observation
* Both algorithms scale approximately linearly for typical inputs.
* Randomized selection is usually faster in practice.
* Deterministic selection is more stable in terms of guaranteed performance.

---

## Requirements

* Python 3.x
* No third-party libraries are required. Only the Python standard library is used.

---

## How to Run the Project

**Run Part 1: Selection Algorithms**
```bash
python part1_selection.py
```

**Run Part 2: Elementary Data Structures**
```bash
python part2_data_structures.py
```

**Run Empirical Testing**
```bash
python empirical_test.py
```

