class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # adjList = defaultdict(list)
        # for flight in flights:
        #     adjList[flight[0]].append((flight[1], flight[2]))
        
        dist1 = [float("inf") for _ in range(n)]
        dist2 = [float("inf") for _ in range(n)]
        dist1[src] = 0
        dist2[src] = 0

        for _ in range(k+1):
            # print(queue)
            for _ in range(n - 1):
                for u, v, w in flights:
                    if dist1[u] != float("inf") and dist1[u] + w < dist2[v]:
                        dist2[v] = dist1[u] + w
            dist1 = dist2[:]
        
        print(dist1)
        if dist1[dst] == float("inf"):
            return -1
        return dist1[dst]
        
            