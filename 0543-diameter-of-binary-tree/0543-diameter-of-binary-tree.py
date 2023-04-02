# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root:
            ld,lp=self.solve(root.left)
            rd,rp=self.solve(root.right)
#                  depth(1+max of left depth and right depth)             path(left path or right path or 1+ld+rd)
            return 1+max(ld,rd), max(lp,rp,1+ld+rd)
# at leaf node the depth and path both are zero
        return 0,0

# we are maintaining two thing in return ,max depth and longest path , at each level we compute the path using the above expression 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.solve(root)[1]-1