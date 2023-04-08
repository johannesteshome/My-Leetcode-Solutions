class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        adjList = {}
        Max = 0

        for i in range(n):
            adjList[i] = []

        for road in roads:
            adjList[road[0]].append(road[1])
            adjList[road[1]].append(road[0])

        # print(adjList)

        for i in range(n-1):
            for j in range(i+1, n):
                if j in adjList[i]:
                    rank = len(adjList[i]) + len(adjList[j]) - 1
                else:
                    rank = len(adjList[i]) + len(adjList[j])
                # print(rank, i, j)
                Max = max(rank, Max)

        return Max