class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        heap = []

        for i in range(len(dist)):
            heap.append(math.ceil(dist[i]/speed[i]))
        
        heapify(heap)

        time = 0
        while heap:
            current = heappop(heap)

            if current <= time:
                return time
            
            time += 1

        
        return time