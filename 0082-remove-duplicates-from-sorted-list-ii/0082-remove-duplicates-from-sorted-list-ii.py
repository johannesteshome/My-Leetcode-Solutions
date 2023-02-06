# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        # newHead = None
        
        if not head:
            return head
        if not head.next:
            return head
        
        Next = head.next
        flag = False
        
        while Next:
            if curr.val != Next.val and not flag:
                prev = curr
                curr = Next
                Next = Next.next
            elif curr.val == Next.val:
                flag = True
                if Next.next:
                    Next = Next.next
                else:
                    if prev:
                        prev.next = None
                        Next = Next.next
                    else:
                        head = None
                        return head
            elif curr.val != Next.val and flag:
                if prev == None:
                    head = Next
                    curr = Next
                    Next = Next.next
                    flag = False
                else:
                    prev.next = Next
                    curr = Next
                    Next = Next.next
                    flag = False
                    
        return head