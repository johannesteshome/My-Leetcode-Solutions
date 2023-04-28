# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # visited = set()
        queue = deque()
        answer = []

        queue.append(root)
        # visited.add(root)
        Sum = root.val

        while queue:
            answer.append(Sum/len(queue))
            Sum = 0
            level = len(queue)

            for i in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    Sum += node.left.val
                if node.right:
                    queue.append(node.right)
                    Sum += node.right.val

        
        return answer