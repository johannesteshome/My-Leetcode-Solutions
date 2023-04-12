# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums = []

        def sumNums(root, num):
            # print(num, root.val)
            if not root:
                return
            num += str(root.val)
            # print(num, "after")
            if not root.left and not root.right:
                nums.append(int(num))
                return
            
            
            sumNums(root.left, num)
            sumNums(root.right, num)
        
        sumNums(root, "")
        print(nums)
        return sum(nums)