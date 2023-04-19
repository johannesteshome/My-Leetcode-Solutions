class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        direction = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = set()
        regions = []

        def dfs(x, y):
            # print(x,y)
            nonlocal area
            if not (0 <= x < m) or not (0 <= y < n):
                area = False
                return
            if board[x][y] == 'X' or (x,y) in visited:
                # visited.add((x,y))
                return
            else:
                region.append((x,y))
                visited.add((x,y))

            for dir in direction:
                dfs(x+dir[0], y+dir[1])
                

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i,j) not in visited:
                    area = True
                    region = []
                    dfs(i, j)
                    regions.append([region])
                    regions[-1].append(area)

        print(regions)
        # print(dumpSet, "dump")
        for region in regions:
            if region[1]:
                for coordinate in region[0]:
                    board[coordinate[0]][coordinate[1]] = "X"