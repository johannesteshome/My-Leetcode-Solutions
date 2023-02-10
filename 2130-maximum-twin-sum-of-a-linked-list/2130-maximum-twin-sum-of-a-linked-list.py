# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = head
        li = []
        ans = 0
        
        if not head.next.next:
            return head.val + head.next.val
        
        while dummy:
            li.append(dummy.val)
            dummy = dummy.next
            
        first = 0
        last = len(li) - 1
        
        while first < last:
            twinSum = li[first] + li[last]
            ans = max(ans, twinSum)
            first += 1
            last -= 1
        
        return ans