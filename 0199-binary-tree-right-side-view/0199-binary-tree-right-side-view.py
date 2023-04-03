# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mp={}
        def traverse(root,level):
            if root:
                # print(level)
                mp[level]=root.val
                traverse(root.left,level+1)
                traverse(root.right,level+1)
            
        traverse(root,0)
        return mp.values()
                
            
            
            
        