class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(list)
        time = [float("inf") for _ in range(n)]
        time[k-1] = 0
        visited = set()

        for u,v,w in times:
            adjList[u].append((v,w))
        
        heap = [(0, k)]

        while heap:
            # print(heap)
            currTime, node = heapq.heappop(heap)

            if node in visited:
                continue
            visited.add(node)

            for neigh, ti in adjList[node]:
                if currTime + ti < time[neigh-1]:
                    time[neigh-1] = currTime + ti
                    heapq.heappush(heap, (currTime + ti, neigh))
        # print(time)
        # print(adjList)
        Max = max(time)

        if Max == float("inf"):
            return -1
        return Max
