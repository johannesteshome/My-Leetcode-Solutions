# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 = []
        leaf2 = []

        def dfs(node, arr):
            if not node:
                return
            
            if not node.right and not node.left:
                arr.append(node.val)
            
            dfs(node.left, arr)
            dfs(node.right, arr)
        
        dfs(root1, leaf1)
        dfs(root2, leaf2)

        print(leaf1, leaf2)

        # if len(leaf1) == len(leaf2):
        #     for i in range(len(leaf1)):
        #         if leaf1[i] != leaf2[i]:
        #             return False
        #     return True

        # return False

        return leaf1 == leaf2