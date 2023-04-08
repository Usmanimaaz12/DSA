# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        traversed=set()
        Tsum=k
        def solve(root):
            if root:
                toFind=Tsum-root.val
                if toFind in traversed:
                    return 1
                else:
                    traversed.add(root.val)
                    return solve(root.left) or solve(root.right)
                    
            return 0
        return solve(root)
        