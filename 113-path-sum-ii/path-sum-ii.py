# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        if not root:
            return []
        heap = [(root.val, 0, root)]
        ans = []
        dic = defaultdict()

        while heap:
            Sum, index, node = heappop(heap)

            if not node.right and not node.left:
                if Sum == targetSum:
                    ans.append(node)
                continue
            
            if node.right:
                # print(Sum,node.right.val)
                heappush(heap, (Sum + node.right.val, random.random(), node.right))
                dic[node.right] = node
            if node.left:
                heappush(heap, (Sum + node.left.val, random.random(), node.left))
                dic[node.left] = node
        
        def backtrack(node):
            # print(node)
            while node in dic:
                # print(path, "here")
                path.append(dic[node].val)
                node = dic[node]
            # path.append(node.val)
            return reversed(path)

        answer = []
        # print(ans)
        # print(dic)
        for a in ans:
            path = [a.val]
            answer.append(backtrack(a))

        return answer

        