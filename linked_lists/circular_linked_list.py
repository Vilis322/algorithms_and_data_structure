from typing import Any


class Node:
    """Represents an item in a circular linked list."""
    def __init__(self, value: Any):
        """Initializes a new node with the given value.

        Args:
            value (Any): The value to be added to the circular linked list.

        Note:
            - 'self.next' (Any): The next node of the circular linked list, default is None.
        """
        self.value: Any = value
        self.next: Any = None

    def __repr__(self):
        return f"Node(data={self.value}, next={self.next.value if self.next else None})"


class CircularLinkedList:
    """Represents a circular linked list."""
    def __init__(self):
        """Initializes an empty circular linked list."""
        self.head = None

    def insert_at_head(self, value: Any) -> None:
        """Inserts a new head node at the beginning of the circular linked list.

        Args:
            value (Any): The value to be inserted."""
        new_node = Node(value)

        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head
        while current.next is not self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node
        return

    def append(self, value: Any) -> None:
        """Inserts a new node at the end of the circular linked list.

        Args:
            value (Any): The value to be inserted."""
        new_node = Node(value)

        if not self.head:
            new_node.next = new_node
            self.head = new_node
            return

        current = self.head
        while current.next is not self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        return

    def insert_by_position(self, value: Any, target_value: Any) -> None:
        """Inserts a new node after the first occurrence of a specified target value.

        Args:
            value (Any): The value to be inserted.
            target_value (Any): The value after which the new node must be inserted.

        Raises:
            ValueError: If the target value is not found in the circular linked list or if linked list is empty."""
        if not self.head:
            raise ValueError("The circular linked list is empty.")

        new_node = Node(value)
        current = self.head

        while True:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

            if current is self.head:
                break
        raise ValueError("There is no node with the entered value for place. Please check the value and try again.")

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of the specified value from the circular linked list.

        Args:
            value (Any): The value to be deleted.

        Raises:
            ValueError: If the value is not found in the circular linked list."""
        if not self.head:
            print("The circular linked list is already empty. There is nothing to delete.")
            return

        if self.head.value == value:
            if self.head.next is self.head:
                self.head = None
                return

            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        current = self.head
        while current.next is not self.head:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("The circular linked list does not have the specified element. Please check and try again.")

    def display(self) -> None:
        """Prints the elements of the circular linked list in order."""
        if not self.head:
            print("The circular linked list is empty.")
            return

        current = self.head
        values = []
        while True:
            values.append(str(current.value))
            current = current.next
            if current is self.head:
                values.append(str(f"HEAD {current.value}"))
                break
        output = "->".join(values)
        print(output)
        return

    def reverse(self) -> None:
        """Reverses the circular linked list."""
        if not self.head or not self.head.next:
            return

        last = self.head
        current = self.head.next
        prev = self.head
        while current is not self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        last.next = self.head


if __name__ == "__main__":
    linked_list = CircularLinkedList()
    for i in [11, 22, 33, 44, 55, 66, 77, 88, 99]:
        linked_list.append(i)
    linked_list.display()
    linked_list.reverse()
    linked_list.display()
