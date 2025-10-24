# File: /c:/Users/ramch/OneDrive/Desktop/AI CODE/lab_11.4/task3.py
# Singly Linked List with insert_at_end, delete_value, and traverse
# Inline comments explain pointer updates (non-trivial steps).
# Suggested test cases (covered in __main__):
# 1. Insert into empty list.
# 2. Insert multiple items and traverse.
# 3. Delete head, middle, tail.
# 4. Delete a non-existent value.
# 5. Delete when duplicates exist (only first occurrence removed).

class Node:
    """A node in a singly linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None  # pointer to the next node

    def __repr__(self):
        return f"Node({self.value})"


class LinkedList:
    """Simple singly linked list with head pointer."""
    def __init__(self):
        self.head = None  # start with an empty list

    def insert_at_end(self, value):
        """Insert a new node with `value` at the end of the list."""
        new_node = Node(value)
        if self.head is None:
            # List is empty: head should point to the new node.
            # This sets the single-node chain start.
            self.head = new_node
            return

        # Walk to the last node (node whose next is None).
        current = self.head
        while current.next is not None:
            current = current.next

        # current now refers to last node. Update its next pointer to the new node.
        # This extends the chain: previous last -> new_node -> None
        current.next = new_node

    def delete_value(self, value):
        """
        Delete the first node that contains `value`.
        Returns True if a node was deleted, False otherwise.
        """
        current = self.head
        prev = None

        # Walk the list to find the target node.
        while current is not None:
            if current.value == value:
                if prev is None:
                    # Deleting the head node:
                    # Move head forward to the next node, effectively removing
                    # the original head from the chain.
                    # Old head still exists as `current` until function ends,
                    # but nothing in the list points to it.
                    self.head = current.next
                else:
                    # Deleting a middle or tail node:
                    # prev.next currently points to current. Change prev.next to
                    # current.next to bypass `current` and link prev -> current.next.
                    # This removes `current` from the chain.
                    prev.next = current.next
                # Optionally break or return since only the first occurrence is removed.
                return True

            # Move both pointers forward: prev follows current, current advances one node.
            prev = current
            current = current.next

        # Value not found
        return False

    def traverse(self):
        """Return a list of node values by traversing from head to tail."""
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next  # advance to next node
        return values

    def __repr__(self):
        return "->".join(str(v) for v in self.traverse()) or "EmptyList"


if __name__ == "__main__":
    # Basic tests covering suggested test cases.
    ll = LinkedList()

    # 1. Insert into empty list.
    ll.insert_at_end(10)
    assert ll.traverse() == [10], "Insert into empty list failed"

    # 2. Insert multiple items and traverse.
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_end(20)  # duplicate to test delete-first-occurrence behavior
    assert ll.traverse() == [10, 20, 30, 20], "Multiple inserts failed"

    # 3. Delete head (10).
    deleted = ll.delete_value(10)
    assert deleted is True and ll.traverse() == [20, 30, 20], "Delete head failed"

    # 4. Delete middle (30).
    deleted = ll.delete_value(30)
    assert deleted is True and ll.traverse() == [20, 20], "Delete middle failed"

    # 5. Delete tail (the second 20).
    deleted = ll.delete_value(20)
    assert deleted is True and ll.traverse() == [20], "Delete first duplicate failed"

    # 6. Delete non-existent value (999).
    deleted = ll.delete_value(999)
    assert deleted is False and ll.traverse() == [20], "Deleting non-existent value should return False"

    # 7. Delete remaining head to become empty.
    deleted = ll.delete_value(20)
    assert deleted is True and ll.traverse() == [], "Delete to empty failed"

    print("All tests passed.")