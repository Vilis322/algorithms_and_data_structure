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


class SinglyLinkedList:
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

        if not self.head:
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
        if not self.head:
            raise ValueError("The singly linked list is empty.")

        new_node = Node(value)
        current = self.head
        while current:
            if current.value == target_value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError("There is no node with the entered value for place. Please check the value and try again.")

    def delete(self, value: Any) -> None:
        """Deletes the first occurrence of the specified value from the singly linked list.

        Args:
            value (Any): The value to be deleted.

        Raises:
            ValueError: If the value is not found in the singly linked list."""
        if not self.head:
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

    def remove_duplicates(self) -> None:
        """Removes duplicates from sorted linked list."""
        if not self.head:
            print("The singly linked list is already empty.")
            return

        current = self.head
        while current.next:
            if current.value == current.next.value:
                current.next = current.next.next
            else:
                current = current.next
        return

    def sort(self) -> None:
        """Sort the linked list in ascending order from the lowest to the biggest."""
        pass

    def display(self) -> str:
        """Returns the string representation of the elements in the singly linked list in order."""
        current = self.head
        result = ""
        while current:
            result += f"{current.value}->"
            current = current.next
        result += "None"
        return result


class HashData:
    """Represents a hash table."""
    def __init__(self, size=10):
        """Initialize the hash table with given size. Defaults size is `10`."""
        self.size: int = size
        self.table: list[int | 'SinglyLinkedList' | None] = [None] * self.size

    def hash_function(self, key: int) -> int:
        """Computes the hash.

        Args:
            key (int): The key to be hashed.

        Returns:
            int: The hash value.
        """
        return key % self.size

    def put(self, key: int):
        """Inserts a key into the hash table.

        This method resolves collisions using chaining, where each index in the hash table
        holds a linked list of keys that hash to the same index.

        Args:
            key (int): The key to be inserted into the hash table.
        """
        index = self.hash_function(key)

        if self.table[index] is None:
            self.table[index] = SinglyLinkedList()

        self.table[index].append(key)

    def display(self):
        """Displays the current state of the hash table with indices and their values."""
        for hash_value, key in enumerate(self.table):
            if key is None:
                print(f"{hash_value}: {key}")
            else:
                print(f"{hash_value}: {key.display()}")


if __name__ == "__main__":
    hash1 = HashData()

    # keys
    keys = [int(x) for x in input().split(', ')]

    # apply hash function to each key
    for key in keys:
        hash1.put(key)

    hash1.display()
