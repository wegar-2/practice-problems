from __future__ import annotations

__all__ = ["Node"]


class Node:

    def __init__(self, val: int, next: Node):
        self.val: int = val
        self.next: Node = next
