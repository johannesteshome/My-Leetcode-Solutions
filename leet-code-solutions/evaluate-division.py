class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjList = defaultdict(list)

        for i, eq in enumerate(equations):
            adjList[eq[0]].append([eq[1], values[i]])
            adjList[eq[1]].append([eq[0], 1/values[i]])
        
        def dfs(node, dest):

            if node in adjList:
                if node == dest:
                    return 1
                for neigh, val in adjList[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        res = dfs(neigh, dest)
                        if res:
                            return val * res
            
        answer = []
        for q in queries:
            visited = set()
            res = dfs(q[0], q[1])
            if not res:
                answer.append(-1.0)
            else:
                answer.append(res)
        
        return answer