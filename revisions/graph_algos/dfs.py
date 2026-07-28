from graph.vertex import Vertex
from graph.ungraph import Ungraph


__all__ = ["dfs"]


def dfs(
        graph: Ungraph,
        v: Vertex,
        path: list[Vertex],
        visited: set[Vertex]
) -> None:
    visited.add(v)
    path.append(v)
    for av in graph.adj_map[v]:
        if av not in visited:
            dfs(graph, av, path, visited)


if __name__ == "__main__":
    from revisions.graph_algos.utils import make_default_graph

    graph = make_default_graph()
    graph.print()

    path: list[Vertex] = []
    visited: set[Vertex] = set()
    dfs(graph, graph.vertices[0], path, visited)
    print(f"{path=}")
    print(f"{visited=}")
