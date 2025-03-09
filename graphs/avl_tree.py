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


class AVLNode:
    """Represents a node in the AVL tree."""
    def __init__(self, AVLNode_id: int, data: Any, parent: 'AVLNode' = None):
        """Creates a new node in the AVL tree.

        This method initializes a new node in the AVL tree with the given data, sets its unique ID.
        Sets the parent reference if provided. By default, both left and right children
        are set to 'None'.
        Additionally, the node's level in the AVL tree is determined:
        - The root node has a level of 0.
        - Any other node's level is one more than its parent's level.

        Args:
            AVLNode_id (int): The unique ID of the node.
            data (Any): The provided data stored in the node.
            parent (AVLNode): The parent node of this node, or 'None' if the node is the root of the AVL tree.
        """
        self.id = AVLNode_id
        self.data = data
        self.parent = parent
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None

        #  Calculation level
        #  self.level = parent + 1 if parent else 0
        if parent:
            self.level = parent.level + 1
        else:
            self.level = 0

    def is_leaf(self) -> bool:
        """Checks is the node is leaf.

        A node is considered a leaf if it has no children (neither left nor right).

        Returns:
            bool: True if the node is a leaf, False otherwise.
        """
        return not (self.left or self.right)

    @property
    def height(self) -> int:
        """Calculates the height of the node.

        The height of a leaf node is 0. For non-leaf nodes, the height is the maximum of the heights
        of the left and right children, plus 1.

        Returns:
            int: The height of the node.
        """
        if self.is_leaf():
            return 0

        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0

        return max(left_height, right_height) + 1

    def __repr__(self) -> str:
        """String representation of the AVL node."""
        return f"AVLNode id={self.id}, data={self.data}, height={self.height}"

    @property
    def balancing_factor(self) -> int:
        """Calculates the balancing factor of the node.

        The balance factor is the difference between the height of the left and right subtrees.

        Returns:
            int: The balancing factor itself.
        """
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height


class AVLTree:
    """Represents an AVL tree in a binary search tree."""
    def __init__(self, root_data: Any):
        """Initializes the AVL tree with the given root of the tree.

        This method creates the root of the AVL tree with the given data and assigns it a unique ID of '0'.
        Sets 'self.map' dictionary. The dictionary maps each node's ID to the node itself (not just the data),
        allowing quick access to any node in the tree.

        Args:
            root_data (Any): The provided data is stored in the root.
        """
        self.root = AVLNode(AVLNode_id=0, data=root_data)
        self.map = {0: self.root}

    def add_child(self, child_data: Any, to_node: AVLNode | int) -> AVLNode:
        """Adds a child node to a parent node in the AVL tree.

        This method creates a new node with the given data and attaches it to the specified parent node.
        The parent node is determined by either its unique ID or by providing the parent node object directly.
        The child node is added to the left child if it is available, otherwise to the right child.
        If both left and right children are already occupied, a custom error is raised.

        Args:
            child_data (Any): The provided data that is stored in the node.
            to_node (AVLNode | int): The parent node to attach the new child node to.

        Returns:
            AVLNode: The newly created child node.

        Raises:
            MaxChildrenError: If the parent node already has two children (left and right).
        """
        if isinstance(to_node, AVLNode):
            node_id = to_node.id
        else:
            node_id = to_node

        parent = self.map[node_id]
        last_id = len(self.map)
        new_node = AVLNode(AVLNode_id=last_id, data=child_data, parent=parent)
        if not parent.left:
            parent.left = new_node
        elif not parent.right:
            parent.right = new_node
        else:
            raise MaxChildrenError("In BinaryTree one can't be added more than 2 Nodes to parent.")
        self.map[last_id] = new_node
        return new_node

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
            current: AVLNode = stack.pop()
            if current.left:
                stack.push(current.left)
            if current.right:
                stack.push(current.right)
            yield current

    def display(self) -> None:
        """Displays each node with indentation based on its level in the AVL tree."""
        for node in self:
            print("  " * node.level + str(node))

    def root_imbalance(self) -> str:
        """Determines the imbalance type of the tree's root node.

        This method evaluates the balance factor of the root node to determine if the tree
        is imbalanced. Based on the balance factors of the root node and its children,
        the method classifies the imbalance as one of the following types:

        - 'LL' (Left-Left): Imbalance caused by the left subtree being higher, and its left child being too high.
        - 'RR' (Right-Right): Imbalance caused by the right subtree being higher, and its right child being too high.
        - 'LR' (Left-Right): Imbalance caused by the left subtree being higher, and its right child being too high.
        - 'RL' (Right-Left): Imbalance caused by the right subtree being higher, and its left child being too high.

        If the tree is balanced, the method will return 'Balanced'.

        Returns:
        str: A string describing the imbalance type ('LL', 'RR', 'LR', 'RL', or 'Balanced').
        """
        balance = self.root.balancing_factor

        if balance > 1:
            if self.root.left.balancing_factor >= 0:
                return "LL"
            else:
                return "LR"

        elif balance < -1:
            if self.root.right.balancing_factor <= 0:
                return "RR"
            else:
                return "RL"

        return "Balanced"


if __name__ == "__main__":
    from re import match

    tree = AVLTree(1)
    line_num = int(input())

    for _ in range(line_num):
        line = input()
        res = match(
            r'(?P<parent_id>\d+): (?P<left>\d+)? ?(?P<right>\d+)?\s*', line)

        if res['left']:
            tree.add_child(int(res['left']), int(res['parent_id']))
        if res['right']:
            tree.add_child(int(res['right']), int(res['parent_id']))

    print(tree.root_imbalance())
