# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        heap = [(root.val, 0, root)]
        visited = set()
      
        count = 0

        while heap:
            
            Sum, index, node = heappop(heap)
            # print(Sum)

            if Sum == targetSum:
                count += 1
            
            if node.right:
                heappush(heap, (Sum + node.right.val, random.random(), node.right))
                if node.right not in visited:
                    # print(Sum, node.right.val, "single")
                    visited.add(node.right)
                    heappush(heap, (node.right.val, random.random(), node.right))
            if node.left:
                heappush(heap, (Sum + node.left.val, random.random(), node.left))
                if node.left not in visited:
                    visited.add(node.left)
                    heappush(heap, (node.left.val, random.random(), node.left))
        
        return count
        
        