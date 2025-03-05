from typing import Any


class Stack:
    """Represents a stack with method that checks if the expression has balanced brackets."""
    def __init__(self):
        """Initializes an empty stack and a dictionary to check matching bracket pairs."""
        self.items = []
        self.bracket_pairs = {")": "(", "]": "[", "}": "{"}

    def is_empty(self) -> bool:
        """Checks if the stack is empty.

        Returns:
            bool: True if stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def push(self, item: Any) -> None:
        """Pushes an item to the stack.

        Args:
            item (Any): Item to be pushed to the stack.
        """
        return self.items.append(item)

    def pop(self) -> Any:
        """Returns an item from the stack and removes it.

        Returns:
            Any: item from the stack.

        Raises:
            IndexError: if the stack was already empty.
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty!")

    def peek(self) -> Any:
        """Returns an item from the stack without removing it.

        Returns:
            Any: item from the stack.

        Raises:
            IndexError: if the stack was already empty.
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty!")

    def size(self) -> int:
        """Returns the size of the stack.

        Returns:
            int: size of the stack.
        """
        return len(self.items)

    def clear(self) -> None:
        """Clears the stack."""
        self.items = []
        return

    def is_bracket_balanced(self, expression: str) -> bool:
        """Checks if the given expression has a balanced brackets.

        Returns:
            bool: True if expression has a balanced brackets, False otherwise.
        """
        self.clear()

        for bracket in expression:
            if bracket in self.bracket_pairs.values():
                self.push(bracket)
            elif bracket in self.bracket_pairs:
                if self.is_empty() or self.pop() != self.bracket_pairs[bracket]:
                    return False

        return self.is_empty()


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_bracket_balanced("[(abc)]{a}{[(b)(42)]*(56)}"))
    print(stack.is_bracket_balanced("[(abc])"))
    print(stack.is_bracket_balanced("[](){}{}{}{}{}{}"))
