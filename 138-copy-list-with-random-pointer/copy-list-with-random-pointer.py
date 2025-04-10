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
        visited = {}
        # copyNode = Node(0)
        # newDummy = copyNode

        while dummy:
            if dummy not in visited:
                newNode = Node(dummy.val)
                visited[dummy] = newNode
            
            if dummy.next and dummy.next in visited:
                visited[dummy].next = visited[dummy.next]
            elif dummy.next and dummy.next not in visited:
                newNode = Node(dummy.next.val)
                visited[dummy.next] = newNode
                visited[dummy].next = newNode
            
            if dummy.random and dummy.random in visited:
                visited[dummy].random = visited[dummy.random]
            elif dummy.random and dummy.random not in visited:
                newNode = Node(dummy.random.val)
                visited[dummy.random] = newNode
                visited[dummy].random = newNode
            
            dummy = dummy.next
        
        return visited[head]