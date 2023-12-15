class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adjList = defaultdict(int)
        for src, dest in paths:
            adjList[src] += 1
            adjList[dest] = adjList[dest]
        
        # print(adjList)
        
        for k in adjList:
            if adjList[k] == 0:
                return k
        