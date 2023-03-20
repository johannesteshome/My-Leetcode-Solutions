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
            # print(Map, newMap)
            # if Map[(pos[0], pos[1])] == []:
            #     Map[(pos[0], pos[1])].append(root.val)
            #     newMap[pos[1]].append(root.val)
            # else:
            #     newMap[pos[1]].remove(Map[(pos[0], pos[1])][0])
            #     Map[(pos[0], pos[1])].append(root.val)
            #     Map[(pos[0], pos[1])].sort()
            #     newMap[pos[1]].extend(Map[(pos[0], pos[1])])
            Map[(pos[1], pos[0])].append(root.val)
            if len(Map[(pos[1], pos[0])]) > 1:
                Map[(pos[1], pos[0])].sort()

                

            vert(root.left, [pos[0]+1, pos[1]-1])
            vert(root.right, [pos[0]+1, pos[1]+1])
        
        vert(root, [0,0])
        # print(Map)
        # for m in Map:
        #     # print(m[1])
        #     if len(Map[m]) == 1:
        #         newMap[int(m[1])].extend(Map[m])
        #         newMap
        #     else:
        #         Map[m].sort()
        #         newMap[int(m[1])].extend(Map[m])
        nMap = OrderedDict(sorted(Map.items()))
        print(nMap)

        for n in nMap:
            newMap[int(n[0])].extend(nMap[n])

        # return newMap.values()
        
        
        # for item in Map.values():
        #     item.sort()
        
        return list(newMap.values())