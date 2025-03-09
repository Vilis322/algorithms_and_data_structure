from re import match
from typing import Any, Optional


class MaxChildrenError(Exception):
    """Raised when trying to add more than two children to a binary tree node."""
    pass


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

        This method initializes the binary node with the given data, sets its unique ID.
        Sets the parent reference if provided. By default, both left and right children
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

    def add_child(self, child_data: Any, to_node_id: int = 0) -> None:
        """Adds a child node to the binary tree.

        This method creates a new child node with a unique ID and attaches it to the parent node
        identified by its unique ID. By default, the parent node is assumed to the root.
        The new node is assigned to the left child position if available,
        otherwise it is assigned to the right child position. If both child positions are occupied,
        the custom MaxChildrenError is raised.

        Args:
            child_data (Any): The given data stored in the child node.
            to_node_id (int): The unique ID for the parent node, default is '0' (root of the tree)

        Raises:
            MaxChildrenError: If the parent node already has left and right children.
        """
        parent = self.map[to_node_id]
        last_id = len(self.map)
        new_node = BinaryNode(BinaryNode_id=last_id, data=child_data, parent=parent)
        if not parent.left:
            parent.left = new_node
        elif not parent.right:
            parent.right = new_node
        else:
            raise MaxChildrenError("In BinaryTree one can't be added more than 2 Nodes to parent.")
        self.map[last_id] = new_node

    def __iter__(self):
        """Performs a Preorder Depth-First Search (DFS) traversal of the binary tree.

        This method uses a stack to recursive traverse.
        The root node is pushed onto the stack first. Then, nodes are popped one by one,
        visiting them in preorder (root -> left -> right). For each visited node,
        its right child is pushed onto the stack first, followed by the left child.
        This ensures that the left subtree is processed before the right subtree.

        Yields:
            BinaryNode: The next node in the tree, following the Preorder DFS traversal order.
        """
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current: BinaryNode = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            yield current

    def is_full(self) -> bool:
        """Checks if the binary tree full.

        A binary tree is considered full if every node has either exactly two children
        or no children at all. If at least one node has only one child, the tree is not full.

        Returns:
            bool: True if the binary tree is full, False otherwise.
        """
        for node in self:
            if node.left and not node.right:
                return False
        return True


if __name__ == "__main__":
    tree = BinaryTree(1)
    line_num = int(input())

    for _ in range(line_num):
        line = input()
        res = match(
            r'(?P<parent_id>\d+): (?P<left>\d+)? ?(?P<right>\d+)?\s*', line)

        if res['left']:
            tree.add_child(int(res['left']), int(res['parent_id']))
        if res['right']:
            tree.add_child(int(res['right']), int(res['parent_id']))

    print(tree.is_full())
