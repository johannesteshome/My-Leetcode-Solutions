# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None
        print(slow.val)
        while slow:
            Next = slow.next
            slow.next = prev
            prev = slow
            slow = Next
            
        
        p = prev
        h = head
        while p:
            if p.val != h.val:
                return False
            p = p.next
            h = h.next
            
        return True
        print(prev, head)
            