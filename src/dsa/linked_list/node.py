from __future__ import annotations
from typing import Optional

__all__ = ["Node"]


class Node:

    def __init__(self, val: int, next: Optional[Node] = None):
        self.val: int = val
        self.next: Optional[Node] = next
