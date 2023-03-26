# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return 0
        if not root.left and not root.right:
            return target==root.val
        
        return self.hasPathSum(root.right,target-root.val) or self.hasPathSum(root.left,target-root.val)
            
             
            
            
        