# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def traverse(root):
            if not root:
                return

            answer.append(root.val)
            traverse(root.left)
            traverse(root.right)
        
        traverse(root)
        
        count = Counter(answer)
        Max = max(count.values())
        ans = []
        for c in count:
            if count[c] == Max:
                ans.append(c)
        print(count, Max)
        return ans