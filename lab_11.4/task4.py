from typing import Optional, List

# task4.py


class Node:
    """
    Node of a Binary Search Tree.

    Attributes:
        value: The value stored in the node.
        left: Left child Node (values < value).
        right: Right child Node (values > value).
    """
    def __init__(self, value: int):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node({self.value})"


class BST:
    """
    Simple Binary Search Tree with insert, search, and inorder traversal.
    Duplicate values are ignored (not inserted).
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        """
        Insert value into the BST. If value already exists, do nothing.

        Args:
            value: Integer value to insert.
        """
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            elif value > current.value:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right
            else:
                # value == current.value -> ignore duplicates
                return

    def search(self, value: int) -> bool:
        """
        Search for value in the BST.

        Args:
            value: Integer value to search for.

        Returns:
            True if value is found, False otherwise.
        """
        current = self.root
        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self) -> List[int]:
        """
        Return the inorder traversal of the BST as a sorted list.

        Returns:
            List of integers in ascending order.
        """
        result: List[int] = []

        def _inorder(node: Optional[Node]):
            if node is None:
                return
            _inorder(node.left)
            result.append(node.value)
            _inorder(node.right)

        _inorder(self.root)
        return result


if __name__ == "__main__":
    # Test setup
    values = [7, 3, 9, 1, 5, 8, 10, 5]  # includes a duplicate 5
    tree = BST()
    for v in values:
        tree.insert(v)

    # Inorder traversal (should be sorted, duplicates ignored)
    print("Inorder traversal:", tree.inorder_traversal())

    # Search tests: present vs absent
    present = 5
    absent = 4
    print(f"Search {present}: {'Found' if tree.search(present) else 'Not found'}")
    print(f"Search {absent}: {'Found' if tree.search(absent) else 'Not found'}")