from collections import deque
from typing import Optional
from neetcode.trees.tree_node import TreeNode


class Solution:

    def _to_list(self, root: Optional[TreeNode]) -> list[int | None]:
        if root is None:
            return []

        out: list[int | None] = []
        queue: deque[TreeNode | None] = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                out.append(node)
                continue

            out.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while out[-1] is None:
            out.pop()

        return out

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self._to_list(p) == self._to_list(q)
