# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def solve(root,depth,isLeft):
            if root:
                if isLeft:
                    return max(solve(root.right,depth+1,0),solve(root.left,1,1))
                else:
                    return max(solve(root.left,depth+1,1),solve(root.right,1,0))
            return depth-1
        return solve(root,0,1)
                
        