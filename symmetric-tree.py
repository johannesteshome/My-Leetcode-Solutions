# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.right
        q = root.left
        def compare(p,q):
            if not p and q:
                return False
            if not q and p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            else:
                return compare(p.left, q.right) and compare(p.right, q.left)
        return compare(p,q)