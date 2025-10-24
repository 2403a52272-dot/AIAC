from collections import defaultdict, deque
from typing import Dict, List, Set, Optional, Any

# GitHub Copilot
# File: task5.py
# Graph representation using an adjacency list with BFS and DFS (recursive & iterative)


class Graph:
    def __init__(self):
        # adjacency list: node -> list of neighbor nodes
        self.adj: Dict[Any, List[Any]] = defaultdict(list)

    def add_edge(self, u: Any, v: Any, undirected: bool = True) -> None:
        """Add an edge u -> v. If undirected=True also add v -> u."""
        self.adj[u].append(v)
        if undirected:
            self.adj[v].append(u)

    def bfs(self, start: Optional[Any] = None) -> List[Any]:
        """
        Breadth-First Search.
        If start is None, run BFS for all components and return visiting order.
        """
        visited: Set[Any] = set()
        order: List[Any] = []
        nodes = list(self.adj.keys())

        # Helper to run BFS from a single source
        def _bfs_source(src: Any):
            q = deque([src])
            visited.add(src)
            while q:
                node = q.popleft()
                order.append(node)
                # visit neighbors in adjacency order
                for nbr in self.adj.get(node, []):
                    if nbr not in visited:
                        visited.add(nbr)
                        q.append(nbr)

        if start is not None:
            # ensure start exists in adjacency list (add isolated start if needed)
            if start not in self.adj:
                self.adj[start] = []
            _bfs_source(start)
            return order

        # No start provided: run BFS for each unvisited component
        for n in nodes:
            if n not in visited:
                _bfs_source(n)
        return order

    def dfs_recursive(self, start: Optional[Any] = None) -> List[Any]:
        """
        Depth-First Search (recursive).
        If start is None, visit all components.
        Recursive DFS is simple and natural to implement but may hit recursion limits
        on very deep graphs (use iterative version to avoid that).
        """
        visited: Set[Any] = set()
        order: List[Any] = []

        def _dfs(node: Any):
            visited.add(node)
            order.append(node)
            for nbr in self.adj.get(node, []):
                if nbr not in visited:
                    _dfs(nbr)

        if start is not None:
            if start not in self.adj:
                self.adj[start] = []
            _dfs(start)
            return order

        for n in list(self.adj.keys()):
            if n not in visited:
                _dfs(n)
        return order

    def dfs_iterative(self, start: Optional[Any] = None) -> List[Any]:
        """
        Depth-First Search (iterative using explicit stack).
        Iterative DFS avoids recursion depth limits and gives explicit control over stack order.
        Note: To mimic recursive order, neighbors are pushed in reverse.
        """
        visited: Set[Any] = set()
        order: List[Any] = []

        def _dfs_source(src: Any):
            stack = [src]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                order.append(node)
                # push neighbors in reverse to visit in the same order as recursive DFS
                neighbors = list(self.adj.get(node, []))
                for nbr in reversed(neighbors):
                    if nbr not in visited:
                        stack.append(nbr)

        if start is not None:
            if start not in self.adj:
                self.adj[start] = []
            _dfs_source(start)
            return order

        for n in list(self.adj.keys()):
            if n not in visited:
                _dfs_source(n)
        return order


if __name__ == "__main__":
    # Example usage
    g = Graph()
    # build a sample graph
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "E"),
        ("F", "G"),  # separate component
    ]
    for u, v in edges:
        g.add_edge(u, v, undirected=False)  # directed edges for demonstration

    print("Adjacency list:")
    for node, nbrs in g.adj.items():
        print(f"  {node}: {nbrs}")

    print("\nBFS from 'A':", g.bfs("A"))
    print("DFS recursive from 'A':", g.dfs_recursive("A"))
    print("DFS iterative from 'A':", g.dfs_iterative("A"))

    print("\nFull BFS (all components):", g.bfs())
    print("Full DFS recursive (all components):", g.dfs_recursive())
    print("Full DFS iterative (all components):", g.dfs_iterative())