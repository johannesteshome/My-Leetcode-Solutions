"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        visited = set()
        Max = 0

        def dfs(root, level):
            nonlocal Max
            if not root:
                return
            # if root.val in visited:
            #     return 
            
            # visited.add(root.val)
            Max = max(Max, level)

            for child in root.children:
                dfs(child, level+1)
        
        dfs(root, 1)
        return Max