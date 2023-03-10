# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        map = defaultdict(list)
        Max = float("-inf")

        def maxWidth(root, level, idx):
            if not root:
                return

            map[level].append(idx)

            left = maxWidth(root.left, level+1, 2*idx)
            right = maxWidth(root.right, level+1, 2*idx+1)

        maxWidth(root, 1, 1)
        
        for m in map:
            Max = max(Max, (map[m][-1] - map[m][0]) + 1)

        return Max