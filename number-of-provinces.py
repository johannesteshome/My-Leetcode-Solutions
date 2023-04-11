class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()

        def dfs(index):
            for i in range(len(isConnected[index])):
                if i not in visited and isConnected[index][i] == 1:
                    visited.add(i)
                    dfs(i)

        for j in range(len(isConnected)):
            if j not in visited:
                provinces += 1
                dfs(j)

        return provinces