from collections import defaultdict
import logging

from graph.vertex import Vertex
from graph.aliases import Edge

logger = logging.getLogger(__name__)

__all__ = ["Ungraph"]


class Ungraph:
    """
    Adjacency-list based implementation of undirected graphs
    """


    def __init__(
            self,
            vertices: list[Vertex],
            edges: list[Edge]
    ):
        self._vertices: list[Vertex] = vertices
        self._adj_map: defaultdict[Vertex, list[Vertex]] = defaultdict(list)
        for e in edges:
            self.add_edge(e)

    @staticmethod
    def _validate_edge(e: Edge) -> None:
        if e[0] == e[1]:
            raise ValueError(f"Received invalid edge: identical vertices {e[0]}")

    def add_vertex(self, v: Vertex) -> None:
        if v not in self._vertices:
            self._vertices.append(v)

    def add_edge(self, e: Edge):
        self._validate_edge(e)

        self.add_vertex(e[0])
        self.add_vertex(e[1])

        if e[0] not in self._adj_map[e[1]]:
            self._adj_map[e[1]].append(e[0])
        if e[1] not in self._adj_map[e[0]]:
            self._adj_map[e[0]].append(e[1])
