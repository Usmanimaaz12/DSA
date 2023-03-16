# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy=ListNode(-60000,head)
        
        last_sorted=head
        curr=head.next
        
        while  curr:
            if curr.val>=last_sorted.val:
                last_sorted=last_sorted.next
            else:
                prev=dummy
                while prev.next.val<=curr.val:
                    prev=prev.next
                #inserting at the position
                last_sorted.next=curr.next
                curr.next=prev.next
                prev.next=curr
                
            curr=last_sorted.next
        return dummy.next