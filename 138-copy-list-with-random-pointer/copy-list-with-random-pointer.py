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
        if head == None:
            return None
        oldList = head
        nodes = {}

        while oldList:
            nodes[oldList] = Node(0)
            oldList = oldList.next

        oldList = head
        
        while oldList:
            nodes[oldList].val = oldList.val
            if oldList.next:
                nodes[oldList].next = nodes[oldList.next]
            if oldList.random:
                nodes[oldList].random = nodes[oldList.random]
            oldList = oldList.next
        
        return list(nodes.values())[0]
            

        
        