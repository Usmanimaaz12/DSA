# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return root
        q=deque([None,root])        
        ans=[]
        curr=[]
        while q:
            x=q.pop()
            if x:
                curr.append(x.val)
                if x.left:
                    q.appendleft(x.left)
                if x.right:
                    q.appendleft(x.right) 
            else:
                if q:
                    q.appendleft(None)
                ans.append(curr)
                curr=[]
        return ans
                
        