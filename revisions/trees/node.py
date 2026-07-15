from __future__ import annotations
from typing import Optional

__all__ = ["Node"]


class Node:

    def __init__(
            self,
            value: int,
            left: Optional[Node] = None,
            right: Optional[Node] = None
    ):
        self.value = value
        self.left: Optional[Node] = left
        self.right: Optional[Node] = right

    def insert(self, value: int) -> None:
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
