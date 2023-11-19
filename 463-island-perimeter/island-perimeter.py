class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        answer = 0
        visited = set()
        found = False
        dir = [(-1,0), (1,0), (0,1), (0,-1)]

        def dfs(x, y):
            nonlocal answer

            for d in dir:
                newx = d[0] + x
                newy = d[1] + y

                if 0 <= newx < m and 0 <= newy < n:
                    if grid[newx][newy] == 0:
                        answer += 1
                    elif grid[newx][newy] == 1 and (newx, newy) not in visited:
                        visited.add((newx, newy))
                        dfs(newx,newy)
                else:
                    answer += 1


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
                    dfs(i,j)
                    found = True
                    break
            if found:
                break
        
        return answer