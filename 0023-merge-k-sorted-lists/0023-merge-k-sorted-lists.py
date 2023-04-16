# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            cur = dummy = ListNode()
            while list1 and list2:               
                if list1.val < list2.val:
                    cur.next = list1
                    list1, cur = list1.next, list1
                else:
                    cur.next = list2
                    list2, cur = list2.next, list2
                
            if list1 or list2:
                cur.next = list1 if list1 else list2
            
            return dummy.next
            
        if len(lists)==0:
            return None
        ans=lists[0]
        for i in range(1,len(lists)):
            ans=mergeTwoLists(ans,lists[i])
        return ans
        
#         NEXT APPROACH IS TO MERGE USING HEAPS