class Node:
    """"""
    def __init__(self, value):
        """"""
        self.value = value
        self.next = None


class LinkedList:
    """"""
    def __init__(self):
        """"""
        self.head = None

    def insert_at_head(self, value):
        """"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        return

    def insert_at_tail(self, value):
        """"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return

    def insert_by_position(self, value, position):
        """"""
        new_node = Node(value)
        current = self.head

        while current.next:
            if current.next.value == position:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("There is have no node with entered value for place. Please check the value and try again.")

    def delete(self, value):
        """"""
        if self.head is None:
            print("The linked list is already empty. There is nothing to delete.")
            return

        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next
            print("The linked list does not have the specified element. Please check and try again.")

    def display(self):
        """"""
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
    linked_list.insert_at_tail(5)
    linked_list.insert_at_head(4)
    linked_list.insert_at_head(3)
    linked_list.insert_at_head(1)
    linked_list.display()
    linked_list.insert_at_tail(7)
    linked_list.insert_at_tail(7)
    linked_list.display()
    linked_list.delete(7)
    linked_list.display()
    linked_list.insert_by_position(7, 6)
    linked_list.display()
