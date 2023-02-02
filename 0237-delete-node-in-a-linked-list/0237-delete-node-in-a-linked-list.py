# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        curr = node
        Next = node.next
        
        while curr:
            curr.val = Next.val
            if Next.next:
                curr = Next
                Next = Next.next
            else: 
                curr.next = None
                curr = curr.next
            
        
        
        