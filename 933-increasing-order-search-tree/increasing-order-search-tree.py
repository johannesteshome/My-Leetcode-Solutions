# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        li = []

        def dfs(curr):
            if not curr:
                return
            
            dfs(curr.left)
            li.append(curr.val)
            dfs(curr.right)
        
        dfs(root)
        answer = TreeNode(li[0])
        res = answer

        for i in range(len(li) - 1):
            answer.right = TreeNode(li[i+1])
            answer = answer.right

        return res
        