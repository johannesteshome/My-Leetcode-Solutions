# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head
        node1 = head
        while node:
            node = node.next
            length += 1
        if length==1:
            head = None
            return head         
        i = 1
        k = length-n

        if n==length:
            head = head.next
            return head

        while i<k:
            node1 = node1.next
            i+=1
       
        if node1.next.next:
            node1.next = node1.next.next
        else:
            node1.next = None

        return head