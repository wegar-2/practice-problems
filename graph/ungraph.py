from graph.vertex import Vertex
from graph.aliases import Edge

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
        self._vertices: list[Vertex] = []
        self._adj_map: dict[Vertex, list[Vertex]] = {}
        for v in vertices:
            self.add_vertex(v)
        for e in edges:
            self.add_edge(e)

    @staticmethod
    def _validate_edge(e: Edge) -> None:
        if e[0] == e[1]:
            raise ValueError(f"Received invalid edge: identical vertices {e[0]}")

    @property
    def vertices(self) -> list[Vertex]:
        return self._vertices

    @property
    def adj_map(self) -> dict[Vertex, list[Vertex]]:
        return self._adj_map

    def add_vertex(self, v: Vertex) -> None:
        if v not in self._vertices:
            self._vertices.append(v)
            self._adj_map[v] = []

    def print_adj_map(self) -> None:
        for v, lov in self._adj_map.items():
            print(f"{v} ====> {self._adj_map[v]}")

    def add_edge(self, e: Edge):
        self._validate_edge(e)

        self.add_vertex(e[0])
        self.add_vertex(e[1])

        if e[0] not in self._adj_map[e[1]]:
            self._adj_map[e[1]].append(e[0])
        if e[1] not in self._adj_map[e[0]]:
            self._adj_map[e[0]].append(e[1])

    def drop_edge(self, e: Edge) -> None:
        """
        Should be enough to check for presence of just one vertex - at this point
        it can be assumed that the graph is well-formed
        """
        if e[0] in self._adj_map[e[1]]:
            try:
                pos = self._adj_map[e[0]].index(e[1])
            except ValueError:
                pass
            else:
                self._adj_map[e[0]].pop(pos)
                self._adj_map[e[1]].pop(self._adj_map[e[1]].index(e[0]))

    def drop_vertex(self, v: Vertex) -> None:
        if v in self._vertices:
            self._vertices.pop(self._vertices.index(v))
        del self._adj_map[v]
        for v in self._adj_map:
            try:
                pos = self._adj_map[v].index(v)
            except ValueError:
                pass
            else:
                self._adj_map[v].pop(pos)

    def print(self) -> None:
        print(f"VERTICES: {self._vertices}")
        print("EDGES: ")
        self.print_adj_map()
