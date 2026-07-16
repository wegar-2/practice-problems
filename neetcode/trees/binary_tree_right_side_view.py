from collections import defaultdict, deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Level-order traverse and then pick the last elements at every level
    """

    def _level_order_traverse(self, root: TreeNode) -> List[int]:

        out: defaultdict = defaultdict(list)
        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])

        while queue:
            node, level = queue.popleft()
            out[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return [v[-1] for v in out.values()]

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self._level_order_traverse(root)
