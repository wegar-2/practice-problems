from collections import deque, defaultdict

from typing import Optional

from graph.aliases import Edge
from graph.vertex import Vertex
from graph.ungraph import Ungraph


def bfs(graph: Ungraph, start: Vertex) -> Optional[list[Vertex]]:
    """
    Implementation of generic breadth-first search algo.
    Return list of all the vertices that have been visited in the search.
    """

    queue: deque[Vertex] = deque([start])
    out: list[Vertex] = []
    visited: set[Vertex] = set()

    while queue:
        v: Vertex = queue.popleft()
        visited.add(v)
        out.append(v)
        for av in graph.adj_map[v]:
            if av not in visited:
                queue.append(av)

    return out


if __name__ == "__main__":
    from revisions.graph_algos.utils import make_default_graph

    graph = make_default_graph()
    graph.print()
    res = bfs(graph, graph.vertices[0])
    print(f"{res=}")
