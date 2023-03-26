# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base case 1 : dono me se koi ek na ho
        if p and not q or  q and not p:
            return 0
#         dono na ho
        if not p and not q :
            return 1
#         if dono ke child hain to check kro unpe above conditions
# values bhi check kro
        if p and q:
            if p.val != q.val:
                return 0
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
        