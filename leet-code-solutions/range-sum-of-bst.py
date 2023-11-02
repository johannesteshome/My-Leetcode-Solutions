# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        Sum = 0

        def dfs(node):
            nonlocal Sum

            if not node:
                return

            if low <= node.val <= high:
                Sum += node.val

            if low < node.val or high < node.val:
                dfs(node.left)
            if high > node.val or low > node.val:
                dfs(node.right)
        
        dfs(root)
        return Sum
        