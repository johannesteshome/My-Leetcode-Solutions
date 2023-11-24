class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        Max = 0
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()

        def dfs(x, y):
            nonlocal area
            if not (0 <= x < m) or not (0 <= y < n):
                return
            if grid[x][y] == 0 or (x,y) in visited:
                visited.add((x,y))
                return
            else:
                visited.add((x,y))
                area += 1

            for dir in direction:
                dfs(x+dir[0], y+dir[1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                area = 0
                dfs(i, j)
                Max = max(Max, area)

        return Max
