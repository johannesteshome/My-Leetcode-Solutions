# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        pointer = head
        queue = deque([])
        length = 0
        newNode = ListNode()

        while pointer:
            queue.append(pointer.val)
            pointer = pointer.next
            length += 1

        pointer = head
        # print(queue)

        while queue:
            # print(queue)
            if queue:
                pointer.val = queue.popleft()
                pointer = pointer.next
            if queue:
                pointer.val = queue.pop()
                pointer = pointer.next
            