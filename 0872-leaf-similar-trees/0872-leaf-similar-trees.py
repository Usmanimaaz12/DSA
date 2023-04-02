# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        #apply any traversal
        l1=[]
        l2=[]
        def solve(root,l):        
            if root:
                if not root.left and not root.right:
                    l.append(root.val)
                solve(root.left,l)
                solve(root.right,l)
                return l
        
        return solve(root1,l1)==solve(root2,l2)