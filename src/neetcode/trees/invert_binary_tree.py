from typing import Optional
from neetcode.trees.tree_node import TreeNode


class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        if root.left and root.right:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        elif root.left:
            root.right = self.invertTree(root.left)
            root.left = None
        elif root.right:
            root.left = self.invertTree(root.right)
            root.right = None
        return root
