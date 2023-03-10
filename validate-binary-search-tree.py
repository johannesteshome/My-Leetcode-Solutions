# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answer = []
        maxNum = float("-inf")

        def traverse(root):
            nonlocal maxNum
            if not root:
                return True
            
            left = traverse(root.left)
            if not left:
                return False
            if maxNum >= root.val:
                return False
            maxNum = max(maxNum, root.val)
            right = traverse(root.right)
            if not right:
                return False
            return True

        return traverse(root)