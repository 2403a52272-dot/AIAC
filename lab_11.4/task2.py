from collections import deque
from time import perf_counter

# task2.py
# Queue implementations and a small performance review benchmark.
# First: simple list-based queue (enqueue: O(1), dequeue: O(n) because of pop(0))
# Then: efficient deque-based queue (both enqueue and dequeue O(1))



class ListQueue:
    """Simple queue using Python list.
    enqueue -> append (amortized O(1))
    dequeue -> pop(0) (O(n) because elements must be shifted)
    """
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class DequeQueue:
    """Efficient queue using collections.deque.
    enqueue -> append (O(1))
    dequeue -> popleft (O(1))
    """
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


def benchmark(n=100_000):
    """Compare list-based and deque-based queue performance for n enqueues + n dequeues."""
    print(f"Benchmarking with n={n}")

    q1 = ListQueue()
    t0 = perf_counter()
    for i in range(n):
        q1.enqueue(i)
    for _ in range(n):
        q1.dequeue()
    t1 = perf_counter()
    print(f"ListQueue elapsed: {t1 - t0:.4f} s")

    q2 = DequeQueue()
    t0 = perf_counter()
    for i in range(n):
        q2.enqueue(i)
    for _ in range(n):
        q2.dequeue()
    t1 = perf_counter()
    print(f"DequeQueue elapsed: {t1 - t0:.4f} s")


if __name__ == "__main__":
    # Quick correctness smoke test
    q = ListQueue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.is_empty()

    qd = DequeQueue()
    qd.enqueue("a")
    qd.enqueue("b")
    assert qd.dequeue() == "a"
    assert qd.dequeue() == "b"
    assert qd.is_empty()

    # Run a small benchmark (adjust n as needed)
    benchmark(50_000)