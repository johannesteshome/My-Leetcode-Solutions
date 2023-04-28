class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[m-1][n-1]:
            return -1


        direction = [(-1,0), (1,0), (0,-1), (0,1), (1,1), (-1,-1), (1,-1), (-1,1)]
        queue = deque([(0,0)])
        path = 1


        while queue:
            length = len(queue)

            for i in range(length):
                currentGrid = queue.popleft()
                
                if (n-1, n-1) == currentGrid:
                    return path
                

                for dir in direction:
                    x = currentGrid[0] + dir[0]
                    y = currentGrid[1] + dir[1]

                    if 0 <= x < m and 0 <= y < n:
                        if grid[x][y] == 0:
                            grid[x][y] = 1
                            queue.append((x,y))
                            
            path += 1
        
        return -1