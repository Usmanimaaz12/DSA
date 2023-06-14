class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def helper(root):
            if root:
                helper(root.left)
                trav.append(root.val)
                helper(root.right)
        
        trav = []
        helper(root)
        
        return min(trav[i+1] - trav[i] for i in range(len(trav) - 1))