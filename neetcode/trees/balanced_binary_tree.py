from typing import Optional
from neetcode.trees.tree_node import TreeNode


class Solution:

    def _is_balanced(self, node: Optional[TreeNode]) -> tuple[bool, int]:

        if not node:
            return True, 0

        if node.left and node.right:
            ibl, hl = self._is_balanced(node.left)
            ibr, hr = self._is_balanced(node.right)
            ib = ibl and ibr and (abs(hl - hr) <= 1)
            h = max(hl, hr) + 1
            return ib, h
        elif node.left:
            ibl, hl = self._is_balanced(node.left)
            h = hl + 1
            ib = ibl and abs(h) <= 1
            return ib, h
        elif node.right:
            ibr, hr = self._is_balanced(node.right)
            h = hr + 1
            ib = ibr and abs(h) <= 1
            return ib, h
        else:
            return True, 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_bal, _ = self._is_balanced(root)
        return is_bal
