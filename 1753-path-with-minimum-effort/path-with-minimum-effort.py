class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dire = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        m = len(heights)
        n = len(heights[0])
        dist = [[float("inf") for _ in range(n)] for _ in range(m)]
        
        
        heap = [(0, (0,0))]
        visted = set()
        while heap:
            weight, node = heapq.heappop(heap)
            if node == (m-1, n-1):
                return weight
            if node in visted:
                continue
            visted.add(node)
            
            # print(node, weight)
            for i in dire:
                x = node[0] + dire[i][0]
                y = node[1] + dire[i][1]
                if 0 <= x < m and 0 <= y < n:
                    currEffort = abs(heights[x][y] - heights[node[0]][node[1]])
                    if dist[x][y] > currEffort:
                        dist[x][y] = max(weight, currEffort)
                        heappush(heap, (dist[x][y], (x,y)))