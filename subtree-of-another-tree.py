# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p, q):
            if not p and q:
                return False
            if not q and p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            else:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        def subTree(root, subRoot):
            if not root:
                return root
            if not subRoot:
                return False
            
            if isSameTree(root, subRoot):
                return True
            
            return subTree(root.left, subRoot)  or subTree(root.right, subRoot)
        
        return subTree(root, subRoot)