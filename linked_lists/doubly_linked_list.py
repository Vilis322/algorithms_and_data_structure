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
        if not isinstance(other, DoublyLinkedList):
            print("The object is not a doubly linked list.")
            return self

        if not other.head:
            print("The second doubly linked list is empty.")
            return self

        if not self.head:
            print("The first doubly linked list is empty.")
            return other

        self.tail.next = other.head
        other.head.prev = self.tail
        self.tail = other.tail
        return self

    @staticmethod
    def concatenation(first_ll: "DoublyLinkedList", second_ll: "DoublyLinkedList") -> "DoublyLinkedList | None":
        """Creates a new doubly linked list with concatenated two linked lists.

        Args:
            first_ll (DoublyLinkedList): The first singly linked list to be concatenated with.
            second_ll (DoublyLinkedList): The second singly linked list to be concatenated with.

        Returns:
            DoublyLinkedList: The new linked list that is a result of concatenation of the two singly linked lists.
        """
        if not isinstance(first_ll, DoublyLinkedList):
            print("First argument is not a linked list.")
            return second_ll

        if not isinstance(second_ll, DoublyLinkedList):
            print("Second argument is not a linked list.")
            return first_ll

        if not first_ll.head:
            print("The first linked list is empty.")
            return second_ll

        if not second_ll.head:
            print("The second linked list is empty.")
            return first_ll

        concatenated_ll = DoublyLinkedList()

        current = first_ll.head
        while current:
            concatenated_ll.append(current.value)
            current = current.next

        current = second_ll.head
        while current:
            concatenated_ll.append(current.value)
            current = current.next

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

    def display(self, from_head=None, from_tail=None) -> None:
        """Prints the elements of the doubly linked list in order from head to tail and from tail to head.

        Args:
            from_head (bool): If True, prints the elements from head to tail, default is None.
            from_tail (bool): If True, prints the elements from tail to head, default is None.
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

    def is_palindrome(self) -> bool:
        """Checks that the doubly linked list is palindrome.

        Returns:
            bool: True if the doubly linked is palindrome, False otherwise.
        """
        if self.head is self.tail:
            return True

        right_element = self.tail
        left_element = self.head
        print(left_element, right_element)
        while left_element is not right_element and left_element.next is not right_element:
            if left_element.value == right_element.value:
                left_element = left_element.next
                right_element = right_element.prev
                print(left_element, right_element)
            else:
                return False
        return True


if __name__ == "__main__":
    linked_list1 = DoublyLinkedList()
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        linked_list1.append(i)

    linked_list2 = DoublyLinkedList()
    for i in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
        linked_list2.append(i)

    palindrome_linked_list = DoublyLinkedList.concatenation(linked_list1, linked_list2)
    palindrome_linked_list.display()
    print(palindrome_linked_list.is_palindrome())
    palindrome_linked_list.insert_by_position(11, 10)
    print(palindrome_linked_list.is_palindrome())
    print(linked_list1.is_palindrome())
    print(linked_list2.is_palindrome())
