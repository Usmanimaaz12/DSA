# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
         def f(root,currSum):
            if root:
                ans=(2*currSum)+root.val
                if not root.left and not root.right:
                    return ans 
                return f(root.left,ans) + f(root.right,ans)
            return 0
         return f(root,0)