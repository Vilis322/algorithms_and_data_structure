from typing import Any


class Stack:
    """Represents a stack."""
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


class Node:
    """Represents a node in the tree."""
    def __init__(self, node_id: int, data: Any, parent: 'Node' = None):
        """Initializes a node in the tree.

        Args:
            node_id (int): The unic node ID.
            data (Any): The data of the node.
            parent (Node): The parent node of current the node, or None if this is the root.
        """
        self.id = node_id
        self.data = data
        self.parent = parent
        self.child = []

    def __repr__(self) -> str:
        """A string representation of the node that prints its unic id and its data."""
        return f"N{self.id}({self.data})"


class Tree:
    """Represents a tree of nodes."""
    def __init__(self, root_data: Any):
        """Initializes a root of tree with the given data.

        Creates the root node with provided data and assigns it a unique ID '0'.
        Initializes a dictionary 'self.map' that stores each node in the tree by its unique ID.
        The dictionary maps each node's ID to the node itself (not just the data),
        allowing quick access to any node in the tree.

        Args:
            root_data (Any): The data of the root.
        """
        self.root = Node(0, root_data)
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node_id: int = 0) -> 'Node':
        """Adds a child node to the tree under a specified parent node with the given data and assigns it a unique ID.

        Creates a new child node with the provided data, assigns it a unique ID based on the current
        length of the 'self.map', and adds it to the parent node's list of children. The parent node is
        determined by the provided 'to_node_id'. If no 'to_node_id' is provided, the root will
        be used as the parent. The new child node is then added to the 'self.map' dictionary
        with its unique ID.

        Args:
            child_data (Any): The given data of the child node.
            to_node_id (int, optional): The given ID of the parent node, default is '0' (root of the tree).

        Returns:
            Node: The new node of the tree.
        """
        parent = self.map[to_node_id]  # Get the parent node by its ID
        last_id = len(self.map)  # Generates a new unique ID for the child node
        new_node = Node(last_id, child_data, parent)  # Create the new child node with the parent reference
        parent.child.append(new_node)  # Add the new node to the parent's list of children
        self.map[last_id] = new_node  # Add the new node to the map with its unique ID
        return new_node  # Return the newly created node

    def __iter__(self):
        """Traverse through the tree using Depth-First Search (DFS).

        Initializes a stack to keep track of the nodes during traversal. The root node is pushed to the stack
        first, and then the nodes are popped one by one. For each node, all of its children are pushed onto the stack.
        This continues until all nodes have been visited.

        Yields:
            Node: The next node in the tree, following the DFS traversal order.
        """
        stack = Stack()
        stack.push(self.root)

        while not stack.is_empty():
            current: Node = stack.pop()
            for child in current.child:
                stack.push(child)
            yield current

    def degree(self, node_id: int) -> int:
        """Returns the degree of a node, which is the number of its children.

        The degree of a node is defined as the number of child nodes it has. This method retrieves the node
        using its ID and then counts the number of children associated with that node.

        Args:
            node_id (int): The ID of the node for which to calculate the degree.

        Returns:
            int: The number of children (degree) of the specified node in the tree.
        """
        node = self.map[node_id]
        return len(node.child)


if __name__ == "__main__":
    tree = Tree('A')
    B = tree.add_child('B')
    C = tree.add_child('C')
    tree.add_child('D', B.id)
    tree.add_child('E', B.id)
    tree.add_child('F', B.id)
    G = tree.add_child('G', C.id)
    H = tree.add_child('H', G.id)

    node_id = int(input())
    print(tree.degree(node_id))
