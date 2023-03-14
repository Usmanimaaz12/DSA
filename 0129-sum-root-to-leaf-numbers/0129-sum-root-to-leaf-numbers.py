# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,Tsum):
            if not root:
                return 0
            Tsum=Tsum*10 + root.val
            if not root.left and not root.right:
                return Tsum
            return (dfs(root.left,Tsum)+dfs(root.right,Tsum))
        return dfs(root,0)