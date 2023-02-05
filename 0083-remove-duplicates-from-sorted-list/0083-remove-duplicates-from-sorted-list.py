# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        
        if not head:
            return head
    
        dummy=head
        prev=dummy
        dummy=dummy.next
        while dummy:
            if dummy.val==prev.val:
                prev.next=dummy.next
                dummy=dummy.next
            else:
                prev=dummy
                dummy=dummy.next
        return head
