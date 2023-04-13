# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        nodes = []
        Sum = 0
        def sumEven(root):
            nonlocal Sum
            if not root: return
            
            nodes.append(root.val)
            if len(nodes) >= 3 and nodes[-3]%2 == 0:
                Sum += root.val

            sumEven(root.left)
            sumEven(root.right)
            nodes.pop()

        sumEven(root)
        return Sum