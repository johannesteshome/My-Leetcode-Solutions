class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        colors = {}
        if len(dislikes) == 0:
            return True
        
        for dislike in dislikes:
            adjList[dislike[0]].append(dislike[1])
            adjList[dislike[1]].append(dislike[0])

    

        def dfs(node, curr):
            if node in colors:
                return colors[node] == curr
            colors[node] = curr

            if node in adjList:
                for neighbour in adjList[node]:
                    if not dfs(neighbour, 1-curr):
                        return False
            return True
        
        for key in adjList:
            print(key)
            if key not in colors:
                res = dfs(key, 1)
                if not res:
                    return False
        return True
        # return dfs(list(adjList.keys())[1], 1)