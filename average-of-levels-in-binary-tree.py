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
        answer.append(root.val)

        while queue:
            count = 0
            Sum = 0
            level = len(queue)
            

            for i in range(level):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    Sum += node.left.val
                    count += 1
                if node.right:
                    queue.append(node.right)
                    Sum += node.right.val
                    count += 1

            if count > 0:
                answer.append(Sum/count)
        
        return answer