# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head = list1
        head2 = list2
        count = 0
        # start = None

        while head:
            if count == a-1:
                start = head
            if count == b+1:
                end = head
            head = head.next
            count += 1
        
        start.next = head2

        while head2.next:
            head2 = head2.next
        
        head2.next = end

        return list1
        