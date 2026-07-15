from revisions.trees.node import Node
from typing import overload


@overload
def make_tree(values: list[int]) -> Node: ...


@overload
def make_tree(values: None = None) -> Node: ...


def make_tree(values: list[int] | None = None) -> Node:
    if values is None:
        root = Node(1)
        for x in [4, 3, 2, 5]:
            root.insert(x)
        return root
    else:
        if len(values):
            raise ValueError("Empty list!")
        else:
            root = Node(values[0])
            for x in values[1:]:
                root.insert(x)
            return root
