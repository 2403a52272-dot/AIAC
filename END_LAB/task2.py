from collections import deque
import unittest


class Stack:
    def __init__(self, limit=10):
        self.s=[]; self.ops=deque(maxlen=limit)
    def push(self,x): self.s.append(x); self.ops.append(f"PUSH:{x!r}")
    def pop(self):
        if not self.s: self.ops.append('POP:<EMPTY>'); raise IndexError
        v=self.s.pop(); self.ops.append(f"POP:{v!r}"); return v
    def peek(self):
        if not self.s: raise IndexError
        return self.s[-1]
    def operations(self): return list(self.ops)


class TestStack(unittest.TestCase):
    def test_basic(self):
        s=Stack(); s.push('A'); s.push('B')
        self.assertEqual(s.pop(),'B'); self.assertEqual(s.peek(),'A')

    def test_empty_pop_records(self):
        s=Stack();
        with self.assertRaises(IndexError): s.pop()
        self.assertIn('POP:<EMPTY>', s.operations())

    def test_limit(self):
        s=Stack(limit=5)
        for i in range(7): s.push(f'e{i}')
        ops=[o for o in s.operations() if o.startswith('PUSH:')]
        self.assertEqual(len(ops),5); self.assertIn('e2', ops[0])


if __name__=='__main__':
    unittest.main(verbosity=2)