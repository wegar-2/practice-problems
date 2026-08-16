from collections import deque, defaultdict
from typing import Optional, List
from neetcode.trees.tree_node import TreeNode

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        out: defaultdict = defaultdict(list)

        if root is None:
            return []

        queue: deque[tuple[TreeNode, int]] = deque([(root, 0)])

        while queue:

            node, level = queue.popleft()
            out[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return [v for _, v in out.items()]
