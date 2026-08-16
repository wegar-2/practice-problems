from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def _count_subtree_good_nodes(
            self,
            node: Optional[TreeNode],
            max_on_path: int
    ) -> int:
        if node is None:
            return 0

        out = int(max_on_path <= node.val)
        max_on_path = max(max_on_path, node.val)

        if node.left:
            out += self._count_subtree_good_nodes(node.left, max_on_path)
        if node.right:
            out += self._count_subtree_good_nodes(node.right, max_on_path)
        return out

    def goodNodes(self, root: TreeNode) -> int:
        out: int = 1  # root
        max_on_path: int = root.val

        if root.left:
            out += self._count_subtree_good_nodes(root.left, max_on_path)
        if root.right:
            out += self._count_subtree_good_nodes(root.right, max_on_path)

        return out
