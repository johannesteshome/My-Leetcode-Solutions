# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        map = defaultdict(list)
        if not root:
            return []
        def depth(root, level):
            map[level].append(root.val)

            if root.left:
                depth(root.left, level+1)
            if root.right:
                depth(root.right, level+1)

            return 
        depth(root,0)
        ans = []
        for vals in map.values():
            ans.append(vals[-1])
        return ans