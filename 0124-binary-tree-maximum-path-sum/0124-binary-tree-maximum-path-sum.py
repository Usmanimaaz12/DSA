# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root:
                l_curr,l_path=solve(root.left)
                r_curr,r_path=solve(root.right)
                rt_curr=max(root.val,root.val+l_curr, root.val+r_curr)
                rt_path=max(rt_curr,root.val+l_curr+r_curr,l_path,r_path)
                return (rt_curr, rt_path)
            return (float("-inf"), float("-inf"))
        return solve(root)[1] #the answer returned from solve will have two values , our ans will be the second value
        