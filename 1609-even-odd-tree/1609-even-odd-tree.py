# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root,None])
        prev=0
        even=1
        while len(q)>1:
            el=q.popleft()
            if el:
                if even:
                    if el.val>prev and el.val%2:
                        prev=el.val
                    else:
                        return 0
                
                else:
                    if el.val<prev and not el.val%2:
                        prev=el.val
                    else:
                        return 0
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
                
            else:
                even= not even
                if even:
                    prev=0
                else:
                    prev=100000000
                q.append(None)
                
        return 1