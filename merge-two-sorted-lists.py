# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # newHead = dummyHead = ListNode()
        # while list1 and list2:
        #     if list1.val < list2.val:
        #         dummyHead.next = list1
        #         list1 = list1.next
        #     else:
        #         dummyHead.next = list2
        #         list2 = list2.next
        #     dummyHead = dummyHead.next
        
        # if list1:
        #     dummyHead.next = list1
        # if list2:
        #     dummyHead.next = list2
        # return newHead.next

        newHead = dummyHead = ListNode()
        node1 = list1
        node2 = list2

        def merge():
            # print(node1, node2)
            nonlocal dummyHead
            nonlocal node1
            nonlocal node2
            if not node1 or not node2:
                return 

            if node1.val < node2.val:
                dummyHead.next = node1
                node1 = node1.next
            else:
                dummyHead.next = node2
                node2 = node2.next
            
            dummyHead = dummyHead.next
            merge()
        
        merge()
        # print(newHead, node1)
        if node1:
            dummyHead.next = node1
        if node2:
            dummyHead.next = node2
        return newHead.next