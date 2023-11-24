# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        adjList = defaultdict(list)
        queue = deque([root])
        visited = set()
        answer = []

        def dfs(node, level):
            # print(node, level)
            visited.add(node)

            for neighbour in adjList[node]:
                if neighbour not in visited:
                    if level == k:
                        answer.append(neighbour)
                    else:
                        dfs(neighbour, level+1)

        while queue:
            node = queue.popleft()

            if node.right:
                adjList[node.val].append(node.right.val)
                adjList[node.right.val].append(node.val)
                queue.append(node.right)
            if node.left:
                adjList[node.val].append(node.left.val)
                adjList[node.left.val].append(node.val)
                queue.append(node.left)

        # print(adjList)

        for keys in adjList:
            # print(keys)
            if keys == target.val:
                dfs(keys, 1)

        return answer