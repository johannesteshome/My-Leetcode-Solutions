# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        Map = defaultdict(list)
        newMap = defaultdict(list)

        def vert(root, pos):
            if not root:
                return 
           
           # store the values on a dictionary where the key is (col, row)
            Map[(pos[1], pos[0])].append(root.val)
            if len(Map[(pos[1], pos[0])]) > 1:
                Map[(pos[1], pos[0])].sort()

            vert(root.left, [pos[0]+1, pos[1]-1])
            vert(root.right, [pos[0]+1, pos[1]+1])
        
        vert(root, [0,0])
        
        # sort the dictionary based on the column
        nMap = OrderedDict(sorted(Map.items()))

        # store the lists with the same column in another dictionary
        for n in nMap:
            newMap[int(n[0])].extend(nMap[n])

        return list(newMap.values())