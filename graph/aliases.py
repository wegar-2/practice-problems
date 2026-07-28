from typing import TypeAlias

from graph.vertex import Vertex

__all__ = ["Edge"]


Edge: TypeAlias = tuple[Vertex, Vertex]
