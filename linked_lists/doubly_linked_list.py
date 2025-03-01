from typing import Any


class DoublyNode:
    """Represents an item in a doubly linked list."""
    def __init__(self, value: Any):
        """Initializes a new node with the given value.

        Args:
            value (Any): The value to be added to the doubly linked list.

        Note:
            - 'self.next' (Any): The next node of the doubly linked list, default is None.
            - 'self.prev' (Any): The previous node of the doubly linked list, default is None.
        """
        self.value: Any = value
        self.next: Any = None
        self.prev: Any = None

    def __repr__(self):
        return (f"Node(data={self.value}, next={self.next.value if self.next else None}, "
                f"prev={self.prev.value if self.prev else None})")


class DoublyLinkedList:
    """Represents a doubly linked list."""
    def __init__(self):
        """Initializes an empty doubly linked list."""
        self.head = None
        self.tail = None

    def insert_at_head(self, value: Any) -> None:
        """Inserts a new head node at the beginning of the doubly linked list.

        Args:
            value (Any): The value to be inserted."""
        new_node = DoublyNode(value)

        if not self.head:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return

    def append(self, value: Any) -> None:
        """Inserts a new node at the end of the doubly linked list.

        Args:
            value (Any): The value to be inserted."""
        new_node = DoublyNode(value)

        if not self.head:
            self.head = self.tail = new_node
            return

        if self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            return

    def insert_by_position(self, value: Any, target_value: Any) -> None:
        """Inserts a new node after the first occurrence of a specified target value.

        Args:
            value (Any): The value to be inserted.
            target_value (Any): The value after which the new node must be inserted.

        Raises:
            ValueError: If the target value is not found in the doubly linked list or if linked list is empty"""
        if not self.head:
            raise ValueError("The doubly linked list is empty.")

        new_node = DoublyNode(value)

        if self.tail.value == target_value:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            return

        current = self.head
        while current.next:
            if current.value == target_value:
                new_node.next = current.next
                new_node.prev = current
                current.next.prev = new_node
                current.next = new_node
                return
            current = current.next
        raise ValueError("There is no node with the entered value for place. Please check the value and try again.")

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of the specified value from the doubly linked list.

        Args:
            value (Any): The value to be deleted.

        Raises:
            ValueError: If the value is not found in the doubly linked list."""
        if not self.head:
            print("The doubly linked list is already empty. There is nothing to delete.")
            return

        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        if self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                if current.next:
                    current.next.prev = current.prev
                    return
            current = current.next
        raise ValueError("The doubly linked list does not have the specified element. Please check and try again.")

    def display(self, from_head=False, from_tail=False) -> None:
        """Prints the elements of the doubly linked list in order from head to tail and from tail to head.

        Args:
            from_head (bool): If True, prints the elements from head to tail, default is False.
            from_tail (bool): If True, prints the elements from tail to head, default is False.
        """
        if not self.head:
            print("The doubly linked list is empty.")
            return

        if self.head is self.tail:
            print(f"HEAD {self.head.value} TAIL")
            return

        if from_head == from_tail:
            from_head, from_tail = True, False

        values = []

        if from_head:
            current = self.head
            values.append(str(f"HEAD {current.value}"))
            current = current.next
            while current.next:
                values.append(str(current.value))
                current = current.next
            values.append(str(f"{current.value} TAIL"))

        if from_tail:
            current = self.tail
            values.append(str(f"TAIL {current.value}"))
            current = current.prev
            while current.prev:
                values.append(str(current.value))
                current = current.prev
            values.append(str(f"{current.value} HEAD"))

        output = "<->".join(values)
        print(output)
        return


if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.display()
    linked_list.insert_at_head(1)
    linked_list.display()
    linked_list.insert_at_head(0)
    linked_list.insert_by_position(2, 1)
    linked_list.display()
    linked_list.delete(2)
    linked_list.append(2)
    linked_list.display()
    linked_list.display(from_tail=True)
