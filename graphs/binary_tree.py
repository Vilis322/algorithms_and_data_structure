from re import match
from typing import Any, Optional


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self, message: str = None):
        print(
            (f"{message}: " if message else "") +
            f"{self.stack}"
        )


class BinaryNode:
    """Represents a node in the binary tree."""
    def __init__(self, BinaryNode_id: int, data: Any, parent: 'BinaryNode' = None):
        """Initializes a new node in the binary tree.

        This method initializes the binary node with the given data, sets its unique ID,
        and establishes a parent-child relationship. By default, both left and right children
        are set to 'None'.

        Args:
            BinaryNode_id (int): The unique ID for the node.
            data (Any): The data stored in the node.
            parent (BinaryNode, optional): The parent node of current the node, or 'None' if this is the root.
        """
        self.id: int = BinaryNode_id
        self.data: Any = data
        self.parent: 'BinaryNode' = parent
        self.left: Optional['BinaryNode'] = None
        self.right: Optional['BinaryNode'] = None

    def __repr__(self) -> str:
        """Returns a string representation of the binary node.

        Returns:
            str: A string representation of the binary node.
        """
        return f"bN{self.id}, data: {self.data}, left: {self.left}, right: {self.right}"


class BinaryTree:
    """Represents a binary tree."""
    def __init__(self, root_data: Any):
        """Initializes a binary tree with the root of the tree.

        This method creates the root of the binary tree with the given data and assigns it a unique ID of '0'.
        Sets 'self.map' dictionary. The dictionary maps each node's ID to the node itself (not just the data),
        allowing quick access to any node in the tree.

        Args:
            root_data (Any): The provided data stored in the root node.
        """
        self.root: 'BinaryNode' = BinaryNode(BinaryNode_id=0, data=root_data)
        self.map: dict = {0: self.root}
