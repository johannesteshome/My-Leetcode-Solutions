class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        dire = [(-1, 0), (1,0), (0, -1), (0, 1)]
        n = len(grid)

        def find(member):
            if member == unionSet[member]:
                return member
            
            unionSet[member] = find(unionSet[member])
            return unionSet[member]

        def union(member1, member2):
            repMember1 = find(member1)
            repMember2 = find(member2)

            if repMember1 != repMember2:
                if size[repMember1] < size[repMember2]:
                    unionSet[repMember1] = repMember2
                    size[repMember2] += size[repMember1]
                else:
                    unionSet[repMember2] = repMember1
                    size[repMember1] += size[repMember2]
        
        unionSet = {}
        size = {}
        visited = set()

        for i in range(n):
            for j in range(n):
                unionSet[(i, j)] = (i, j)
                size[(i,j)] = 1


        def dfs(i, j):
            # print("dfs", i, j)

            for d in dire:
                x = i + d[0]
                y = j + d[1]

                if 0 <= x < n and 0 <= y < n:
                    # print("waht about here", x,y, grid[x][y])
                    if grid[x][y] == 1 and (x,y) not in visited:
                        # print("here", x,y)
                        visited.add((x,y))
                        union((i,j), (x,y))
                        dfs(x, y)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    # print(i,j, "here for initial")
                    visited.add((i,j))
                    dfs(i, j)

        
        ans = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    unions = set()
                    total = 0
                    for d in dire:
                        x = i + d[0]
                        y = j + d[1]

                        if 0 <= x < n and 0 <= y < n:
                            if grid[x][y] == 1:
                                unions.add(find((x,y)))
                    for u in unions:
                        total += size[u]
                    ans = max(ans, total + 1)


        
        # print(unionSet, size)

        return max(ans, max(size.values()))
        