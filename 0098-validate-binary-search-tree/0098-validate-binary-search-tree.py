# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root,leftRange,rightRange):        
            if root:
                if root.val > rightRange or root.val < leftRange:
                    return 0
                else:
                    return solve(root.left,leftRange,root.val-1) and solve(root.right,root.val+1,rightRange)
                
            return 1
        return solve(root,-float("inf"),float("inf"))
            
                
        