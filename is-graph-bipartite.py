class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        color=defaultdict(int)

        def dfs(node,curr):

            if node in color:
                return color[node]==curr

            color[node]=curr

            for neighbour in graph[node]:
                found=dfs(neighbour,1-curr)
                if not found:
                    return False
            return True

        for key in range(len(graph)):
            if key not in color:
                res=dfs(key,1)
                if not res:
                    return False
        return True