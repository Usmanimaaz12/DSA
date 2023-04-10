# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     count = 0
#     ans = None 
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#             if root:
#                 global ans, count 
#                 self.kthSmallest(root.left,k)
#                 count+=1
#                 if count == k :
#                     n = root.val
#                 elif count<k:
#                     self.kthSmallest(root.right,k)
#             return ans
           
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        arr = self.inorder(root,values)
        return arr[k-1]
    
    #Driver Function For Inorder Traversal
	#Inorder Traversal means Left -> Root -> Right
	
    def inorder(self,root,a):
        if(root):
            self.inorder(root.left,a)
            a.append(root.val)  #Storing The Values in the Array which is passed as an argument
            self.inorder(root.right,a)
        return a