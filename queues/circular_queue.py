from typing import Any


class CircularQueue:
    def __init__(self, capacity: int):
        """Initializes an empty circular queue.

        Args:
            capacity (int): represents maximum capacity of the circular queue.

        Notes:
            'self.front' (int): index of the first element in the circular queue.
            'self.rear' (int): index of the most recently added element in the  queue.
        """
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self) -> bool:
        """Checks if a circular queue is empty.

        Returns:
            bool: True if the circular queue is empty, False otherwise.
        """
        return self.front == -1

    def is_full(self) -> bool:
        """Checks if a circular queue is full.

        Returns:
            bool: True if the circular queue is full, False otherwise.
        """
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, value: Any) -> None:
        """Enqueues a value to the circular queue.

        Args:
            value (Any): value to be enqueued to the circular queue.
        """
        if self.is_full():
            self.front = (self.front + 1) % self.capacity
        elif self.is_empty():
            self.front = self.rear = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        return

    def dequeue(self) -> Any:
        """Dequeues an element from a circular queue.

        Returns:
            Any: the element that was enqueued first to the circular queue.
        """
        if self.is_empty():
            return None

        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return value

    def peek(self) -> Any:
        """Returns the front element of the circular queue without removing it.

        Returns:
            Any: the front element of the circular queue.
        """
        if self.is_empty():
            return None
        return self.queue[self.front]

    def display(self) -> None:
        """Displays all elements in the circular queue."""
        if self.is_empty():
            return None

        index = self.front
        while index != self.rear:
            print(self.queue[index], end=" ")
            index = (index + 1) % self.capacity
        print(self.queue[self.rear])
        return


if __name__ == "__main__":
    cq = CircularQueue(5)
    print(cq.is_full())
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    cq.display()
    cq.dequeue()
    cq.display()
    cq.enqueue(6)
    cq.display()
    cq.enqueue(7)
    cq.display()
