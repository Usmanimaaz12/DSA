# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pre,curr,ne=head,head.next,head.next.next
        while ne:
            curr.next=pre
            pre=curr
            curr=ne
            ne=ne.next
        head.next=None
        curr.next=pre
        return curr
        
        