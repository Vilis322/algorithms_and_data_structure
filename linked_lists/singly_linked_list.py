from typing import Any


class Node:
    """Represents an item in a singly linked list."""
    def __init__(self, value: Any):
        """Initializes a new node with the given value.

        Args:
            value (Any): The value to be added to the singly linked list.

        Note:
            - 'self.next' (Any): The next node of the singly linked list, default is None.
        """
        self.value: Any = value
        self.next: Any = None

    def __repr__(self):
        return f"Node(data={self.value}, next={self.next.value if self.next else None})"


class LinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def insert_at_head(self, value: Any) -> None:
        """Inserts a new head node at the beginning of the singly linked list.

        Args:
            value (Any): The value to be inserted."""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    def append(self, value: Any) -> None:
        """Inserts a new node at the end of the singly linked list.

        Args:
            value (Any): The value to be inserted."""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return

    def insert_by_position(self, value: Any, target_value: Any) -> None:
        """Inserts a new node after the first occurrence of a specified target value.

        Args:
            value (Any): The value to be inserted.
            target_value (Any): The value after which the new node must be inserted.

        Raises:
            ValueError: If the target value is not found in the singly linked list or if linked list is empty"""
        if self.head is None:
            raise ValueError("The singly linked list is empty.")

        new_node = Node(value)
        current = self.head
        while current:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError("There is have no node with entered value for place. Please check the value and try again.")

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of the specified value from the singly linked list.

        Args:
            value (Any): The value to be deleted.

        Raises:
            ValueError: If the value is not found in the singly linked list."""
        if self.head is None:
            print("The singly linked list is already empty. There is nothing to delete.")
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError("The singly linked list does not have the specified element. Please check and try again.")

    def display(self) -> None:
        """Prints the elements of the singly linked list in order."""
        if not self.head:
            print("The singly linked list is empty.")
            return

        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        output = "->".join(values)
        print(output)
        return


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.display()
    linked_list.delete(1)
    linked_list.append(5)
    linked_list.display()
    linked_list.insert_at_head(4)
    linked_list.display()
    linked_list.insert_at_head(3)
    linked_list.display()
    linked_list.insert_at_head(1)
    linked_list.display()
    linked_list.append(7)
    linked_list.display()
    linked_list.append(7)
    linked_list.display()
    linked_list.delete(7)
    linked_list.display()
    linked_list.insert_by_position(8, 7)
    linked_list.display()
    linked_list.insert_by_position(2, 1)
    linked_list.display()
    linked_list.insert_by_position(6, 5)
    linked_list.display()
    linked_list.insert_by_position(9, 8)
    linked_list.display()
