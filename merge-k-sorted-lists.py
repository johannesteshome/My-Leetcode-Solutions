# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = head = ListNode()
        # initialize the first heap list having the first element of each list
        for i in range(len(lists)):
            if lists[i]:
                heap.append((lists[i].val, i, lists[i]))

        # heapify the heap array or list
        heapify(heap)

        
        # append the min element of the current heap to a new linked list and insert the next node in the heap
        while heap:
            val, index, node = heappop(heap)
            head.next = ListNode(val)
            head = head.next

            if node.next:
                heappush(heap, (node.next.val, index, node.next))


        return dummy.next