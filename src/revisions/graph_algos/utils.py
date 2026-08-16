from graph.vertex import Vertex
from graph.ungraph import Ungraph
from graph.aliases import Edge

__all__ = ["make_default_graph"]


def make_default_graph() -> Ungraph:

    v1 = Vertex()
    v2 = Vertex()
    v3 = Vertex()
    v4 = Vertex()
    v5 = Vertex()
    v6 = Vertex()
    v7 = Vertex()

    vertices: list[Vertex] = [v1, v2, v3, v4, v5, v6, v7]
    edges: list[Edge] = [
        (v1, v2),
        (v1, v3),
        (v3, v4),
        (v4, v6),
        (v6, v7),
        (v1, v5),
        (v5, v7)
    ]

    graph = Ungraph(vertices, edges)

    return graph


if __name__ == "__main__":
    graph = make_default_graph()
    graph.print()
