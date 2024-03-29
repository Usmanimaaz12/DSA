# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def find_min_depth(root):
            if not root:
                return 0
            if not root.left and not root.right:
                return 1
            if not root.left and root.right:
                return 1+find_min_depth(root.right)
            if not root.right and root.left:
                return 1+find_min_depth(root.left)
            if root.left and root.right:
                return min(1+find_min_depth(root.left),1+find_min_depth(root.right))
        return find_min_depth(root)
        