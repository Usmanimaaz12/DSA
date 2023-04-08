# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root,p,q):
            if root:
                if p<root.val and q>root.val:
                    return root
                elif p==root.val:
                    return root
                elif q==root.val:
                    return root
                elif p<root.val and q<root.val:
                    return solve(root.left,p,q)
                else:
                    return solve(root.right,p,q)
            return None
            
            
            
        return solve(root,min(p.val,q.val),max(p.val,q.val))
        