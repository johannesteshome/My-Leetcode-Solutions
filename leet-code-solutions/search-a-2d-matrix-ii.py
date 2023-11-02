class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        visited = set()
        i = 0
        j = 0
        while 0 <= i < len(matrix) and 0 <= j < len(matrix[i]):
            visited.add((i, j))
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                if j+1 < len(matrix[i]):
                    j += 1
                else:
                    i += 1
            else:
                if (i, j-1) in visited:
                    i += 1
                j -= 1
        
        return False