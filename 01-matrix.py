class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        m, n = len(mat), len(mat[0])
        queue = deque()
        visited = set()

                
        for i in range(m):
            row = []
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        
        

        while queue:
            node = queue.popleft()
                # print(node)
            for dir in direction:
                nx = node[0] + dir[0]
                ny = node[1] + dir[1]

                if 0 <= nx < m and 0 <= ny < n:
                    if (nx, ny) not in visited:
                        mat[nx][ny] = mat[node[0]][node[1]] + 1
                        queue.append((nx, ny))
                        visited.add((nx, ny))

        return mat