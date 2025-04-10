# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])

        while queue:
            items = set()
            for _ in range(len(queue)):
                node = queue.popleft()

                items.add(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if node.left and node.right:
                    if set([node.left.val, node.right.val]) == set([x,y]):
                        return False
            
            if x in items and y in items:
                return True
        
        return False

