class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for flight in flights:
            adjList[flight[0]].append((flight[1], flight[2]))
        
        heap = [(0, k, src)]
        visited = set()

        while heap:
            # print(heap)
            dist, k, node = heappop(heap) 

            if (node, k) in visited:
                continue
            visited.add((node, k))
            if k == -1:
                if node == dst:
                    return dist
                continue
            if node == dst:
                return dist

            for neigh in adjList[node]:
                heappush(heap, (neigh[1] + dist, k-1, neigh[0]))
                # if neigh[0] == dst:
                #     return neigh[1] + dist
        
        # if ans == float("inf"):
        #     return -1
        # return ans
        return -1