class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dire = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
        n = len(heights)
        m = len(heights[0])

        heap = [(0, 0, 0)]
        heapify(heap)
        visited = set()

        while heap:
            dist, row, col = heappop(heap)

            if (row, col) in visited:
                continue
            
            if (row,col) == (n-1, m-1):
                return dist
            visited.add((row, col))
            for i in dire:
                x,y = row + dire[i][0], col + dire[i][1]

                if 0<=x < n and 0<=y < m:
                    heappush(heap, (max(dist, abs(heights[x][y] - heights[row][col])), x,y))