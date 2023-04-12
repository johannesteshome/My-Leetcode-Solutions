class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        m = len(grid1)
        n = len(grid1[0])
        count = 0

        def dfs(x, y):
            nonlocal notFound
            if not (0 <= x < m) or not (0 <= y < n):
                return
            if grid2[x][y] == 0 or (x,y) in visited:
                return
            else:
                if grid1[x][y] != 1:
                    notFound = True
                    return

            visited.add((x,y))

            for dir in direction:
                dfs(x+dir[0], y+dir[1])

        for i in range(len(grid2)):
            for j in range(len(grid2[i])):
                
                if (i,j) not in visited and grid2[i][j] == 1:
                    notFound = False
                    dfs(i,j)
                    if not notFound:
                        count += 1
        return count