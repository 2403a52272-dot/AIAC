class Stack:
    """Simple LIFO stack.

    Implements push, pop, peek and is_empty operations.

    Methods follow Python list semantics: pop() raises IndexError if the stack is empty.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []  # Using list for compact, efficient append/pop at the end.

    def push(self, item):
        """Push an item onto the top of the stack.

        Args:
            item: Any Python object to be stored on the stack.
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Returns:
            The top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._items:
            # Explicit check gives a clearer error message than letting list.pop() raise.
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it.

        Returns:
            The top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]  # Last element is the top of stack.

    def is_empty(self):
        """Return True if the stack has no items, else False."""
        return len(self._items) == 0

    def __len__(self):
        """Return number of items in the stack."""
        return len(self._items)


if __name__ == "__main__":
    # Basic tests / usage demonstration
    s = Stack()
    print("Initially empty:", s.is_empty())

    # Push sample data
    for v in [10, 20, 30]:
        s.push(v)
        print(f"Pushed {v}, top now:", s.peek())

    print("Stack size:", len(s))

    # Pop all items
    while not s.is_empty():
        print("Popped:", s.pop())

    print("Empty after pops:", s.is_empty())

    # Demonstrate error on invalid operations
    try:
        s.pop()
    except IndexError as e:
        print("Expected error on pop from empty:", e)

    try:
        s.peek()
    except IndexError as e:
        print("Expected error on peek from empty:", e)