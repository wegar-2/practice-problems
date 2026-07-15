from revisions.trees.node import Node
from collections import deque
from revisions.trees.tree_util import make_tree


def tree_to_list(root: Node) -> list[int | None]:

    queue: deque[Node | None] = deque()
    queue.append(root)
    out: list[int | None] = []

    while queue:
        node = queue.popleft()

        if node is None:
            out.append(None)
            continue

        out.append(node.value)
        queue.append(node.left)
        queue.append(node.right)

    while out[-1] is None:
        out.pop(-1)

    return out


if __name__ == "__main__":
    root = make_tree()
    res = tree_to_list(root)
    print(res)
