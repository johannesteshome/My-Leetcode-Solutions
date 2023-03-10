# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        path = ""

        def treePath(root, path):
            nonlocal answer
            if not root:
                return 

            path = path + str(root.val) + "->"
            if not root.left and not root.right:
                answer.append(path[:-2])
                return

            treePath(root.left, path)
            treePath(root.right, path)
            
        treePath(root, path)
        return answer