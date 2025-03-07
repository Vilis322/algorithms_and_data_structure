from typing import Any


class Deque:
    def __init__(self, capacity: int):
        """Initializes an empty circular deque.

        Args:
            capacity (int): represents maximum capacity of the circular deque.

        Notes:
            'self.front' (int): index of the front element in circular deque.
            'self.rear' (int): index of the rear element in circular deque.
        """
        self.capacity = capacity
        self.deque = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_empty(self) -> bool:
        """Checks if a circular deque is empty.

        Returns:
            bool: True if the circular deque is empty, False otherwise.
        """
        return self.front == -1

    def is_full(self) -> bool:
        """Checks if a circular deque is full.

        Returns:
            bool: True if the circular deque is full, False otherwise.
        """
        return (self.rear + 1) % self.capacity == self.front

    def insert_front(self, value: Any) -> None:
        """Inserts an element at the front of the circular deque.

        Args:
            value (Any): the value to be inserted at the front of the circular deque.
        """
        if self.is_empty():
            self.front = self.rear = 0
        elif self.is_full():
            self.front = (self.front + 1) % self.capacity

        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        return

    def insert_rear(self, value: Any) -> None:
        """Inserts an element at the rear of the circular deque.

        Args:
            value (Any): the value to be inserted at the rear of the circular deque.
        """
        if self.is_empty():
            self.front = self.rear = 0
        elif self.is_full():
            self.front = (self.front + 1) % self.capacity

        self.rear = (self.rear + 1) % self.capacity
        self.deque[self.rear] = value
        return

    def delete_front(self) -> Any:
        """Deletes a front element from the circular deque.

        Returns:
            Any: the front element that was inserted first at the front of circular deque.
        """
        if self.is_empty():
            return None

        value = self.deque[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return value

    def delete_rear(self) -> Any:
        """Deletes a rear element from the circular deque.

        Returns:
            Any: the rear element that was inserted first at the rear of circular deque.
        """
        if self.is_empty():
            return None

        value = self.deque[self.rear]
        if self.front == self.rear:
            self.rear = self.front = -1
        else:
            self.rear = (self.rear - 1) % self.capacity
        return value

    def peek_front(self) -> Any:
        """Returns the front element of the circular deque without removing it.

        Returns:
            Any: the front element of the circular deque.
        """
        if self.is_empty():
            return None
        return self.deque[self.front]

    def peek_rear(self) -> Any:
        """Returns the rear element of the circular deque without removing it.

        Returns:
            Any: the rear element of the circular deque.
        """
        if self.is_empty():
            return None
        return self.deque[self.rear]

    def display(self) -> None:
        """Displays all elements in the circular deque."""
        if self.is_empty():
            return None

        index = self.front
        while index != self.rear:
            print(self.deque[index], end=" ")
            index = (index + 1) % self.capacity
        print(self.deque[self.rear])
        return


if __name__ == "__main__":
    dq = Deque(5)
    for i in [1, 2, 3, 4, 5]:
        dq.insert_rear(i)
    dq.display()
    dq.insert_rear(6)
    dq.display()
    dq.insert_front(0)
    dq.display()
    dq.insert_front(2)
    dq.display()
    dq.insert_rear(7)
    dq.display()
