from collections import deque, defaultdict

from typing import Optional

from graph.aliases import Edge
from graph.vertex import Vertex
from graph.ungraph import Ungraph


def bfs(graph: Ungraph, start: Vertex, end: Vertex) -> Optional[list[Vertex]]:
    """
    Implementation of generic breadth-first search algo.
    Return list of all the vertices that have been visited in the search for a path from
    start vertex to end vertex
    """


    queue: deque[Vertex] = deque([start])
    out: list[Vertex] = [start]
    visited: set[Vertex] = {start}

    while queue:
        next_: Vertex = queue.popleft()


    return out