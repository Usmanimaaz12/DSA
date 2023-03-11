# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
#          step-1    == Setting positions of left and right   
        if left==right:
            return head
        DUMMY=ListNode(100,head)
        p1,p2=DUMMY,DUMMY
        
        while right+1:
            p1=p1.next
            right-=1
        while left-1:
            p2=p2.next
            left-=1
#        step-2   reversing from left+1 to right-1  
        h2=p2.next
        
        
        p=h2
        c=h2.next
        n=h2.next.next
        while n!=p1:
            c.next=p
            p=c
            c=n
            n=n.next
        c.next=p
#         joining the link
        p2.next=c
        h2.next=p1
        return DUMMY.next
        
            
    
        