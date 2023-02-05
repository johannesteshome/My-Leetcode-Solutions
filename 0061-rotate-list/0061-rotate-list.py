# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head
        newHead = None
        length = 0
        if k == 0:
            return head
        
        
        while dummy:
            length += 1
            dummy = dummy.next
            
        if length == 0:
            return head
        rotate = k%length
        
        if rotate == 0:
            return head
        
        
        dummy = head
        Next = dummy.next
        
        for i in range((length - rotate) - 1):
            dummy = Next
            Next = Next.next
            
        dummy.next = None
        newHead = Next
        
        while Next.next:
            Next = Next.next
            
        Next.next = head
        
        return newHead
            