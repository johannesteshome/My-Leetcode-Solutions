# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:

        queue = deque([root])
        level = 0

        while queue:
            # print(level, 'level')
            prev = None

            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 != 0:
                        if not prev:
                            prev = node.val
                        else:
                            if prev < node.val:
                                prev = node.val
                            else:
                                return False
                    else:
                        return False
                else:
                    if node.val % 2 == 0:
                        if not prev:
                            prev = node.val
                        else:
                            if prev > node.val:
                                prev = node.val
                            else:
                                return False
                    else:
                        return False
                if node.left:
                    # print('here')
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            # print(stack, 'stack')
                
        return True
        