"""
part2_data_structures.py
Assignment 6 - Part 2: Elementary Data Structures

This module implements several basic data structures from scratch:

1. ArrayStructure
2. MatrixStructure
3. Stack
4. Queue
5. SinglyLinkedList
"""
# ==============================================================================
# Data Structures Implementation
# ==============================================================================
from ast import Return


class ArrayStructure:
    """
    Simple wrapper around a Python list to demonstrate array behavior.

    Supports insertion, deletion, and indexed access.
    """

    def __init__(self):
        """Initialize an empty array."""
        self.data = []

    def insert(self, index, value):
        """
        Insert a value at a specified index.

        Args:
            index (int): Position where the value should be inserted.
            value (int): Value to insert.
        """
        self.data.insert(index, value)

    def delete(self, index):
        """
        Delete and return the value at the given index.

        Args: index (int): Index of the element to remove.

        Returns: int: Removed value.

        Raises: IndexError: If index is invalid.
        """
        if 0 <= index < len(self.data):
            return self.data.pop(index)
        raise IndexError("Index out of range")

    def access(self, index):
        """
        Return the value stored at the given index.

        Args: index (int): Index of the element to access.

        Returns: int: Value at the given index.

        Raises: IndexError: If index is invalid.
        """
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Index out of range")

    #Return a string representation of the array.
    def __str__(self):
        return str(self.data)


class MatrixStructure:
    """
    Represents a 2D matrix using a nested Python list.

    Supports setting and retrieving values by row and column.
    """

    def __init__(self, rows, cols, default=0):
        """
        Create a matrix with the given dimensions.

        Args:
            rows (int): Number of rows.
            cols (int): Number of columns.
            default (int, optional): Initial value for each cell.
        """
        self.matrix = []
        
        for _ in range(rows):
            # Create a single row of the correct length
            new_row = [default] * cols
            # Add it to the main matrix
            self.matrix.append(new_row)

    def set(self, row, col, value):
        """
        Set the value of a matrix cell.

        Args:
            row (int): Row index.
            col (int): Column index.
            value (int): Value to assign.
        """
        self.matrix[row][col] = value

    def get(self, row, col):
        """
        Get the value of a matrix cell.

        Args:
            row (int): Row index.
            col (int): Column index.

        Returns: int: Value stored at the specified location.
        """
        return self.matrix[row][col]
        
    #Return the matrix as a formatted string.
    def __str__(self):
        return "\n".join(str(row) for row in self.matrix)


class Stack:
    """
    Stack implementation using a Python list.

    Follows the Last-In, First-Out (LIFO) principle.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def push(self, item):
        """
        Add an item to the top of the stack.

        Args: item: Value to push onto the stack
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item.

        Returns: The last item added to the stack.

        Raises: IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """
        Return the top item without removing it.

        Returns: Top item in the stack.

        Raises: IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """
        Check whether the stack is empty.

        Returns: bool: True if empty, otherwise False.
        """
        return len(self.items) == 0

    #Return a string representation of the stack.
    def __str__(self):
        return str(self.items)


class Queue:
    """
    Queue implementation using a Python list.

    Follows the First-In, First-Out (FIFO) principle.
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args: item: Value to add.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item.

        Returns: The oldest item in the queue.

        Raises: IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def front(self):
        """
        Return the front item without removing it.

        Returns:Front item in the queue.

        Raises: IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        """
        Check whether the queue is empty.

        Returns: bool: True if empty, otherwise False.
        """
        return len(self.items) == 0

    #Return a string representation of the queue.
    def __str__(self):
        return str(self.items)


class Node:
    """
    Node used in the singly linked list.

    Attributes:
        data: Value stored in the node.
        next: Reference to the next node.
    """

    def __init__(self, data):
        """
        Create a new node.

        Args: data: Value stored in the node.
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly linked list implementation.

    Supports insertion at the end, deletion by value, and traversal.
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Args: data: Value to insert.
        """
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def delete(self, key):
        """
        Delete the first node containing the given value.

        Args: key: Value to remove.
        """
        current = self.head

        # Case 1: the head node contains the key
        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Key not found
        if current is None:
            return

        prev.next = current.next

    def traverse(self):
        """
        Traverse the linked list and return all values.

        Returns: list: A list containing all node values in order.
        """
        elements = []
        current = self.head

        while current:
            elements.append(current.data)
            current = current.next

        return elements


def main():
    """
    Demonstrate all implemented data structures.
    """
    print("Array Example:")
    arr = ArrayStructure()
    arr.insert(0, 10)
    arr.insert(1, 20)
    arr.insert(1, 15)
    print(arr)
    print("Access index 1:", arr.access(1))
    arr.delete(1)
    print("After deletion:", arr)

    print("\nMatrix Example:")
    mat = MatrixStructure(2, 2)
    mat.set(0, 0, 5)
    mat.set(1, 1, 9)
    print(mat)

    print("\nStack Example:")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack)
    print("Pop:", stack.pop())

    print("\nQueue Example:")
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue)
    print("Dequeue:", queue.dequeue())

    print("\nLinked List Example:")
    ll = SinglyLinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("Traversal:", ll.traverse())
    ll.delete(20)
    print("After delete:", ll.traverse())


if __name__ == "__main__":
    main()