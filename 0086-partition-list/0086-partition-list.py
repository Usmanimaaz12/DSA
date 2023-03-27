# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_left=l1=ListNode(101)
        dummy_right=l2=ListNode(102)
        while head:
            if head.val<x:
                l1.next=head
                l1=l1.next
            else:
                l2.next=head
                l2=l2.next
            head=head.next
        l2.next=None
        l1.next=dummy_right.next
        return dummy_left.next
        
        
                
        
        