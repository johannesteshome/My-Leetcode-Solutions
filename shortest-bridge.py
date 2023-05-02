class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        queue = deque()
        n = len(grid)

        # to check if the coordinate is bound
        def inbound(x, y):
            nonlocal n
            return 0 <= x < n and 0 <= y < n
        
        # depth first search to find the first area
        def dfs(x, y):
            grid[x][y] = 2
            queue.append((x,y))

            for dir in direction:
                nx = x + dir[0]
                ny = y + dir[1]

                if inbound(nx, ny) and grid[nx][ny] == 1:
                    dfs(nx, ny)

        # to find the first starting point of the first area
        for i in range(n):
            if queue:
                break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    break

        # breadth first search to find the shortest distance between the first visited area and the second area
        distance = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                for dir in direction:
                    nx = node[0] + dir[0]
                    ny = node[1] + dir[1]

                    if inbound(nx,ny):
                        if grid[nx][ny] == 1:
                            return distance

                        if grid[nx][ny] == 0:
                            queue.append((nx, ny))
                            grid[nx][ny] = 2
            distance += 1