# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def avg(root, Sum):
            nonlocal count
            if not root:
                return [0, 0]

            left = avg(root.left, Sum)
            right = avg(root.right, Sum)
            print(right, root.val)

            
            if (left[0] + right[0] + root.val) // (left[1] + right[1] + 1) == root.val:
                print(root.val)
                count += 1
            
            Sum += root.val
            return [left[0] + right[0] + root.val, left[1] + right[1] + 1]
        
        avg(root, 0)
        return count