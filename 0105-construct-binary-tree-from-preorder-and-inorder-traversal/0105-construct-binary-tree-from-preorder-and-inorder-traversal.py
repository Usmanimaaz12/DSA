# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            n1=len(preorder)
            n2=len(inorder)
            inomap={i:el for el,i in enumerate(inorder)}
      
            def get_tree(prestart,preend,instart,inend):
                ino_idx=inomap[preorder[prestart]]
                l=ino_idx-instart
                r=inend-ino_idx
                root=ListNode(preorder[prestart])
                root.left=get_tree(prestart+1,prestart+l,instart,ino_idx-1) if l else None
                root.right=get_tree(prestart+l+1,preend,ino_idx+1,inend) if r else None
                return root
            return get_tree(0,n1-1,0,n2-1)
                      
        