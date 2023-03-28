# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        ans=[]
        q=deque([None,root])
        
#         our answer will include last element of each level
        while q:
            x=q.pop()
            if x:
#                 applying condition to check that is it last element
                if q[-1] is None:
                    ans.append(x.val)
                if x.left:
                    q.appendleft(x.left)
                if x.right:
                    q.appendleft(x.right)
            else:
                if q:
                    q.appendleft(None)
        return ans
            
            
            
        