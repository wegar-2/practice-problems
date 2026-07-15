from revisions.trees.node import Node
from revisions.trees.tree_util import make_tree
from revisions.trees.tree_to_list import tree_to_list
from collections import deque


def tree_from_list(l: list[int | None]) -> Node | None:

    if len(l) == 0 or l[0] is None:
        return None

    root: Node = Node(l[0])

    queue: deque = deque([root])
    i: int = 1

    while queue:

        node = queue.popleft()

        if i < len(l):
            value = l[i]
            if value is not None:
                node.left = Node(value)
                queue.append(node.left)
            i += 1

        if i < len(l):
            value = l[i]
            if value is not None:
                node.right = Node(value)
                queue.append(node.right)
            i += 1

    return root


if __name__ == "__main__":
    root = make_tree()
    l = tree_to_list(root)
    print(l)

    root = tree_from_list(l)
    l = tree_to_list(root)
    print(l)
