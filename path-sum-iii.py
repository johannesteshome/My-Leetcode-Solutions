# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        Map = defaultdict(int)
        prefixSum = 0
        count = 0

        Map[0] = 1

        def sumPath(root):
            # print(targetSum)
            nonlocal prefixSum
            nonlocal Map
            nonlocal count

            if not root:
                return
            
            prefixSum += root.val

            if prefixSum - targetSum in Map:
                count+=Map[prefixSum - targetSum]
            
            Map[prefixSum] += 1

            sumPath(root.left)
            sumPath(root.right)
            Map[prefixSum] -= 1
            prefixSum -= root.val
            return
        sumPath(root)
        return count