from revisions.trees.node import Node
from collections import deque


def tree_from_list(l: list[int | None]) -> Node | None:

    dq = deque(l)

    value = dq.popleft()
    if not value:
        return None
    root = Node(value)
    node = root

    while dq:

        value = dq.popleft()
        if not value:
            pass

    return root
