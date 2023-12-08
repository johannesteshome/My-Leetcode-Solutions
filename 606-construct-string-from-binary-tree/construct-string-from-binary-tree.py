# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[]
        if not root:
            return

        ans.append(str(root.val))

        if root.left:
            ans.append('('+self.tree2str(root.left)+')')

        if root.right:
            if not root.left:
                ans.append('()')

            ans.append('('+self.tree2str(root.right)+')')

        return "".join(ans)