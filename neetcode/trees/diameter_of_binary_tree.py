from neetcode.trees.tree_node import TreeNode
from typing import Optional


class Solution:

    def _get_height_and_diameter(
            self,
            node: Optional[TreeNode]
    ) -> tuple[int, int]:

        if not node:
            return 0, 0

        if node.left and node.right:
            left_h, left_d = self._get_height_and_diameter(node.left)
            right_h, right_d = self._get_height_and_diameter(node.right)
            h = max(left_h, right_h) + 1
            d = max(left_h + right_h + 2, left_h + 1, right_h + 1)
        elif node.left:
            left_h, left_d = self._get_height_and_diameter(node.left)
            h = left_h + 1
            d = max(left_d, left_h + 1)
        elif node.right:
            right_h, right_d = self._get_height_and_diameter(node.right)
            h = right_h + 1
            d = max(right_d, right_h + 1)
        else:
            h = 0
            d = 0

        return h, d

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, d = self._get_height_and_diameter(root)
        return d
