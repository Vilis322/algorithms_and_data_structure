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

    def __add__(self, other: "DoublyLinkedList") -> "DoublyLinkedList":
        """Updates a linked list with concatenating of the second doubly linked lists.

        Args:
            other (DoublyLinkedList): The other doubly linked list to be added.

        Returns:
            DoublyLinkedList: The updated doubly linked list with concatenated 'other' doubly linked list.
        Raises:
            TypeError: if 'other' is not instance of DoublyLinkedList.
        """
        try:
            if not isinstance(other, DoublyLinkedList):
                raise TypeError("An entered data is not a doubly linked list. Check the value and try again.")
        except TypeError as e:
            print(str(e))
            return self

        if not other.head:
            print("The second doubly linked list is empty.")
            return self

        if not self.head:
            print("The first doubly linked list is empty.")
            return other

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = other.head
        return self

    def __iter__(self):
        """Iterate through the doubly linked list and yields its elements.

        Yields:
            Any: The elements of the doubly linked list one by one from the first to the last.
        """
        current = self.head
        while current:
            yield current
            current = current.next

    @staticmethod
    def concatenation(first_ll: "DoublyLinkedList", second_ll: "DoublyLinkedList") -> "DoublyLinkedList | None":
        """Creates a new doubly linked list with concatenated two linked lists.

        Args:
            first_ll (DoublyLinkedList): The first singly linked list to be concatenated with.
            second_ll (DoublyLinkedList): The second singly linked list to be concatenated with.

        Returns:
            DoublyLinkedList: The new linked list that is a result of concatenation of the two singly linked lists.

        Raises:
            TypeError: if 'first_ll' or/and 'second_ll' is not instance of DoublyLinkedList.
        """
        try:
            if not isinstance(first_ll, DoublyLinkedList) or not isinstance(second_ll, DoublyLinkedList):
                raise TypeError(f"The {'first' if not isinstance(first_ll, DoublyLinkedList)
                                else 'second'} argument is not a doubly linked list")
        except TypeError as e:
            print(str(e))
            if not isinstance(second_ll, DoublyLinkedList):
                return first_ll
            else:
                return second_ll

        if not first_ll.head:
            print("The first linked list is empty.")
            return second_ll

        if not second_ll.head:
            print("The second linked list is empty.")
            return first_ll

        concatenated_ll = DoublyLinkedList()
        for node in first_ll:
            concatenated_ll.append(node.value)

        last_node = concatenated_ll.tail
        last_node.next = second_ll.head
        second_ll.head.prev = last_node
        return concatenated_ll

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
    linked_list1 = DoublyLinkedList()
    linked_list2 = DoublyLinkedList()
    linked_list1.insert_at_head(5)
    linked_list1.insert_at_head(4)
    linked_list1.insert_at_head(3)
    linked_list1.insert_at_head(2)
    linked_list1.insert_at_head(1)
    linked_list2.insert_at_head(10)
    linked_list2.insert_at_head(9)
    linked_list2.insert_at_head(8)
    linked_list2.insert_at_head(7)
    linked_list2.insert_at_head(6)
    ll4 = DoublyLinkedList.concatenation(linked_list1, linked_list2)
    ll4.display()
    ll3 = linked_list1 + linked_list2
    ll3.display()
    linked_list1.display()
    lin = DoublyLinkedList.concatenation(2, linked_list2)
    lin.display()
    lin = DoublyLinkedList.concatenation(linked_list2, 2)
    lin.display()
