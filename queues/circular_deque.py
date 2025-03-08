from typing import Any


class CircularDeque:
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

        If the deque is empty, the element is inserted at index 0.
        If the deque is full, the rear element is removed, and the new element replaces it.
        Otherwise, element is inserted ar `(front - 1) % capacity`, following circular behavior.

        Args:
            value (Any): the value to be inserted at the front of the circular deque.

        Example:
            Inserting into a full deque (capacity = 5).
            ```python
            deque = CircularDeque(5)
            for i in [10, 20, 30, 40, 50]:
                deque.insert_front(i)

            deque.insert_front(60)  # Overwrites index 4 (current rear)
            # Before: [50, 40, 30, 20, 10] => front=0, rear=4, deque.is_full()=True
            # After: [50, 40, 30, 20, 60] => front=4, rear=3, deque.is_full()=True

            deque.insert_front(70)  # Overwrites index 3 (current rear)
            # Before: [50, 40, 30, 20, 60] => front=4, rear=3, deque.is_full()=True
            # After: [50, 40, 30, 70, 60] => front=3, rear=2, deque.is_full()=True
            ```
        """
        if self.is_empty():
            self.front = self.rear = 0
        elif self.is_full():
            self.rear = (self.rear - 1) % self.capacity

        self.front = (self.front - 1) % self.capacity
        self.deque[self.front] = value
        return

    def insert_rear(self, value: Any) -> None:
        """Inserts an element at the rear of the circular deque.

        If the deque is empty, the element is inserted at index 0.
        If the deque is full, the front element is removed, and the new element replaces it.
        Otherwise, the element is inserted at `(rear + 1) % capacity`, following circular behavior.

        Args:
            value (Any): the value to be inserted at the rear of the circular deque.

        Example:
            Inserting into a full deque (capacity = 5):

            ```python
            deque = CircularDeque(5)
            for i in [10, 20, 30, 40, 50]:
                deque.insert_rear(i)

            deque.insert_rear(60)  # Overwrites index 1 (current front)
            # Before: [50, 10, 20, 30, 40] => front=1, rear=0, deque.is_full()=True
            # After: [50, 60, 20, 30, 40] => front=2, rear=1, deque.is_full()=True

            deque.insert_rear(70)  # Overwrites index 2 (current front)
            # Before: [50, 60, 20, 30, 40] => front=2, rear=1, deque.is_full()=True
            # After: [50, 60, 70, 30, 40] => front=3, rear=2, deque.is_full()=True
            ```
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

    def __repr__(self) -> str:
        """Returns a string representation of the circular deque and front and rear indexes."""
        return f"Deque_list={self.deque}, front={self.front}, rear={self.rear}"


if __name__ == "__main__":
    dq = CircularDeque(5)
    for i in [10, 20, 30, 40, 50]:
        dq.insert_rear(i)
    print(dq)
    dq.display()
    dq.insert_rear(60)
    print(dq)
    dq.display()
    dq.insert_rear(70)
    print(dq)
    dq.display()

