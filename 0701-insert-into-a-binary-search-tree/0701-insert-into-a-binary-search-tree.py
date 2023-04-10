# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=root
        if not root:
            return TreeNode(val)
        while temp:
            if val < temp.val:
                if not temp.left:
                    break
                temp=temp.left
            elif val>temp.val:
                if not temp.right:
                    break
                temp=temp.right
        x=TreeNode(val)
        if val<temp.val:
            temp.left=x
        else:
            temp.right=x
        return root
        
                
        