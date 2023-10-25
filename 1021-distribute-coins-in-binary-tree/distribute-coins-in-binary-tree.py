# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # return -1
        count = 0
        def dfs(curr):
            nonlocal count
            if not curr.right and not curr.left:
                if curr.val == 1:
                    return 0
                elif curr.val == 0:
                    return 1
                else:
                    return -(curr.val - 1)

            
            if curr.left:
                left = dfs(curr.left)
                if left < 0:
                    curr.val += (-1 *left)
                    count += (-1 *left)
                    left = 0
            else:
                left = 0
            if curr.right:
                right = dfs(curr.right)
                if right < 0:
                    curr.val += (-1 * right)
                    count += (-1 *right)
                    right = 0
            else:
                right = 0
            
            print(left, right, curr.val)

            if left + right == 0:
                return -(curr.val - 1)
            if curr.val == 0:
                count += (left+right)
                return left + right + 1
        
            count += (left + right)
            return (left + right) - (curr.val - 1)
                

        dfs(root)
        return count
        