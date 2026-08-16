from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        lb: float = float("-inf")
        ub: float = float("inf")

        def _recurse(node: TreeNode, lb: float, ub: float, check: bool):
            if not node:
                return True and check
            else:
                if node.val <= lb or node.val >= ub:
                    return False
                else:
                    if node.left:
                        check = _recurse(node.left, lb, min(ub, node.val),
                                         True) and check
                    if node.right:
                        check = _recurse(node.right, max(lb, node.val), ub,
                                         True) and check
                    return check

        return _recurse(root, lb, ub, True)
