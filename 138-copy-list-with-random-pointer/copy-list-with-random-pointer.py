"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = head
        count = 0
        hashmap = defaultdict()
        copyNode = Node(0)
        newDummy = copyNode

        while dummy:
            newDummy.val = dummy.val
            newDummy.next = dummy.next

            hashmap[count] = newDummy

            dummy.val = (dummy.val, count)

            if dummy.next:
                count += 1

                newNode = Node(0)
                newDummy.next = newNode
                newDummy = newDummy.next
                
            dummy = dummy.next
        
        # print(hashmap)
        dummy = head
        newDummy = copyNode

        while dummy:
            if dummy.random:
                index = dummy.random.val[1]
                newDummy.random = hashmap[index]
            
            dummy = dummy.next
            newDummy = newDummy.next
        
        return copyNode