class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = defaultdict(list)
        visited = set()
        probs = [float("-inf") for _ in range(n)]
        probs[0] = -1

        for i, edge in enumerate(edges):
            adjList[edge[0]].append([edge[1], succProb[i]])
            adjList[edge[1]].append([edge[0], succProb[i]])
        heap = [(-1, start_node)]
        # print(adjList)

        if len(adjList[end_node]) == 0:
            return 0

        while heap:
            # print(heap)
            currProb, currNode = heappop(heap)

            if currNode in visited:
                continue
            
            visited.add(currNode)
            # print(visited)
            
            
            for neigh, prob in adjList[currNode]:
                p = -1 * currProb * prob
                if p > probs[neigh]:
                    # print(neigh, p, "here")
                    probs[neigh] = p
                    heappush(heap, (-1 * p, neigh))

        if probs[end_node] == float("-inf"):
            return 0.0
        return probs[end_node]