from typing import Optional
from neetcode.trees.tree_node import TreeNode


class Solution:

    def _get_depth(self, node: Optional[TreeNode]) -> int:

        if not node:
            return 0

        if node.left and node.right:
            return 1 + max(self._get_depth(node.left),
                           self._get_depth(node.right))
        elif node.left:
            return 1 + self._get_depth(node.left)
        elif node.right:
            return 1 + self._get_depth(node.right)
        else:
            return 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._get_depth(root)
