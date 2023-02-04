# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        smallLists = ListNode(-1)
        largeLists = ListNode(-1)
        smallHead = smallLists
        largeHead = largeLists
        
        while head:
            
            if head.val < x:
                smallLists.next = head
                head = head.next
                smallLists = smallLists.next
                smallLists.next = None
            
            else:
                largeLists.next = head
                head = head.next
                largeLists = largeLists.next
                largeLists.next = None
        
        smallLists.next = largeHead.next
        
        return smallHead.next