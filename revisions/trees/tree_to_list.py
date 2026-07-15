from revisions.trees.node import Node
from typing import Optional
from collections import deque
from revisions.trees.tree_util import make_tree


def tree_to_list(root: Node | None) -> list[int | None]:
    pass


if __name__ == "__main__":
    root = make_tree()
    res = tree_to_list(root)
    print(res)
