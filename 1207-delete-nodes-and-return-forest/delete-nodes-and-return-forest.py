# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        answer = []
        td = []

    
        def dfs(curr, toInsert):

            nullify = False

            if not curr:
                return
            
            if toInsert and curr.val not in to_delete:
                answer.append(curr)
            
            if curr.val in to_delete:
                left = dfs(curr.left, True)
                right = dfs(curr.right, True)
                nullify = True
            else:
                left = dfs(curr.left, False)
                right = dfs(curr.right, False)
            
            if left:
                curr.left = None
            if right:
                curr.right = None
            
            return nullify

            


        
        dfs(root, root.val not in to_delete)
    
        return answer
        