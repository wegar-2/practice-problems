from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def _is_subtree(
            self,
            node: Optional[TreeNode],
            subRoot: Optional[TreeNode]
    ) -> bool:
        if node is not None and subRoot is None:
            return False
        elif node is None and subRoot is not None:
            return False
        elif node is None and subRoot is None:
            return True

        if node.val == subRoot.val:
            return (
                    self._is_subtree(node.left, subRoot.left) and
                    self._is_subtree(node.right, subRoot.right)
            )
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode],
                  subRoot: Optional[TreeNode]) -> bool:

        if self._is_subtree(root, subRoot):
            return True

        if root.left is not None:
            left_check = self.isSubtree(root.left, subRoot)
        else:
            left_check = False

        if root.right is not None:
            right_check = self.isSubtree(root.right, subRoot)
        else:
            right_check = False

        return left_check or right_check
